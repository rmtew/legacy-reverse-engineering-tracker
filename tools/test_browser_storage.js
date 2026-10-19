const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const crypto=require('node:crypto');
const root=path.resolve(__dirname,'..');
const source=fs.readFileSync(path.join(root,'web/tracker.js'),'utf8');
const loader=source.slice(source.indexOf('async function loadProjectCatalogue('),source.indexOf('\nloadProjectCatalogue()'));
function setup(edit=()=>{}){
  const requests=[];
  const context=vm.createContext({crypto:crypto.webcrypto,TextDecoder,Uint8Array,Map,Set,Promise});
  vm.runInContext(loader,context);
  const fetcher=async url=>{
    requests.push(url);
    const file=path.join(root,url);
    if(!fs.existsSync(file))return {ok:false,status:404};
    let bytes=fs.readFileSync(file);
    return {ok:true,json:async()=>{const index=JSON.parse(bytes);edit(index);return index;},arrayBuffer:async()=>bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength)};
  };
  return {load:()=>context.loadProjectCatalogue(fetcher),requests};
}
test('browser reconstructs exact catalogue in index order and reads only project shards',async()=>{
  const x=setup(),records=await x.load();
  const index=JSON.parse(fs.readFileSync(path.join(root,'data/projects.index.json')));
  assert.deepEqual(Array.from(records,p=>p.id),index.order);
  assert.equal(x.requests.length,index.shards.length+1);
  assert.ok(x.requests.every(p=>p==='data/projects.index.json'||/^data\/projects\/[0-9a-f]+\.json$/.test(p)));
  assert.match(source,/fetch\("data\/activity-30d.json"/);
  assert.doesNotMatch(source,/activity-180d|loadFullActivity/);
});
test('browser rejects unsafe, missing, corrupt and duplicate shard references',async()=>{
  await assert.rejects(setup(i=>i.shards[0].path='../secret').load(),/Invalid project shard/);
  await assert.rejects(setup(i=>{i.shards=i.shards.slice(0,1);i.shards[0].path='projects/'+ 'f'.repeat(64)+'.json';}).load(),/HTTP 404/);
  await assert.rejects(setup(i=>i.shards[0].sha256='0'.repeat(64)).load(),/digest/);
  await assert.rejects(setup(i=>i.shards.push(i.shards[0])).load(),/Invalid project shard/);
  await assert.rejects(setup(i=>i.order.push('missing')).load(),/coverage/);
});
