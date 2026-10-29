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

// The raw functions.exec isolate has no Node or Web Crypto/text-encoding APIs.
// SHA-1 here is only Git's existing object identity, never a security primitive.
function publicationUTF8(text, emit) {
  let bytes = 0, chars = 0;
  for (let i = 0; i < text.length; i++) {
    let c = text.charCodeAt(i);
    if (c >= 0xd800 && c <= 0xdbff) {
      const low = text.charCodeAt(++i);
      if (!(low >= 0xdc00 && low <= 0xdfff)) throw new Error('Invalid Unicode surrogate in bridge text');
      c = 0x10000 + ((c - 0xd800) << 10) + low - 0xdc00;
    } else if (c >= 0xdc00 && c <= 0xdfff) throw new Error('Invalid Unicode surrogate in bridge text');
    chars++;
    const octets = c < 0x80 ? [c] : c < 0x800 ? [0xc0 | (c >> 6), 0x80 | (c & 63)] : c < 0x10000 ?
      [0xe0 | (c >> 12), 0x80 | ((c >> 6) & 63), 0x80 | (c & 63)] :
      [0xf0 | (c >> 18), 0x80 | ((c >> 12) & 63), 0x80 | ((c >> 6) & 63), 0x80 | (c & 63)];
    bytes += octets.length;
    if (emit) for (const byte of octets) emit(byte);
  }
  return {bytes, chars};
}

function gitBlobDigest(text, expectedBytes) {
  const h = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0];
  const block = new Uint8Array(64), words = new Uint32Array(80);
  let used = 0, length = 0;
  const rotate = (n, bits) => (n << bits) | (n >>> (32 - bits));
  function byte(value) {
    block[used++] = value;
    length++;
    if (used !== 64) return;
    for (let i = 0; i < 16; i++) words[i] = (block[i * 4] << 24) | (block[i * 4 + 1] << 16) | (block[i * 4 + 2] << 8) | block[i * 4 + 3];
    for (let i = 16; i < 80; i++) words[i] = rotate(words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16], 1);
    let [a, b, c, d, e] = h;
    for (let i = 0; i < 80; i++) {
      const f = i < 20 ? (b & c) | (~b & d) : i < 40 ? b ^ c ^ d : i < 60 ? (b & c) | (b & d) | (c & d) : b ^ c ^ d;
      const k = i < 20 ? 0x5a827999 : i < 40 ? 0x6ed9eba1 : i < 60 ? 0x8f1bbcdc : 0xca62c1d6;
      const next = (rotate(a, 5) + f + e + k + words[i]) | 0;
      e = d; d = c; c = rotate(b, 30); b = a; a = next;
    }
    [a, b, c, d, e].forEach((value, i) => { h[i] = (h[i] + value) | 0; });
    used = 0;
  }
  publicationUTF8('blob ' + expectedBytes + '\0', byte);
  const metrics = publicationUTF8(text, byte);
  const high = Math.floor(length / 0x20000000), low = (length * 8) >>> 0;
  byte(0x80);
  while (used !== 56) byte(0);
  for (const value of [high, low]) for (let shift = 24; shift >= 0; shift -= 8) byte((value >>> shift) & 255);
  return {...metrics, sha: h.map(value => (value >>> 0).toString(16).padStart(8, '0')).join('')};
}

const PUBLICATION_OUTPUT_BYTES = 120000;
const PUBLICATION_OUTPUT_TOKENS = 40000;
const PUBLICATION_MIN_OUTPUT_BYTES = 1024;

async function publicationCommand(tools, code, allowTruncatedRead = false) {
  const result = await tools.exec_command({cmd: "python - <<'PY'\n" + code + '\nPY', max_output_tokens: PUBLICATION_OUTPUT_TOKENS});
  // Tool/auth failures and unfinished commands must never enter the retry path.
  if (!result || result.isError || result.exit_code !== 0 || result.session_id) throw new Error('Local publication command failed: ' + (result && result.output));
  if (result.original_token_count > PUBLICATION_OUTPUT_TOKENS || /^Warning: truncated output\b/.test(result.output)) {
    const error = new Error('Truncated file bridge output');
    error.retryBridgeRead = allowTruncatedRead;
    throw error;
  }
  return JSON.parse(result.output);
}

function publicationOutputLimit(value = PUBLICATION_OUTPUT_BYTES) {
  if (!Number.isSafeInteger(value) || value < PUBLICATION_MIN_OUTPUT_BYTES || value > PUBLICATION_OUTPUT_BYTES) throw new Error('Invalid bridge output byte limit');
  return value;
}

// Read-only: validate the exact selected manifest and payload once, then plan
// Unicode-safe byte ranges close to the serialized-output limit. No per-slice
// whole-file reads, and no dependency on an unavailable filesystem upload API.
async function planDiscoveryPayload(tools, {bundle, manifest, outputBytes}) {
  const limit = publicationOutputLimit(outputBytes);
  return publicationCommand(tools, 'import json,hashlib\nfrom pathlib import Path\np=Path(' + JSON.stringify(bundle) + ')\n' +
    'm=json.loads(' + JSON.stringify(JSON.stringify(manifest)) + ')\nlimit=' + limit + '\nplans=[]\n' +
    'for e in m["files"]:\n' +

    ' r=Path(e["path"])\n assert not r.is_absolute() and ".." not in r.parts and ".git" not in r.parts\n' +
    ' if e["sha"] is None:\n  assert not (p/"payload"/r).exists()\n  continue\n' +
    ' b=(p/"payload"/r).read_bytes()\n s=b.decode("utf-8")\n' +
    ' assert len(b)==e["bytes"] and len(s)==e["chars"]\n' +
    ' assert hashlib.sha1(b"blob "+str(len(b)).encode()+b"\\0"+b).hexdigest()==e["sha"]\n' +
    ' assert hashlib.sha256(b).hexdigest()==e["sha256"]\n' +
    ' chunks=[]\n start=0\n offset=0\n' +
    ' while start<len(s):\n' +
    '  lo=1\n  hi=min(len(s)-start,limit-256)\n' +
    '  while lo<hi:\n' +
    '   mid=(lo+hi+1)//2\n' +
    '   if len(json.dumps(s[start:start+mid],ensure_ascii=False).encode("utf-8"))<=limit-256: lo=mid\n' +
    '   else: hi=mid-1\n' +
    '  size=len(s[start:start+lo].encode("utf-8"))\n' +
    '  chunks.append({"offset":offset,"bytes":size,"chars":lo})\n  start+=lo\n  offset+=size\n' +
    ' plans.append({"path":e["path"],"chunks":chunks})\n' +
    'print(json.dumps(plans,separators=(",",":")))');
}

// Read-only and portable: benchmark this same loader with actual exec_command.
// Concurrency applies to reads only; publication mutations remain sequential.
async function loadDiscoveryFile(tools, {bundle, entry, plan, outputBytes, concurrency = 4}) {
  let limit = publicationOutputLimit(outputBytes);
  if (!Number.isSafeInteger(concurrency) || concurrency < 1 || concurrency > 4) throw new Error('Bridge read concurrency must be 1 through 4');
  if (!plan || plan.path !== entry.path || !Array.isArray(plan.chunks)) throw new Error('Missing file bridge plan');
  let expectedOffset = 0, expectedChars = 0;
  for (const chunk of plan.chunks) {
    if (chunk.offset !== expectedOffset || !Number.isSafeInteger(chunk.bytes) || chunk.bytes <= 0 || !Number.isSafeInteger(chunk.chars) || chunk.chars <= 0) throw new Error('Invalid file bridge plan order');
    expectedOffset += chunk.bytes;
    expectedChars += chunk.chars;
  }
  if (expectedOffset !== entry.bytes || expectedChars !== entry.chars) throw new Error('File bridge plan size mismatch');
  const texts = new Array(plan.chunks.length);
  const stats = {read_calls: 0, truncation_retries: 0, max_concurrent_reads: 0, output_byte_limit: limit};
  let next = 0, active = 0, failed;
  async function worker() {
    try {
      while (!failed && next < plan.chunks.length) {
        const index = next++, chunk = plan.chunks[index], pieces = [];
        let offset = chunk.offset, chars = 0;
        while (!failed && offset < chunk.offset + chunk.bytes) {
          const requestedLimit = limit;
          let part;
          try {
            stats.read_calls++;
            active++;
            stats.max_concurrent_reads = Math.max(stats.max_concurrent_reads, active);
            part = await publicationCommand(tools, 'import json\nfrom pathlib import Path\n' +
              '# publication-bridge-read\n' +
              'p=Path(' + JSON.stringify(bundle) + ')/"payload"/' + JSON.stringify(entry.path) + '\n' +
              'offset=' + offset + '\nsize=' + (chunk.offset + chunk.bytes - offset) + '\nlimit=' + requestedLimit + '\n' +
              'with p.open("rb") as f:\n f.seek(offset)\n b=f.read(size)\n' +
              'assert len(b)==size\ns=b.decode("utf-8")\n' +
              'def encode(n):\n t=s[:n]\n return json.dumps({"offset":offset,"bytes":len(t.encode("utf-8")),"chars":n,"text":t},ensure_ascii=False,separators=(",",":"))\n' +
              'lo=1\nhi=len(s)\nout=encode(hi)\n' +
              'if len(out.encode("utf-8"))+1>limit:\n' +
              ' while lo<hi:\n  mid=(lo+hi+1)//2\n  if len(encode(mid).encode("utf-8"))+1<=limit: lo=mid\n  else: hi=mid-1\n out=encode(lo)\n' +
              'assert len(out.encode("utf-8"))+1<=limit\nprint(out)', true);
          } catch (error) {
            if (!error.retryBridgeRead || requestedLimit <= PUBLICATION_MIN_OUTPUT_BYTES) throw error;
            limit = Math.min(limit, Math.max(PUBLICATION_MIN_OUTPUT_BYTES, Math.floor(requestedLimit / 2)));
            stats.truncation_retries++;
            stats.output_byte_limit = limit;
            continue;
          } finally { active--; }
          if (typeof part.text !== 'string') throw new Error('Invalid file bridge text');
          const metrics = publicationUTF8(part.text);
          if (part.offset !== offset || !Number.isSafeInteger(part.bytes) || part.bytes <= 0 || part.bytes !== metrics.bytes || part.chars !== metrics.chars || offset + part.bytes > chunk.offset + chunk.bytes) throw new Error('Truncated or reordered file bridge read');
          pieces.push(part.text);
          offset += part.bytes;
          chars += part.chars;
        }
        if (failed) return;
        if (chars !== chunk.chars) throw new Error('File bridge character count mismatch');
        texts[index] = pieces.join('');
      }
    } catch (error) {
      // Close the shared gate in this worker before a sibling continuation can
      // start another read. An outer await/catch would add a microtask gap.
      failed ||= error;
    }
  }
  // Drain already-running read-only calls before rejecting; do not launch more
  // after any worker fails, and never turn an auth failure into a smaller read.
  await Promise.all(Array.from({length: Math.min(concurrency, plan.chunks.length)}, worker));
  if (failed) throw failed;
  const text = texts.join('');
  const digest = gitBlobDigest(text, entry.bytes);
  if (digest.bytes !== entry.bytes || digest.chars !== entry.chars || digest.sha !== entry.sha) throw new Error('Received file bridge SHA/size mismatch for ' + entry.path);
  return {text, ...digest, stats};
}

// Stable research-records/v1 wire identity, not a second catalogue validator.
// Full compilation remains in research_submission.py and trusted-main Actions.
const researchWireCode = String.raw`import base64,copy,hashlib,json,re

def unique(items):
 out={}
 for k,v in items:
  assert k not in out, 'Duplicate research JSON key'
  out[k]=v
 return out

def load(raw):
 assert len(raw)<=1024*1024, 'Research wire input exceeds 1 MiB'
 return json.loads(raw,object_pairs_hook=unique)

def identify(raw):
 doc=load(raw)
 assert isinstance(doc,dict) and doc.get('format')=='research-records/v1', 'Not a compact research record'
 event=doc.get('event_id')
 assert isinstance(event,str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,127}',event), 'Unsafe research event ID'
 payload=copy.deepcopy(doc); review=payload.pop('review',{})
 proofs=payload.get('proofs',{})
 assert isinstance(proofs,dict), 'Invalid research proofs'
 locations={}
 for proof_id,proof in proofs.items():
  assert isinstance(proof_id,str) and proof_id.strip(), 'Invalid research proof ID'
  assert isinstance(proof,dict) and not set(proof)-{'repository','commit','path','blob','text'}, 'Invalid research proof fields'
  repository=proof.get('repository'); commit=proof.get('commit'); blob=proof.get('blob'); path=proof.get('path')
  assert isinstance(repository,str) and re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?',repository), 'Invalid research proof repository'
  assert all(isinstance(v,str) and re.fullmatch(r'[0-9a-fA-F]{40}',v) for v in (commit,blob)), 'Invalid research proof SHA'
  assert isinstance(path,str) and path.strip() and not any(p in {'','.','..'} for p in path.split('/')) and chr(92) not in path and not any(ord(c)<32 for c in path), 'Invalid research proof path'
  location=(repository.rstrip('/').casefold(),commit.lower(),path)
  assert location not in locations or locations[location]==blob.lower(), 'Conflicting research proof blobs'
  locations[location]=blob.lower()
  if 'text' in proof:
   assert isinstance(proof['text'],str), 'Research proof text must be a string'
   text=proof.pop('text').encode('utf-8')
   assert hashlib.sha1(b'blob '+str(len(text)).encode()+bytes([0])+text).hexdigest()==blob.lower(), 'Research proof bytes changed'
 digest=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
 assert review.get('status')=='ready' and review.get('digest')==digest, 'Invalid ready research seal'
 return {'event_id':event,'digest':digest}
`;

function compactSubmission(manifest, branch) {
  const marker=manifest.submission, entry=manifest.files?.[0];
  if(branch!=='main' || !marker || marker.version!==1 || typeof marker.event_id!=='string' || typeof marker.digest!=='string' || !/^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$/.test(marker.event_id)
    || marker.event_id!==manifest.event_id || !/^[0-9a-f]{64}$/.test(marker.digest)
    || !Array.isArray(manifest.files) || manifest.files.length!==1 || !entry || entry.path!==`submissions/research/${marker.event_id}.json`
    || !/^[0-9a-f]{40}$/.test(entry.sha) || !/^[0-9a-f]{64}$/.test(entry.sha256)
    || !Number.isSafeInteger(entry.bytes) || entry.bytes<1 || entry.bytes>1024*1024
    || !/^[0-9a-f]{40}$/.test(manifest.baseline_commit)
    || !Array.isArray(manifest.baseline_files) || manifest.baseline_files.length>1
    || manifest.baseline_files.some(e=>e.path!==entry.path || !/^[0-9a-f]{40}$/.test(e.sha))) {
    throw new Error('Automatic parent refresh requires exactly one bounded compact research submission on main');
  }
  return {marker,entry};
}

async function uploadPublicationBlob(tools,{repository,bundle,entry,plan}) {
  const loaded=await loadDiscoveryFile(tools,{bundle,entry,plan});
  const request={repository_full_name:repository,encoding:'utf-8',content:loaded.text};
  const size=publicationUTF8(JSON.stringify(request)).bytes;
  if(size>4*1024*1024 || (entry.request_bytes!==undefined && size!==entry.request_bytes)) throw new Error('Escaped connector request exceeds bound or manifest size: '+entry.path);
  const blob=publicationResult(await tools.mcp__codex_apps__github_create_blob(request));
  if(blob.sha!==entry.sha) throw new Error('Uploaded blob SHA mismatch for '+entry.path);
  return blob.sha;
}

async function publishCompactSubmission(tools,{repository,branch,bundle,message,manifest,state,plans,fetch,checkpoint,repoURL,refURL}) {
  const {marker,entry}=compactSubmission(manifest,branch);
  const local=await publicationCommand(tools,researchWireCode+'\nfrom pathlib import Path\nraw=(Path('+JSON.stringify(bundle)+')/'+JSON.stringify('payload/'+entry.path)+').read_bytes()\nprint(json.dumps(identify(raw)))');
  if(local.event_id!==marker.event_id || local.digest!==marker.digest) throw new Error('Compact research identity differs from manifest');
  async function remoteIdentity(sha,receipt=false) {
    const response=await tools.mcp__codex_apps__github_fetch({url:repoURL+'/git/blobs/'+sha});
    if(!response || response.isError) publicationResult(response);
    const value=response.structuredContent;
    let blob=value, text=null;
    if(typeof value?.content==='string' && value.encoding!=='base64') {
      const parsed=JSON.parse(value.content);
      if(parsed?.encoding==='base64') blob=parsed;
      else text=value.content; // Connector blob reads expose exact UTF-8 text.
    }
    let raw;
    if(text!==null) {
      if(publicationUTF8(text).bytes>1024*1024) throw new Error('Oversized remote research blob');
      raw='raw='+JSON.stringify(text)+'.encode("utf-8")';
    } else {
      if(blob?.encoding!=='base64' || typeof blob.content!=='string' || blob.size>1024*1024) throw new Error('Invalid or oversized remote research blob');
      raw='raw=base64.b64decode('+JSON.stringify(blob.content)+')';
    }
    // Keep remote validation portable too: large existing inputs must not be
    // embedded in a shell argument above the bridge's serialized-byte ceiling.
    const limit=PUBLICATION_OUTPUT_BYTES-8192;
    if(publicationUTF8(raw).bytes>limit) {
      const source=text!==null?text:blob.content, file=bundle+'/remote-'+sha+'.wire';
      for(let offset=0;offset<source.length;) {
        let low=1,high=Math.min(source.length-offset,limit);
        while(low<high) {
          const mid=Math.ceil((low+high)/2);
          if(publicationUTF8(JSON.stringify(source.slice(offset,offset+mid))).bytes<=limit) low=mid;else high=mid-1;
        }
        if(offset+low<source.length && /[\uD800-\uDBFF]/.test(source[offset+low-1])) low--;
        if(low<1) throw new Error('Cannot transfer remote research code point within bound');
        await publicationCommand(tools,'from pathlib import Path\nwith Path('+JSON.stringify(file)+').open('+JSON.stringify(offset===0?'wb':'ab')+') as f: f.write('+JSON.stringify(source.slice(offset,offset+low))+'.encode("utf-8"))\nprint("true")');
        offset+=low;
      }
      raw='from pathlib import Path\nraw=Path('+JSON.stringify(file)+').read_bytes()';
      if(text===null) raw+='\nraw=base64.b64decode(raw)';
    }
    const result=receipt ? "doc=load(raw)\nassert doc.get('version')==1 and isinstance(doc.get('event_id'),str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,127}',doc['event_id']) and re.fullmatch(r'[0-9a-f]{64}',doc.get('digest','')) and re.fullmatch(r'[0-9a-f]{40}',doc.get('input_blob','')), 'Invalid research receipt'\nresult={k:doc[k] for k in ('event_id','digest','input_blob')}" : 'result=identify(raw)';
    return publicationCommand(tools,researchWireCode+'\n'+raw+'\nassert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()=='+JSON.stringify(sha)+', "Remote research blob SHA mismatch"\n'+result+'\nprint(json.dumps(result))');
  }
  async function inspect(head) {
    const commit=await fetch(repoURL+'/git/commits/'+head);
    const tree=await fetch(repoURL+'/git/trees/'+commit.tree.sha+'?recursive=1');
    if(tree.truncated) throw new Error('Cannot verify truncated compact-submission tree');
    const blobs=new Map(tree.tree.filter(e=>e.type==='blob').map(e=>[e.path,e.sha]));
    const present=blobs.get(entry.path), receipt=blobs.get(`state/research-receipts/${marker.event_id}.json`);
    let submitted=present;
    if(present && present!==entry.sha) {
      const remote=await remoteIdentity(present);
      if(remote.event_id!==marker.event_id || remote.digest!==marker.digest) throw new Error('Research event ID conflicts with current main: '+marker.event_id);
    }
    if(receipt) {
      const remote=await remoteIdentity(receipt,true);
      if(remote.event_id!==marker.event_id || remote.digest!==marker.digest) throw new Error('Research event ID conflicts with published receipt: '+marker.event_id);
      submitted ||= remote.input_blob;
    }
    return {base_tree:commit.tree.sha,submitted};
  }
  async function finish(head,snapshot,already) {
    state.commit=head;
    state.submission_blob=snapshot.submitted;
    state.already_submitted=already;
    state.authored_files_verified=true;
    state.ref_verified=true;
    await checkpoint();
    return state;
  }
  let head=(await fetch(refURL)).object.sha;
  for(let attempt=0;attempt<3;attempt++) {
    const snapshot=await inspect(head);
    if(snapshot.submitted) return finish(head,snapshot,true);
    if(state.blobs[entry.path]!==entry.sha) {
      state.blobs[entry.path]=await uploadPublicationBlob(tools,{repository,bundle,entry,plan:plans[0]});
      await checkpoint();
    }
    if(state.submission_attempt?.parent!==head) {
      state.submission_attempt={parent:head};
      await checkpoint();
    }
    const pending=state.submission_attempt;
    if(!pending.tree) {
      pending.tree=publicationResult(await tools.mcp__codex_apps__github_create_tree({repository_full_name:repository,base_tree_sha:snapshot.base_tree,
        tree_elements:[{path:entry.path,mode:'100644',type:'blob',sha:entry.sha}]})).sha;
      await checkpoint();
    }
    if(!pending.commit) {
      pending.commit=publicationResult(await tools.mcp__codex_apps__github_create_commit({repository_full_name:repository,tree_sha:pending.tree,parent_sha:head,message})).sha;
      await checkpoint();
    }
    try {
      publicationResult(await tools.mcp__codex_apps__github_update_ref({repository_full_name:repository,branch_name:branch,sha:pending.commit,expected_sha:head,force:false}));
    } catch(error) {
      // Denials are never retried. A failed/uncertain CAS must be resolved by a
      // fresh remote read before refreshing a parent or making another write.
      if(/unacceptable risk|authorization|unauthorized|forbidden|approval|permission|denied|not accessible|not authorized|\b401\b|\b403\b/i.test(String(error))) throw error;
      const observed=(await fetch(refURL)).object.sha;
      const verified=await inspect(observed);
      if(verified.submitted) return finish(observed,verified,false);
      if(observed===head) throw error; // Outcome unresolved; resume the same checkpoint later.
      head=observed;
      continue;
    }
    const observed=(await fetch(refURL)).object.sha;
    const verified=await inspect(observed);
    if(verified.submitted) return finish(observed,verified,false);
    if(observed===head) throw new Error('Compact ref update was not visible; resume its checkpoint');
    head=observed;
  }
  throw new Error('Compact submission exhausted three fast-forward races; resume the unchanged bundle');
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
  const command = code => publicationCommand(tools, code);
  async function fetch(url) { return publicationResult(await tools.mcp__codex_apps__github_fetch({url})); }
  const local = await command('import json,sys\nfrom pathlib import Path\np=Path(' + JSON.stringify(bundle) + ')\n' +
    'print(json.dumps({"manifest":json.loads((p/"manifest.json").read_text()),"state":json.loads((p/"publication-state.json").read_text()) if (p/"publication-state.json").exists() else {}}))');
  const manifest = local.manifest;
  const state = local.state;
  const identity = {repository, branch, baseline: manifest.baseline_commit, input_digest: manifest.input_digest, files: manifest.files, baseline_files: manifest.baseline_files};
  if (manifest.submission !== undefined) identity.submission = manifest.submission;
  if (state.identity && JSON.stringify(state.identity) !== JSON.stringify(identity)) throw new Error('Publication checkpoint belongs to another bundle/ref');
  state.identity = identity;
  state.blobs ||= {};
  async function verifyRemote() {
    const tree = await fetch(repoURL + '/git/trees/' + state.commit + '?recursive=1');
    if (tree.truncated) throw new Error('Cannot verify truncated remote tree');
    const entries = new Map(tree.tree.filter(e => e.type === 'blob').map(e => [e.path, e.sha]));
    for (const entry of manifest.files) if ((entries.get(entry.path) ?? null) !== entry.sha) throw new Error('Remote payload mismatch: ' + entry.path);
    state.authored_files_verified = true;
  }
  async function checkpoint() {
    await command('import json,os\nfrom pathlib import Path\np=Path(' + JSON.stringify(bundle) + ')/"publication-state.json"\n' +
      's=' + JSON.stringify(JSON.stringify(state)) + '\nt=p.with_suffix(".tmp")\nt.write_text(s+"\\n")\nos.replace(t,p)\nprint("true")');
  }
  // Verify all bytes before starting writes. Never trust an old checkpoint over
  // a newly modified payload or silently reuse a different manifest.
  const plans = await planDiscoveryPayload(tools, {bundle, manifest});
  if (manifest.submission !== undefined) return publishCompactSubmission(tools,{repository,branch,bundle,message,manifest,state,plans,fetch,checkpoint,repoURL,refURL});
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
    if (entry.sha === null && !inputs.has(entry.path)) throw new Error('Deletion needs verified baseline: ' + entry.path);
    if (baselineBlobs.has(entry.path) && !inputs.has(entry.path)) throw new Error('New publication path already exists: ' + entry.path);
  }
  const started = Date.now();
  for (const entry of manifest.files) {
    if (entry.sha === null || baselineBlobs.get(entry.path) === entry.sha || state.blobs[entry.path] === entry.sha) continue;
    state.blobs[entry.path] = await uploadPublicationBlob(tools,{repository,bundle,entry,plan:plans.find(plan=>plan.path===entry.path)});
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

if (typeof module !== 'undefined') module.exports = {publishDiscovery, publicationResult, planDiscoveryPayload, loadDiscoveryFile, gitBlobDigest};
