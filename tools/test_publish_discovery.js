const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const crypto = require('node:crypto');
const {execSync} = require('node:child_process');
const {publishDiscovery} = require('./publish_discovery.js');

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
      assert.ok(Buffer.byteLength(output) < 40000, 'Bounded serialized transfer output');
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
  return {bundle, tools, remote, options: {repository: 'owner/tracker', branch: 'reviewed/batch', bundle, message: 'Publish reviewed research'}};
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
