"use strict";
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const {test}=require('node:test');
const root=path.resolve(__dirname,'..');
function setup(extra={}){
  const elements=new Map(),timers=[];
  function node(){return {value:'',checked:false,dataset:{},listeners:{},children:[],html:'',
    classList:{contains:()=>false,toggle:()=>{}},setAttribute(){},removeAttribute(){},close(){},
    addEventListener(name,callback){(this.listeners[name]??=[]).push(callback);},
    set innerHTML(value){this.html=value;this.children=[];},get innerHTML(){return this.html;},
    insertAdjacentHTML(_,value){this.html+=value;for(const match of value.matchAll(/<tr class="project-row [^"]*" data-id="([^"]*)"/g)){const row={dataset:{id:match[1]},remove:()=>{this.children.splice(this.children.indexOf(row),1);}};this.children.push(row);}},
    querySelectorAll(){return this.children;}};}
  const get=id=>{if(!elements.has(id))elements.set(id,node());return elements.get(id);};
  const context=vm.createContext({document:{documentElement:{dataset:{}},getElementById:get,querySelector:()=>node(),querySelectorAll:()=>[]},window:{matchMedia:()=>({matches:false,addEventListener(){}})},fetch:()=>new Promise(()=>{}),localStorage:{getItem(){return null;},setItem(){}},console,setTimeout:fn=>timers.push(fn),clearTimeout(){},...extra});
  vm.runInContext(fs.readFileSync(path.join(root,'web/reading-state.js'),'utf8'),context);
  vm.runInContext(fs.readFileSync(path.join(root,'web/tracker.js'),'utf8'),context);
  const run=code=>vm.runInContext(code,context);
  const records=Array.from({length:251},(_,i)=>({id:'p'+i,title:'Project '+i,source_platforms:['Amiga'],notes:i===250?'needle outside first batch':''}));
  context.records=records;run('projects=records;render()');
  return {get,run,context,timers,records};
}
test('full-catalogue search and counts with bounded initial DOM and append-only more',()=>{
  const x=setup();assert.equal(x.get('rows').children.length,100);assert.equal(x.get('count').textContent,251);
  const first=x.get('rows').children[0];x.get('projectShowMore').listeners.click[0]();
  assert.equal(x.get('rows').children.length,200);assert.equal(x.get('rows').children[0],first);
  x.get('q').value='needle outside';x.run('render()');
  assert.equal(x.get('count').textContent,1);assert.equal(x.get('rows').children[0].dataset.id,'p250');
  x.get('q').value='missing';x.run('render()');assert.equal(x.get('count').textContent,0);assert.match(x.get('rows').innerHTML,/No projects/);
});
test('metadata and sorted order reused across queries, replaced on snapshot update',()=>{
  const x=setup();x.run('globalThis.savedOrder=sortedProjects();globalThis.savedMeta=projectMeta(projects[0]);');
  x.get('q').value='project';x.run('render()');assert.equal(x.run('savedOrder===sortedProjects()&&savedMeta===projectMeta(projects[0])'),true);
  x.run('projects=projects.map(p=>({...p,title:p.id==="p0"?"ZZZ refreshed":p.title}));render()');
  assert.equal(x.run('savedOrder===sortedProjects()'),false);x.get('q').value='zzz refreshed';x.run('render()');assert.equal(x.get('count').textContent,1);
});
test('sorting is numeric and keeps unknown values last in both directions',()=>{
  const x=setup();x.run('projects=[{id:"a",title:"Project 10",last_activity:null},{id:"b",title:"Project 2",last_activity:"2026-10-02"},{id:"c",title:"Project 1",last_activity:"2026-10-01"}];render()');
  assert.deepEqual(x.get('rows').children.map(r=>r.dataset.id),['c','b','a']);
  for(const dir of [1,-1]){x.run(`sort={key:"updated",dir:${dir}};render()`);assert.equal(x.get('rows').children.at(-1).dataset.id,'a');}
});
test('show all is chunked, and new search cancels obsolete batches',()=>{
  const x=setup();x.get('projectShowAll').listeners.click[0]();assert.equal(x.get('rows').children.length,200);
  x.get('q').value='needle';x.run('render()');while(x.timers.length)x.timers.shift()();assert.equal(x.get('rows').children.length,1);
  x.get('q').value='';x.run('render()');x.get('projectShowAll').listeners.click[0]();while(x.timers.length)x.timers.shift()();assert.equal(x.get('rows').children.length,251);assert.equal(x.get('projectShowAll').hidden,true);
});
test('bookmark-filter removal preserves surviving row identity and accurate count',()=>{
  const x=setup();x.get('bookmarkedProjects').checked=true;x.run('bookmarks=new Set(projects.map(p=>p.id));render()');
  const survivor=x.get('rows').children[1];x.run('bookmarks.delete("p0");refreshProjectBookmarkMembership()');
  assert.equal(x.get('rows').children[0],survivor);assert.equal(x.get('rows').children.length,100);assert.equal(x.get('count').textContent,250);
});
test('deep position restoration exposes requested row and delegated click finds project',()=>{
  const x=setup();assert.equal(x.run('ensureProjectAnchorRendered("p250")'),false);assert.equal(x.get('rows').children.length,200);assert.equal(x.run('ensureProjectAnchorRendered("p250")'),true);assert.equal(x.get('rows').children.length,251);
  x.run('showDetails=record=>{globalThis.opened=record.id;}');
  const row={dataset:{id:'p250'}};const event={target:{closest:selector=>selector==='tr.project-row'?row:null}};
  x.get('rows').listeners.click.forEach(fn=>fn(event));assert.equal(x.run('opened'),'p250');
});

test('scroll observer appends a bounded batch and keeps existing nodes',()=>{
  const observers=[];
  class Observer{constructor(fn){this.callback=fn;observers.push(this);}observe(node){this.observed=node;}disconnect(){}}
  const x=setup({IntersectionObserver:Observer});const {callback}=observers.find(observer=>observer.observed===x.get('projectShowMore'));
  const first=x.get('rows').children[0];callback([{isIntersecting:false}]);assert.equal(x.get('rows').children.length,100);
  callback([{isIntersecting:true}]);assert.equal(x.get('rows').children.length,200);assert.equal(x.get('rows').children[0],first);
});
test('platform vocabulary changes invalidate normalized search metadata',()=>{
  const x=setup();x.records[0].source_platforms=['alias'];x.run('projects=projects.slice();render()');
  x.get('q').value='canonical platform';x.run('render()');assert.equal(x.get('count').textContent,0);
  x.run('platformVocabulary={aliases:{alias:"Canonical platform"},non_platform_values:[]};render()');assert.equal(x.get('count').textContent,1);
});
