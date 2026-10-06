/* GitHub-connector adapter for publication_pipeline.py bundles.
 * Load this file in functions.exec, then call publishDiscovery(tools, options).
 * No tokens, direct HTTP writes, or unsupported path-upload API are required.
 */
function publicationResult(result) {
  if (!result || result.isError) throw new Error(JSON.stringify(result));
  const value = result.structuredContent;
  if (!value) throw new Error('Missing structured connector result');
  return typeof value.content === 'string' ? JSON.parse(value.content) : value;
}

async function publishDiscovery(tools, options) {
  const { repository, branch, bundle, message } = options;
  if (!/^[\w.-]+\/[\w.-]+$/.test(repository) || !branch || !message || !bundle) {
    throw new Error('repository, branch, bundle and message are required');
  }
  // This adapter only advances an EXISTING explicitly selected ref. Branch/PR
  // creation and authorization remain the caller's responsibility.
  const repoURL = 'https://api.github.com/repos/' + repository;
  const refURL = repoURL + '/git/ref/heads/' + branch.split('/').map(encodeURIComponent).join('/');
  async function command(code) {
    const result = await tools.exec_command({cmd: "python - <<'PY'\n" + code + '\nPY', max_output_tokens: 40000});
    if (result.exit_code !== 0 || result.session_id) throw new Error('Local publication command failed: ' + result.output);
    return JSON.parse(result.output);
  }
  async function fetch(url) { return publicationResult(await tools.mcp__codex_apps__github_fetch({url})); }
  const local = await command('import json,sys\nfrom pathlib import Path\np=Path(' + JSON.stringify(bundle) + ')\n' +
    'print(json.dumps({"manifest":json.loads((p/"manifest.json").read_text()),"state":json.loads((p/"publication-state.json").read_text()) if (p/"publication-state.json").exists() else {}}))');
  const manifest = local.manifest;
  const state = local.state;
  const identity = {repository, branch, baseline: manifest.baseline_commit, input_digest: manifest.input_digest};
  if (state.identity && JSON.stringify(state.identity) !== JSON.stringify(identity)) throw new Error('Publication checkpoint belongs to another bundle/ref');
  state.identity = identity;
  state.blobs ||= {};
  async function verifyRemote() {
    const tree = await fetch(repoURL + '/git/trees/' + state.commit + '?recursive=1');
    if (tree.truncated) throw new Error('Cannot verify truncated remote tree');
    const entries = new Map(tree.tree.filter(e => e.type === 'blob').map(e => [e.path, e.sha]));
    for (const entry of manifest.files) if (entries.get(entry.path) !== entry.sha) throw new Error('Remote payload mismatch: ' + entry.path);
    state.authored_files_verified = true;
  }
  async function checkpoint() {
    await command('import json,os\nfrom pathlib import Path\np=Path(' + JSON.stringify(bundle) + ')/"publication-state.json"\n' +
      's=' + JSON.stringify(JSON.stringify(state)) + '\nt=p.with_suffix(".tmp")\nt.write_text(s+"\\n")\nos.replace(t,p)\nprint("true")');
  }
  // Verify all bytes before starting writes. Never trust an old checkpoint over
  // a newly modified payload or silently reuse a different manifest.
  await command('import json,hashlib\nfrom pathlib import Path\np=Path(' + JSON.stringify(bundle) + ')\n' +
    'm=json.loads((p/"manifest.json").read_text())\nfor e in m["files"]:\n r=Path(e["path"])\n assert not r.is_absolute() and ".." not in r.parts and ".git" not in r.parts\n b=(p/"payload"/r).read_bytes()\n assert len(b)==e["bytes"] and len(b.decode())==e["chars"]\n assert hashlib.sha1(b"blob "+str(len(b)).encode()+b"\\0"+b).hexdigest()==e["sha"]\n assert hashlib.sha256(b).hexdigest()==e["sha256"]\nprint("true")');
  const current = (await fetch(refURL)).object.sha;
  if (state.commit && current === state.commit) {
    await verifyRemote();
    state.ref_verified = true;
    await checkpoint();
    return state;
  }
  if (current !== manifest.baseline_commit) throw new Error('Branch advanced; regenerate against its current SHA and review the new diff');
  const parent = await fetch(repoURL + '/git/commits/' + current);
  const baselineTree = await fetch(repoURL + '/git/trees/' + parent.tree.sha + '?recursive=1');
  if (baselineTree.truncated) throw new Error('Cannot verify truncated baseline tree');
  const baselineBlobs = new Map(baselineTree.tree.filter(e => e.type === 'blob').map(e => [e.path, e.sha]));
  if (!Array.isArray(manifest.baseline_files)) throw new Error('Manifest needs verified baseline files');
  const inputs = new Map(manifest.baseline_files.map(e => [e.path, e.sha]));
  for (const [path, sha] of inputs) if (baselineBlobs.get(path) !== sha) throw new Error('Baseline input differs from current commit: ' + path);
  for (const entry of manifest.files) {
    if (baselineBlobs.has(entry.path) && !inputs.has(entry.path)) throw new Error('New publication path already exists: ' + entry.path);
  }
  const started = Date.now();
  for (const entry of manifest.files) {
    if (state.blobs[entry.path] === entry.sha) continue;
    const chunks = [];
    // The connector takes text, not local file paths. This bounded bridge stays
    // outside model context. It is unavoidable until that API supports files.
    for (let offset = 0; offset < entry.chars;) {
      const part = await command('import json\nfrom pathlib import Path\ns=(Path(' + JSON.stringify(bundle) + ')/"payload"/' + JSON.stringify(entry.path) + ').read_text()\n' +
        's=s[' + offset + ':' + (offset + 30000) + ']\nwhile True:\n r=json.dumps({"text":s,"chars":len(s)},ensure_ascii=False)\n if len(r.encode())<=32000: break\n s=s[:max(1,len(s)//2)]\nprint(r)');
      if (!part.chars || Array.from(part.text).length !== part.chars || offset + part.chars > entry.chars) throw new Error('Truncated file bridge read');
      chunks.push(part.text);
      offset += part.chars;
    }
    const blob = publicationResult(await tools.mcp__codex_apps__github_create_blob({repository_full_name: repository, encoding: 'utf-8', content: chunks.join('')}));
    if (blob.sha !== entry.sha) throw new Error('Uploaded blob SHA mismatch for ' + entry.path);
    state.blobs[entry.path] = blob.sha;
    await checkpoint();
  }
  if (!state.tree) {
    state.tree = publicationResult(await tools.mcp__codex_apps__github_create_tree({repository_full_name: repository, base_tree_sha: parent.tree.sha,
      tree_elements: manifest.files.map(e => ({path: e.path, mode: '100644', type: 'blob', sha: e.sha}))})).sha;
    await checkpoint();
  }
  if (!state.commit) {
    state.commit = publicationResult(await tools.mcp__codex_apps__github_create_commit({repository_full_name: repository, tree_sha: state.tree, parent_sha: current, message})).sha;
    await checkpoint();
  }
  // A lost response is not blindly retried. The next invocation reads the ref;
  // same commit means success, another head requires a freshly reviewed bundle.
  publicationResult(await tools.mcp__codex_apps__github_update_ref({repository_full_name: repository, branch_name: branch,
    sha: state.commit, expected_sha: current, force: false}));
  if ((await fetch(refURL)).object.sha !== state.commit) throw new Error('Publication ref verification failed');
  await verifyRemote();
  state.ref_verified = true;
  state.upload_and_commit_wall_seconds = (Date.now() - started) / 1000;
  await checkpoint();
  return state;
}

if (typeof module !== 'undefined') module.exports = {publishDiscovery, publicationResult};
