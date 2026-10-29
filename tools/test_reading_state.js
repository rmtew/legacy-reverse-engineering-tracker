const test=require('node:test');
const assert=require('node:assert/strict');
const r=require('../web/reading-state.js');
const date='2026-10-29T00:00:00Z',now=Date.parse(date);
const commit=(sha,date='2026-10-28T00:00:00Z')=>({type:'commit',project_id:'p',sha,date});
test('first visit is unread; reload, late old commits and repeated snapshots never auto-acknowledge',()=>{
  let x=r.reconcile(r.empty(),[commit('a')],date,now);
  assert.equal(x.firstVisit,true);assert.equal(x.added,1);
  x=r.reconcile(r.parse(JSON.stringify(x.state)),[commit('a'),commit('late','2026-10-06T00:00:00Z')],date,now+1);
  assert.equal(x.added,1);assert.equal(Object.values(x.state.seen).filter(v=>v).length,2);
  x=r.reconcile(x.state,[commit('a'),commit('late','2026-10-06T00:00:00Z')],date,now+2);
  assert.equal(x.added,0);assert.equal(Object.values(x.state.seen).filter(v=>v).length,2);
});
test('compaction retains SHA identities and unread membership; late additions to a summary are new',()=>{
  let x=r.reconcile(r.empty(),[commit('a')],date,now).state;
  x=r.reconcile(x,[commit('a'),commit('b')],date,now+1).state;
  const summary={type:'daily_commits',project_id:'p',date,day:'2026-10-29',count:2,shas:['a','b']};
  let result=r.reconcile(x,[summary],date,now+2);
  assert.equal(result.added,0);assert.equal(result.expired,0);assert.equal(result.state.seen[r.ids(commit('b'))[0]],true);
  result=r.reconcile(result.state,[{...summary,count:3,shas:['a','b','late']}],date,now+3);assert.equal(result.added,1);
});
test('mark shown read acknowledges only captured identities, not concurrent new activity',()=>{
  let x=r.reconcile(r.empty(),[],date,now).state;
  x=r.reconcile(x,[commit('a')],date,now+1).state;
  const shown=r.ids(commit('a'));
  x=r.reconcile(x,[commit('a'),commit('b')],date,now+2).state;
  x=r.acknowledge(x,shown);
  assert.equal(x.seen[shown[0]],false);assert.equal(x.seen[r.ids(commit('b'))[0]],true);
});
test('retention and identity-less legacy summaries are honest and conservative',()=>{
  let x=r.reconcile(r.empty(),[],date,now).state;
  x=r.reconcile(x,[commit('a')],date,now+1).state;
  const expired=r.reconcile(x,[],'2026-12-01T00:00:00Z',now+33*86400000);
  assert.equal(expired.limited,true);assert.equal(expired.expired,1);assert.equal(Object.keys(expired.state.seen).length,0);
  assert.equal(r.reconcile(x,[{type:'daily_commits',project_id:'p',date,count:5}],date,now+2).added,1);
});
test('project changes have stable, compact identities independent of object key order',()=>{
  const a={type:'project_changed',project_id:'p',date,change_details:[{field:'notes',before:'x'.repeat(50000),after:'y'}]};
  const b={...a,change_details:[{after:'y',before:'x'.repeat(50000),field:'notes'}]};
  assert.deepEqual(r.ids(a),r.ids(b));assert.ok(r.ids(a)[0].length<200);
  assert.notDeepEqual(r.ids(a),r.ids({...a,change_details:[]}));
});
test('bookmark imports validate, deduplicate, and preserve IDs as plain text',()=>{
  assert.deepEqual(r.parseBookmarks('{"version":1,"project_ids":["p","p","<script>"]}'),['p','<script>']);
  for(const value of ['{','{}','{"version":2,"project_ids":[]}','{"version":1,"project_ids":[5]}'])assert.throws(()=>r.parseBookmarks(value));
  assert.throws(()=>r.parse('{'));assert.throws(()=>r.parse('{"version":1,"seen":[]}'));
});

const fs=require('node:fs'),vm=require('node:vm');
function browser(storage={},extras={}){
  const elements=new Map(),handlers=new Map();
  const node=id=>({value:'',dataset:{},checked:false,hidden:false,innerHTML:'',insertAdjacentHTML:function(_,html){this.innerHTML+=html;},textContent:'',classList:{contains:()=>id==='activityView',toggle:()=>{}},setAttribute:()=>{},addEventListener:(event,fn)=>handlers.set(id+':'+event,fn),querySelectorAll:()=>[],querySelector:()=>node('child'),close:()=>{}});
  const get=id=>{if(!elements.has(id))elements.set(id,node(id));return elements.get(id);};
  const context=vm.createContext({document:{documentElement:{dataset:{}},getElementById:get,querySelector:()=>node('q'),querySelectorAll:()=>[]},window:{matchMedia:()=>({matches:false,addEventListener:()=>{}}),addEventListener:()=>{},scrollTo:()=>{}},localStorage:{getItem:key=>storage[key]||null,setItem:(key,value)=>{storage[key]=value;}},fetch:()=>new Promise(()=>{}),console,Date,Set,Map,Promise,setTimeout:()=>{},clearTimeout:()=>{},TrackerReading:r,...extras});
  vm.runInContext(fs.readFileSync(require.resolve('../web/tracker.js'),'utf8'),context);
  const run=code=>vm.runInContext(code,context);
  run(`projects=[{id:'p',title:'Project'}];projectsReady=true;activityReady=true;activityUiReady=true;readingInitialized=true;bindActivityProjectFacets=()=>{};loadProjectCatalogue=async()=>projects;activityData={generated_at:'${date}',events:[]};readingState=reading.reconcile(reading.empty(),[],activityData.generated_at).state;saveReading();`);
  return {run,get,handlers,storage,context};
}
test('fetch succeeds, does not duplicate unread, fails without changing saved check, and repeated in-flight controls are safe',async()=>{
  const b=browser();
  b.run(`loadActivitySnapshot=async()=>({generated_at:'${date}',events:[${JSON.stringify(commit('late','2026-10-06T00:00:00Z'))}]});`);
  await b.run('fetchUpdates()');
  assert.equal(b.get('unreadCount').textContent,1);assert.equal(b.get('activityMore').hidden,true);
  const state=b.storage[r.KEY];await b.run('fetchUpdates()');assert.equal(b.get('unreadCount').textContent,1);
  b.run("loadActivitySnapshot=async()=>{throw Error('offline')}");const before=b.storage[r.KEY];await b.run('fetchUpdates()');
  assert.equal(b.storage[r.KEY],before);assert.match(b.get('readingStatus').textContent,/Fetch failed/);
  b.handlers.get('markRead:click')();assert.equal(b.get('unreadCount').textContent,0);
  b.run('fetchingUpdates=true');await b.run('fetchUpdates()');assert.equal(b.get('unreadCount').textContent,0);
  assert.ok(state);
});
test('malformed and quota-blocked storage warn without crashing or claiming persistence',()=>{
  const bad=browser({[r.KEY]:'{'});assert.equal(bad.get('storageWarning').hidden,false);
  const full=browser();full.run("localStorage.setItem=()=>{throw Error('quota')};saveReading()");
  assert.match(full.get('storageWarning').textContent,/tab only/);
});
test('bookmark controls toggle without navigation; import merges safely and rejects malformed input',async()=>{
  const b=browser();
  const button={dataset:{bookmark:'p'}};let prevented=false,stopped=false;
  b.context.click={target:{closest:()=>button},preventDefault:()=>{prevented=true},stopPropagation:()=>{stopped=true}};
  b.run('bookmarkClick(click)');assert.equal(prevented&&stopped,true);assert.deepEqual(r.parseBookmarks(b.storage[r.BOOKMARKS]),['p']);
  b.run('bookmarkClick(click)');assert.deepEqual(r.parseBookmarks(b.storage[r.BOOKMARKS]),[]);
  b.run('bookmarkClick(click)');
  await b.handlers.get('importBookmarks:change')({target:{files:[{size:60,text:async()=>'{"version":1,"project_ids":["q","p","q"]}'}]}});
  assert.deepEqual(r.parseBookmarks(b.storage[r.BOOKMARKS]),['p','q']);
  await b.handlers.get('importBookmarks:change')({target:{files:[{size:1,text:async()=>'{'}]}});
  assert.deepEqual(r.parseBookmarks(b.storage[r.BOOKMARKS]),['p','q']);assert.match(b.get('readingStatus').textContent,/Import failed/);
});
test('saved positions are validated; stale snapshots cannot erase unread or rewind successful check',()=>{
  const state=r.reconcile(r.empty(),[],date,now).state;
  const updated=r.reconcile(state,[commit('a')],date,now+1).state;
  assert.equal(r.reconcile(updated,[],'2026-10-01T00:00:00Z',now+2).stale,true);
  assert.deepEqual(r.reconcile(updated,[],'2026-10-01T00:00:00Z',now+2).state,updated);
  const invalid={...state,position:{view:'not-a-view',scope:'all',y:0,offset:0,visible:150,anchor:null}};
  assert.equal(r.parse(JSON.stringify(invalid)).position,null);
  assert.throws(()=>r.parse(JSON.stringify({...state,snapshot:'wrong'})));
  const valid={view:'activityView',scope:'all',y:123,offset:-25,visible:300,anchor:'["day","p"]'};
  assert.deepEqual(r.parse(JSON.stringify({...state,position:valid})).position,valid);
});
test('all-read captures loaded snapshot even under filters, preserving another tab’s later entries',()=>{
  const b=browser();
  b.run(`activityData.events=[${JSON.stringify(commit('a'))},${JSON.stringify(commit('b'))}];ingestReadingSnapshot();document.getElementById('activityQ').value='not matching';renderActivity();`);
  assert.equal(b.get('activityCount').textContent,0);
  b.run(`readingState=reading.reconcile(readingState,[...activityData.events,${JSON.stringify(commit('concurrent'))}],activityData.generated_at).state;saveReading();`);
  b.handlers.get('markRead:click')();
  const saved=r.parse(b.storage[r.KEY]);
  assert.equal(saved.seen[r.ids(commit('a'))[0]],false);assert.equal(saved.seen[r.ids(commit('b'))[0]],false);assert.equal(saved.seen[r.ids(commit('concurrent'))[0]],true);
});
test('unread exposes the whole range with bounded incremental rendering; bookmarks remain filterable',()=>{
  const b=browser();b.context.many=Array.from({length:180},(_,i)=>commit(String(i)));
  b.run('activityData.events=many;ingestReadingSnapshot();renderActivity()');
  assert.equal(b.get('activityCount').textContent,180);assert.equal(b.run('activityRenderedCount'),150);assert.equal((b.get('activityFeed').innerHTML.match(/data-reading-anchor=/g)||[]).length,150);b.run('renderActivity(true)');assert.equal(b.run('activityRenderedCount'),180);assert.equal((b.get('activityFeed').innerHTML.match(/data-reading-anchor=/g)||[]).length,180);assert.equal(b.get('activityMore').hidden,true);
  b.run("inboxView='bookmarks';renderActivity()");assert.equal(b.get('activityCount').textContent,0);
  b.run("bookmarks.add('p');renderActivity()");assert.equal(b.get('activityCount').textContent,180);
  b.run("projects.push({id:'other',title:'Other'});document.getElementById('bookmarkedProjects').checked=true;render()");assert.equal(b.get('count').textContent,1);
});
test('scroll anchor restores its offset without navigation; bookmark export is small versioned JSON',async()=>{
  const b=browser();let restored;
  b.context.anchor={dataset:{readingAnchor:'anchor'},getBoundingClientRect:()=>({top:300,bottom:400})};
  b.context.scroll=(x,y)=>{restored=y;};
  b.run("document.querySelectorAll=()=>[anchor];window.scrollY=100;window.scrollTo=scroll;restorePosition({view:'activityView',anchor:'anchor',offset:-25,y:0})");
  assert.equal(restored,425);
  let blob,clicked=false;
  b.context.Blob=Blob;b.context.URL={createObjectURL:value=>{blob=value;return 'blob:export';},revokeObjectURL:()=>{}};
  b.context.link={click:()=>{clicked=true;}};
  b.run("document.createElement=()=>link;bookmarks.add('p')");b.handlers.get('exportBookmarks:click')();
  assert.equal(clicked,true);assert.deepEqual(r.parseBookmarks(await blob.text()),['p']);
});
test('return restores both views’ queries, facets, direction, bookmark-only filter and sort; malformed filters are rejected atomically',()=>{
  const b=browser();
  b.run("projectFilterState.cpu.add('68000 family');projectFilterState.directionMode='route';activityFilterState.days='7';activityFilterState.type.add('release');document.getElementById('q').value='project';document.getElementById('activityQ').value='release';document.getElementById('bookmarkedProjects').checked=true;sort={key:'updated',dir:-1};savedFilters=captureFilters()");
  b.run("projectFilterState.cpu.clear();activityFilterState.type.clear();document.getElementById('q').value='';document.getElementById('bookmarkedProjects').checked=false");
  assert.equal(b.run('restoreFilters(savedFilters)'),true);
  assert.equal(b.run("projectFilterState.cpu.has('68000 family')"),true);assert.equal(b.run("activityFilterState.type.has('release')"),true);
  assert.equal(b.get('q').value,'project');assert.equal(b.get('activityQ').value,'release');assert.equal(b.get('bookmarkedProjects').checked,true);assert.equal(b.run('sort.dir'),-1);
  b.run("savedFilters.activity.days='bad';savedFilters.q='not applied'");assert.equal(b.run('restoreFilters(savedFilters)'),false);assert.equal(b.get('q').value,'project');
});
test('v1 migration restores all available entries unread once, including explicit reads whose origin cannot be proved',()=>{
  const a=commit('a'),b=commit('b');
  const old={version:1,checked:now,snapshot:date,seen:{[r.ids(a)[0]]:false,[r.ids(b)[0]]:true},position:null};
  const migrated=r.parse(JSON.stringify(old));assert.equal(migrated.version,2);assert.equal(migrated.migrationNotice,true);
  let state=r.reconcile(migrated,[a,b],date,now+1).state;
  assert.equal(state.seen[r.ids(a)[0]],true);assert.equal(state.seen[r.ids(b)[0]],true);
  state=r.acknowledge(state,r.ids(a));assert.equal(state.migrationNotice,false);
  state=r.reconcile(r.parse(JSON.stringify(state)),[a,b],date,now+2).state;
  assert.equal(state.seen[r.ids(a)[0]],false);assert.equal(state.seen[r.ids(b)[0]],true);
});
test('empty first visit does not acknowledge later arrivals; explicit reads persist on reload/fetch and through summary compaction',()=>{
  const a=commit('a'),b=commit('b');
  let state=r.reconcile(r.empty(),[],date,now).state;
  state=r.reconcile(state,[a],date,now+1).state;assert.equal(state.seen[r.ids(a)[0]],true);
  state=r.acknowledge(state,r.ids(a));
  const summary={type:'daily_commits',project_id:'p',date,day:'2026-10-29',count:2,shas:['a','b']};
  state=r.reconcile(r.parse(JSON.stringify(state)),[summary],date,now+2).state;
  assert.equal(state.seen[r.ids(a)[0]],false);assert.equal(state.seen[r.ids(b)[0]],true);
  state=r.acknowledge(state,r.ids(summary));
  assert.ok(Object.values(r.reconcile(r.parse(JSON.stringify(state)),[summary],date,now+3).state.seen).every(value=>value===false));
});
test('identity-less summaries start unread and only explicit acknowledgement clears them; changed counts reappear honestly',()=>{
  const summary={type:'daily_commits',project_id:'p',date,count:5};
  let state=r.reconcile(r.empty(),[summary],date,now).state;
  assert.equal(state.seen[r.ids(summary)[0]],true);
  state=r.reconcile(r.parse(JSON.stringify(state)),[summary],date,now+1).state;assert.equal(state.seen[r.ids(summary)[0]],true);
  state=r.acknowledge(state,r.ids(summary));
  state=r.reconcile(state,[summary],date,now+2).state;assert.equal(state.seen[r.ids(summary)[0]],false);
  const changed={...summary,count:6};state=r.reconcile(state,[changed],date,now+3).state;assert.equal(state.seen[r.ids(changed)[0]],true);
});
test('large first inbox creates only one render batch, and mark all read acknowledges even not-yet-rendered entries',()=>{
  const b=browser();b.context.many=Array.from({length:47000},(_,i)=>commit(String(i)));
  b.run('activityData.events=many;ingestReadingSnapshot();renderActivity()');
  assert.equal(b.get('activityCount').textContent,47000);assert.equal(b.run('activityRenderedCount'),150);assert.equal((b.get('activityFeed').innerHTML.match(/data-reading-anchor=/g)||[]).length,150);
  b.handlers.get('markRead:click')();assert.equal(b.get('unreadCount').textContent,0);
  b.run('readingState=reading.parse(localStorage.getItem(reading.KEY));ingestReadingSnapshot();renderActivity()');assert.equal(b.get('unreadCount').textContent,0);
});
test('intersection observer automatically appends batches without repeated controls or duplicate entries',()=>{
  let notify;
  const b=browser({}, {IntersectionObserver:class{constructor(callback){notify=callback;}observe(){}}});
  b.context.many=Array.from({length:460},(_,i)=>commit(String(i)));
  b.run('activityData.events=many;ingestReadingSnapshot();renderActivity()');
  assert.equal(b.get('activityMore').hidden,true);assert.equal(b.run('activityRenderedCount'),150);
  for(let i=0;i<4;i++)notify([{isIntersecting:true}]);
  assert.equal(b.run('activityRenderedCount'),460);assert.equal((b.get('activityFeed').innerHTML.match(/data-reading-anchor=/g)||[]).length,460);assert.equal(b.get('activitySentinel').hidden,true);
});
test('deep reading-position restore yields between bounded batches, and newer navigation cancels pending restoration',()=>{
  const queue=[];let scroll;
  const b=browser({}, {setTimeout:callback=>queue.push(callback)});
  b.context.many=Array.from({length:460},(_,i)=>commit(String(i)));
  b.run('activityData.events=many;ingestReadingSnapshot();renderActivity()');
  b.context.targetAnchor=r.ids(b.context.many[400])[0];b.context.scroll=(x,y)=>{scroll=y;};
  b.run("window.scrollTo=scroll;document.querySelectorAll=()=>activityRenderedEvents.slice(0,activityRenderedCount).map(event=>({dataset:{readingAnchor:reading.ids(event)[0]},getBoundingClientRect:()=>({top:75})}));restorePosition({view:'activityView',anchor:targetAnchor,offset:25,y:0})");
  assert.equal(b.run('activityRenderedCount'),150);assert.equal(queue.length,1);
  queue.shift()();assert.equal(b.run('activityRenderedCount'),300);
  queue.shift()();assert.equal(b.run('activityRenderedCount'),450);assert.equal(scroll,50);
  b.run('renderActivity();restorePosition({view:"activityView",anchor:targetAnchor,offset:25,y:0});requestActivityRender()');
  while(queue.length)queue.shift()();assert.equal(b.run('activityRenderedCount'),150);
});
test('one-time migration persists v2 and leaves bookmark export untouched',()=>{
  const bookmarkJSON=JSON.stringify({version:1,project_ids:['p']});
  const b=browser({[r.BOOKMARKS]:bookmarkJSON});
  b.context.old=JSON.stringify({version:1,checked:now,snapshot:date,seen:{},position:null});
  b.run(`localStorage.setItem(reading.KEY,old);activityData.events=[${JSON.stringify(commit('a'))}];ingestReadingSnapshot()`);
  assert.equal(b.get('migrationNotice').hidden,false);assert.equal(JSON.parse(b.storage[r.KEY]).version,2);assert.equal(b.storage[r.BOOKMARKS],bookmarkJSON);
  b.run('renderActivity()');b.handlers.get('markRead:click')();b.run('ingestReadingSnapshot();renderActivity()');
  assert.equal(b.get('unreadCount').textContent,0);assert.equal(b.get('migrationNotice').hidden,true);
});
