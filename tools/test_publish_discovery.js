const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const crypto = require('node:crypto');
const {execSync} = require('node:child_process');
const vm = require('node:vm');
const {publishDiscovery, planDiscoveryPayload, loadDiscoveryFile, gitBlobDigest} = require('./publish_discovery.js');

function setup(t, text = 'Evidence unchanged. 🦊\n') {
  const bundle = fs.mkdtempSync(path.join(os.tmpdir(), 'publish-discovery-test-'));
  t.after(() => fs.rmSync(bundle, {recursive: true, force: true}));
  fs.mkdirSync(path.join(bundle, 'payload'));
  const content = Buffer.from(text);
  const sha = crypto.createHash('sha1').update(Buffer.from(`blob ${content.length}\0`)).update(content).digest('hex');
  const manifest = {baseline_commit: 'a'.repeat(40), baseline_files: [{path: 'sources.md', sha: 'f'.repeat(40)}], input_digest: 'b'.repeat(64), files: [{path: 'report.md', bytes: content.length,
    chars: Array.from(text).length, sha, sha256: crypto.createHash('sha256').update(content).digest('hex')}]};
  fs.writeFileSync(path.join(bundle, 'payload/report.md'), text);
  fs.writeFileSync(path.join(bundle, 'manifest.json'), JSON.stringify(manifest));
  const remote = {head: manifest.baseline_commit, blobs: 0, commits: 0, refs: 0, loseResponse: false};
  const result = value => ({structuredContent: value});
  const tools = {
    exec_command: async ({cmd}) => {
      const output = execSync(cmd, {encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe']});
      assert.ok(Buffer.byteLength(output) <= 120000, 'Bounded serialized transfer output');
      return {output, exit_code: 0};
    },
    mcp__codex_apps__github_fetch: async ({url}) => {
      if (url.includes('/git/ref/')) {
        assert.ok(!url.includes('%2F'), 'Connector ref paths preserve branch separators');
        return result({object: {sha: remote.head}});
      }
      if (url.includes('/git/commits/')) return result({tree: {sha: 'c'.repeat(40)}});
      if (url.includes('/git/trees/' + 'c'.repeat(40))) return result({tree: [{path: 'sources.md', type: 'blob', sha: remote.baselineSHA || 'f'.repeat(40)}]});
      if (url.includes('/git/trees/')) return result({tree: [{path: 'report.md', type: 'blob', sha}]});
      throw new Error(url);
    },
    mcp__codex_apps__github_create_blob: async args => {remote.blobs++; assert.equal(args.content, text); return result({sha});},
    mcp__codex_apps__github_create_tree: async args => {assert.equal(args.base_tree_sha, 'c'.repeat(40)); return result({sha: 'd'.repeat(40)});},
    mcp__codex_apps__github_create_commit: async args => {remote.commits++; assert.equal(args.parent_sha, manifest.baseline_commit); return result({sha: 'e'.repeat(40)});},
    mcp__codex_apps__github_update_ref: async args => {
      remote.refs++;
      assert.equal(args.expected_sha, remote.head);
      assert.equal(args.force, false);
      remote.head = args.sha;
      if (remote.loseResponse) throw new Error('Connection lost after update');
      return result({sha: args.sha});
    },
  };
  return {bundle, manifest, text, tools, remote, options: {repository: 'owner/tracker', branch: 'reviewed/batch', bundle, message: 'Publish reviewed research'}};
}

test('publishes with expected-SHA and verifies exact tree, then resumes without writes', async t => {
  const x = setup(t);
  const first = await publishDiscovery(x.tools, x.options);
  assert.equal(first.authored_files_verified, true);
  assert.equal(first.ref_verified, true);
  await publishDiscovery(x.tools, x.options);
  assert.equal(x.remote.blobs, 1);
  assert.equal(x.remote.commits, 1);
  assert.equal(x.remote.refs, 1);
});

test('advanced main fails before uploading', async t => {
  const x = setup(t);
  x.remote.head = 'f'.repeat(40);
  await assert.rejects(publishDiscovery(x.tools, x.options), /Branch advanced/);
  assert.equal(x.remote.blobs, 0);
});

test('large non-ASCII content uses bounded UTF-8 chunks without truncation', async t => {
  const x = setup(t, '漢🦊'.repeat(30000) + '\n');
  const result = await publishDiscovery(x.tools, x.options);
  assert.equal(result.authored_files_verified, true);
  assert.equal(x.remote.blobs, 1);
});

test('a stale input tree cannot be relabeled with the current commit SHA', async t => {
  const x = setup(t);
  x.remote.baselineSHA = '1'.repeat(40);
  await assert.rejects(publishDiscovery(x.tools, x.options), /Baseline input differs/);
  assert.equal(x.remote.blobs, 0);
  assert.equal(x.remote.refs, 0);
});

test('uncertain ref response is resolved by read, never a blind repeated mutation', async t => {
  const x = setup(t);
  x.remote.loseResponse = true;
  await assert.rejects(publishDiscovery(x.tools, x.options), /Connection lost/);
  const recovered = await publishDiscovery(x.tools, x.options);
  assert.equal(recovered.authored_files_verified, true);
  assert.equal(x.remote.refs, 1);
  assert.equal(x.remote.commits, 1);
});

test('changed payload cannot reuse saved checkpoint or publish', async t => {
  const x = setup(t);
  fs.appendFileSync(path.join(x.bundle, 'payload/report.md'), 'Changed');
  await assert.rejects(publishDiscovery(x.tools, x.options));
  assert.equal(x.remote.blobs, 0);
});

test('failed upload can resume verified blobs but a mismatched SHA never moves ref', async t => {
  const x = setup(t);
  x.tools.mcp__codex_apps__github_create_blob = async () => ({structuredContent: {sha: '0'.repeat(40)}});
  await assert.rejects(publishDiscovery(x.tools, x.options), /SHA mismatch/);
  assert.equal(x.remote.refs, 0);
});

async function planned(x, options = {}) {
  const plans = await planDiscoveryPayload(x.tools, {bundle: x.bundle, manifest: x.manifest, ...options});
  return {bundle: x.bundle, entry: x.manifest.files[0], plan: plans[0], ...options};
}

function isRead(args) { return args.cmd.includes('# publication-bridge-read'); }

function referenceDigest(text) {
  const content = Buffer.from(text);
  return crypto.createHash('sha1').update(Buffer.from(`blob ${content.length}\0`)).update(content).digest('hex');
}

test('portable Git SHA-1 matches Node across padding boundaries and Unicode', () => {
  const examples = ['', 'hello\n', '\ufeffA\r\n漢🦊\u0000\b\t\\"\r\n', 'a'.repeat(1000000)];
  for (let i = 0; i < 140; i++) examples.push('x'.repeat(i), '漢🦊'.repeat(i));
  for (const text of examples) {
    const actual = gitBlobDigest(text, Buffer.byteLength(text));
    assert.equal(actual.sha, referenceDigest(text));
    assert.equal(actual.bytes, Buffer.byteLength(text));
    assert.equal(actual.chars, Array.from(text).length);
  }
  assert.throws(() => gitBlobDigest('\ud800', 3), /Unicode surrogate/);
  assert.throws(() => gitBlobDigest('\udc00', 3), /Unicode surrogate/);
});

test('driver and exact received hash work without Node or Web encoding/crypto globals', async t => {
  const source = fs.readFileSync(path.join(__dirname, 'publish_discovery.js'), 'utf8');
  const context = vm.createContext({});
  vm.runInContext(source, context);
  for (const name of ['require', 'crypto', 'TextEncoder', 'TextDecoder', 'atob', 'Buffer']) assert.equal(vm.runInContext('typeof ' + name, context), 'undefined');
  const x = setup(t, '\ufeff漢🦊\r\n"\\\u0000'.repeat(12000));
  const plans = await context.planDiscoveryPayload(x.tools, {bundle: x.bundle, manifest: x.manifest});
  const result = await context.loadDiscoveryFile(x.tools, {bundle: x.bundle, entry: x.manifest.files[0], plan: plans[0]});
  assert.equal(result.text, x.text);
  assert.equal(result.sha, referenceDigest(x.text));
});

test('bounded large chunks preserve CRLF, BOM, controls and JSON escaping exactly', async t => {
  const x = setup(t, '\ufeff' + '漢🦊\r\n\u0000\b\t\\"\r'.repeat(30000));
  let maximum = 0;
  const exec = x.tools.exec_command;
  x.tools.exec_command = async args => {
    const result = await exec(args);
    if (isRead(args)) {
      maximum = Math.max(maximum, Buffer.byteLength(result.output));
      assert.match(args.cmd, /f\.seek\(offset\)/);
      assert.match(args.cmd, /f\.read\(size\)/);
      assert.doesNotMatch(args.cmd, /read_text|read_bytes/);
    }
    return result;
  };
  const options = await planned(x);
  const loaded = await loadDiscoveryFile(x.tools, options);
  assert.equal(loaded.text, x.text);
  assert.ok(maximum > 115000, 'Use nearly the full 120 KB output budget, rather than repeatedly halving dense JSON');
  assert.ok(maximum <= 120000);
  assert.equal(loaded.stats.read_calls, options.plan.chunks.length);
  assert.equal(loaded.stats.truncation_retries, 0);
});

test('four concurrent reads assemble correctly despite out-of-order completion', async t => {
  const x = setup(t, Array.from({length: 16}, (_, i) => String.fromCharCode(65 + i).repeat(18000)).join(''));
  const options = await planned(x, {outputBytes: 16000});
  const exec = x.tools.exec_command;
  let active = 0, maximum = 0, started = 0;
  const completed = [];
  x.tools.exec_command = async args => {
    if (!isRead(args)) return exec(args);
    const index = started++;
    active++;
    maximum = Math.max(maximum, active);
    const result = await exec(args);
    await new Promise(resolve => setTimeout(resolve, index === 0 ? 120 : 1));
    completed.push(index);
    active--;
    return result;
  };
  const loaded = await loadDiscoveryFile(x.tools, options);
  assert.equal(loaded.text, x.text);
  assert.equal(maximum, 4);
  assert.equal(loaded.stats.max_concurrent_reads, 4);
  assert.notEqual(completed[0], 0);
});

test('explicit truncation shrinks and retries only the affected byte ranges', async t => {
  const x = setup(t, '\ufeff' + '漢🦊\r\n\u0000\\"'.repeat(15000));
  const options = await planned(x);
  const exec = x.tools.exec_command;
  let truncations = 0;
  x.tools.exec_command = async args => {
    const result = await exec(args);
    if (isRead(args) && Buffer.byteLength(result.output) > 32000) {
      truncations++;
      return {...result, original_token_count: 45001, output: 'Warning: truncated output (original token count: 45001)\n' + result.output.slice(0, 1000)};
    }
    return result;
  };
  const loaded = await loadDiscoveryFile(x.tools, options);
  assert.equal(loaded.text, x.text);
  assert.ok(truncations > 0);
  assert.equal(loaded.stats.truncation_retries, truncations);
  assert.equal(loaded.stats.output_byte_limit, 30000);
});

test('truncation token metadata alone permits a bounded retry', async t => {
  const x = setup(t, '0123456789'.repeat(12000));
  const options = await planned(x);
  const exec = x.tools.exec_command;
  let truncated = false;
  x.tools.exec_command = async args => {
    if (isRead(args) && !truncated) { truncated = true; return {exit_code: 0, original_token_count: 40001, output: '{'}; }
    return exec(args);
  };
  const loaded = await loadDiscoveryFile(x.tools, options);
  assert.equal(loaded.text, x.text);
  assert.equal(loaded.stats.truncation_retries, 1);
});

test('persistent explicit truncation stops at minimum output size', async t => {
  const x = setup(t, 'A'.repeat(20000));
  const options = await planned(x, {concurrency: 1, outputBytes: 2048});
  let calls = 0;
  x.tools.exec_command = async () => { calls++; return {exit_code: 0, output: 'Warning: truncated output'}; };
  await assert.rejects(loadDiscoveryFile(x.tools, options), /Truncated file bridge output/);
  assert.equal(calls, 2);
});

for (const [name, response, pattern] of [
  ['malformed JSON', {exit_code: 0, output: '{'}, /JSON|Unexpected/],
  ['command failure', {exit_code: 1, output: 'Denied'}, /command failed/],
  ['unfinished command', {exit_code: 0, session_id: 99, output: '{}'}, /command failed/],
  ['structured authorization failure', {isError: true, exit_code: 0, output: 'Warning: truncated output'}, /command failed/],
]) test(name + ' stops without a smaller-read retry', async t => {
  const x = setup(t, 'A'.repeat(20000));
  const options = await planned(x, {concurrency: 1});
  let calls = 0;
  x.tools.exec_command = async () => { calls++; return response; };
  await assert.rejects(loadDiscoveryFile(x.tools, options), pattern);
  assert.equal(calls, 1);
});

test('rejected authorization drains in-flight reads and starts no further reads', async t => {
  const x = setup(t, 'A'.repeat(200000));
  const options = await planned(x, {outputBytes: 4000});
  const exec = x.tools.exec_command;
  let calls = 0, completed = 0;
  x.tools.exec_command = async args => {
    const n = calls++;
    if (n === 0) throw new Error('Authorization denied');
    await new Promise(resolve => setTimeout(resolve, 10));
    const result = await exec(args);
    completed++;
    return result;
  };
  await assert.rejects(loadDiscoveryFile(x.tools, options), /Authorization denied/);
  assert.equal(calls, 4);
  assert.equal(completed, 3);
});

for (const field of ['offset', 'bytes', 'chars', 'text']) test('corrupted received ' + field + ' blocks upload', async t => {
  const x = setup(t, 'A'.repeat(30000));
  const exec = x.tools.exec_command;
  x.tools.exec_command = async args => {
    const result = await exec(args);
    if (isRead(args)) {
      const part = JSON.parse(result.output);
      if (field === 'text') part.text = 'B' + part.text.slice(1);
      else part[field]++;
      result.output = JSON.stringify(part);
    }
    return result;
  };
  await assert.rejects(publishDiscovery(x.tools, x.options), /bridge/);
  assert.equal(x.remote.blobs, 0);
  assert.equal(x.remote.refs, 0);
});

test('same-length source modification after planning fails the received hash', async t => {
  const x = setup(t, 'A'.repeat(30000));
  const options = await planned(x);
  fs.writeFileSync(path.join(x.bundle, 'payload/report.md'), 'B'.repeat(30000));
  await assert.rejects(loadDiscoveryFile(x.tools, options), /SHA\/size mismatch/);
});

test('reordered or incomplete plans fail before reading', async t => {
  const x = setup(t, 'A'.repeat(20000));
  const options = await planned(x, {outputBytes: 4000});
  let reads = 0;
  x.tools.exec_command = async () => { reads++; throw new Error('Should not read'); };
  const reordered = {...options, plan: {...options.plan, chunks: [...options.plan.chunks].reverse()}};
  await assert.rejects(loadDiscoveryFile(x.tools, reordered), /plan order/);
  const incomplete = {...options, plan: {...options.plan, chunks: options.plan.chunks.slice(0, -1)}};
  await assert.rejects(loadDiscoveryFile(x.tools, incomplete), /plan size mismatch/);
  assert.equal(reads, 0);
});

test('empty file has exact Git identity and makes no chunk reads', async t => {
  const x = setup(t, '');
  const loaded = await loadDiscoveryFile(x.tools, await planned(x));
  assert.equal(loaded.sha, 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391');
  assert.equal(loaded.text, '');
  assert.equal(loaded.stats.read_calls, 0);
  const result = await publishDiscovery(x.tools, x.options);
  assert.equal(result.authored_files_verified, true);
});

test('source SHA-256 mismatch fails before any upload', async t => {
  const x = setup(t);
  x.manifest.files[0].sha256 = '0'.repeat(64);
  fs.writeFileSync(path.join(x.bundle, 'manifest.json'), JSON.stringify(x.manifest));
  await assert.rejects(publishDiscovery(x.tools, x.options), /assert|AssertionError|Command failed/i);
  assert.equal(x.remote.blobs, 0);
});

test('multiple blob mutations remain sequential and checkpointed', async t => {
  const x = setup(t, 'A'.repeat(140000));
  const second = '漢🦊\r\n'.repeat(25000);
  const entry = {path: 'second.md', bytes: Buffer.byteLength(second), chars: Array.from(second).length,
    sha: referenceDigest(second), sha256: crypto.createHash('sha256').update(second).digest('hex')};
  x.manifest.files.push(entry);
  fs.writeFileSync(path.join(x.bundle, 'payload/second.md'), second);
  fs.writeFileSync(path.join(x.bundle, 'manifest.json'), JSON.stringify(x.manifest));
  const events = [];
  const exec = x.tools.exec_command, fetch = x.tools.mcp__codex_apps__github_fetch;
  x.tools.exec_command = async args => {
    if (args.cmd.includes('os.replace')) events.push('checkpoint');
    return exec(args);
  };
  x.tools.mcp__codex_apps__github_fetch = async args => {
    if (args.url.includes('/git/trees/' + 'e'.repeat(40))) return {structuredContent: {tree: x.manifest.files.map(e => ({...e, type: 'blob'}))}};
    return fetch(args);
  };
  let active = 0;
  x.tools.mcp__codex_apps__github_create_blob = async args => {
    assert.equal(active++, 0);
    const name = args.content === x.text ? 'report.md' : 'second.md';
    assert.equal(args.content, name === 'report.md' ? x.text : second);
    events.push('blob:' + name);
    await new Promise(resolve => setTimeout(resolve, 5));
    active--;
    return {structuredContent: {sha: referenceDigest(args.content)}};
  };
  const result = await publishDiscovery(x.tools, x.options);
  assert.equal(result.ref_verified, true);
  assert.deepEqual(events.slice(0, 4), ['blob:report.md', 'checkpoint', 'blob:second.md', 'checkpoint']);
});

for (const [name, fail, pattern] of [
  ['thrown denial', () => { throw new Error('Authorization denied'); }, /Authorization denied/],
  ['exit-code failure', () => ({exit_code: 1, output: 'Denied'}), /command failed/],
  ['malformed JSON', () => ({exit_code: 0, output: '{'}), /JSON|Unexpected/],
  ['corrupt read validation', part => ({exit_code: 0, output: JSON.stringify({...part, offset: 1})}), /reordered/],
]) test('immediately resolved siblings stop at four reads after ' + name, async () => {
  const text = 'A'.repeat(12000);
  const entry = {path: 'report.md', bytes: text.length, chars: text.length, sha: referenceDigest(text)};
  const plan = {path: entry.path, chunks: Array.from({length: 12}, (_, i) => ({offset: i * 1000, bytes: 1000, chars: 1000}))};
  let calls = 0;
  const tools = {exec_command: async ({cmd}) => {
    calls++;
    const offset = Number(cmd.match(/^offset=(\d+)$/m)[1]);
    const part = {offset, bytes: 1000, chars: 1000, text: 'A'.repeat(1000)};
    // No delay or nested await: all four results settle in the same microtask turn.
    if (offset === 0) return fail(part);
    return {exit_code: 0, output: JSON.stringify(part)};
  }};
  await assert.rejects(loadDiscoveryFile(tools, {bundle: '/unused', entry, plan}), pattern);
  assert.equal(calls, 4, 'No read beyond the initial four may start once a worker detects failure');
});
