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
  const node=id=>({id,value:'',dataset:{},checked:false,hidden:false,innerHTML:'',insertAdjacentHTML:function(_,html){this.innerHTML+=html;},textContent:'',classList:{contains:()=>id==='activityView',toggle:()=>{}},setAttribute:()=>{},addEventListener:(event,fn)=>handlers.set(id+':'+event,fn),querySelectorAll:()=>[],querySelector:()=>node('child'),focus:()=>{},close:()=>{}});
  const get=id=>{if(!elements.has(id))elements.set(id,node(id));return elements.get(id);};
  const context=vm.createContext({document:{documentElement:{dataset:{}},getElementById:get,querySelector:()=>node('q'),querySelectorAll:()=>[]},window:{matchMedia:()=>({matches:false,addEventListener:()=>{}}),addEventListener:(event,fn)=>handlers.set('window:'+event,fn),scrollTo:()=>{}},localStorage:{getItem:key=>storage[key]||null,setItem:(key,value)=>{storage[key]=value;}},fetch:()=>new Promise(()=>{}),console,Date,Set,Map,Promise,setTimeout:()=>{},clearTimeout:()=>{},TrackerReading:r,...extras});
  vm.runInContext(fs.readFileSync(require.resolve('../web/tracker.js'),'utf8'),context);
  const run=code=>vm.runInContext(code,context);
  run(`projects=[{id:'p',title:'Project'}];projectsReady=true;activityReady=true;activityUiReady=true;readingInitialized=true;bindActivityProjectFacets=()=>{};loadProjectCatalogue=async()=>projects;activityData={generated_at:'${date}',events:[]};readingState=reading.reconcile(reading.empty(),[],activityData.generated_at).state;saveReading();`);
  return {run,get,handlers,storage,context};
}
test('activity loading and empty states span both columns; populated streams retain the timeline column',()=>{
  const css=fs.readFileSync(require.resolve('../web/tracker.css'),'utf8');
  const html=fs.readFileSync(require.resolve('../index.html'),'utf8');
  assert.match(html,/<nav\b[^>]*id="activityRail"[^>]*\bhidden[^>]*><\/nav>\s*<div class="activity-stream">/);
  assert.match(css,/\.activity-stream\{[^}]*grid-column:2(?:;|\})/);
  assert.match(css,/\.activity-timeline\[hidden\]\s*\+\s*\.activity-stream\{[^}]*grid-column:1\s*\/\s*-1(?:;|\})/);
  const b=browser();
  b.run('renderActivity()');
  assert.equal(b.get('activityRail').hidden,true);
  assert.match(b.get('activityFeed').innerHTML,/No unread activity matches/);
  b.run(`activityData.events=[${JSON.stringify(commit('a'))}];ingestReadingSnapshot();renderActivity()`);
  assert.equal(b.get('activityRail').hidden,false);
  b.run("$('activityQ').value='no matching activity';renderActivity()");
  assert.equal(b.get('activityRail').hidden,true);
  b.run("$('activityQ').value='';renderActivity()");
  assert.equal(b.get('activityRail').hidden,false);
  b.run("inboxView='bookmarks';renderActivity()");
  assert.equal(b.get('activityRail').hidden,true);
  assert.match(b.get('activityFeed').innerHTML,/No activity matches/);
});
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
  const b=browser({}, {IntersectionObserver:class{constructor(callback){this.callback=callback;}observe(node){if(node.id==='activitySentinel')notify=this.callback;}disconnect(){}}});
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
  b.run("window.scrollTo=scroll;document.querySelectorAll=selector=>selector==='[data-reading-anchor]'?activityRenderedEvents.slice(0,activityRenderedCount).map(event=>({dataset:{readingAnchor:reading.ids(event)[0]},getBoundingClientRect:()=>({top:75})})):[];restorePosition({view:'activityView',anchor:targetAnchor,offset:25,y:0})");
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
test('project names open details, external links and bookmark remain independent',()=>{
  const b=browser();
  b.run("projects=[{id:'p',title:'A long <project> name',repo:'https://example.com/project'}];render()");
  const row=b.get('rows').innerHTML;
  assert.match(row,/<button type="button" class="project-title" data-open-project="p" aria-haspopup="dialog"[^>]*>A long &lt;project&gt; name<\/button>/);
  assert.match(row,/<a href="https:\/\/example.com\/project" target="_blank" rel="noopener noreferrer"[^>]*><span>Source repository<\/span>/);
  assert.match(row,/data-bookmark="p"[^>]*aria-pressed="false"[^>]*aria-label="Bookmark A long &lt;project&gt; name"/);
  const header=b.run("activityProjectHeader(projects[0])");
  assert.match(header,/class="project-title" data-open-project="p"/);
  assert.match(header,/class="project-links"/);
  b.run("bookmarks.add('p');projects[0].repo=null;render()");
  assert.doesNotMatch(b.get('rows').innerHTML,/class="project-links"/);
  assert.match(b.get('rows').innerHTML,/data-bookmark="p"[^>]*aria-pressed="true"/);
  assert.match(b.run('activityProjectHeader(projects[0])'),/aria-label="Remove bookmark for A long &lt;project&gt; name"/);
});

function mockTimeline(b){
  b.run(`
    globalThis.railBody={innerHTML:'',querySelector:()=>({focus(){}})};
    globalThis.track={scrollTop:0,clientHeight:480,querySelector:()=>railBody,addEventListener(){}};
    globalThis.daySelect={value:''};
    $('activityRail').querySelector=selector=>selector==='.timeline-marks'?track:selector==='.timeline-day-jump'?daySelect:{focus(){}};
    $('activityRail').contains=()=>false;
  `);
}
test('timeline uses paged day/project order and local dates, with individual accessible targets',()=>{
  const b=browser();
  b.context.timelineEvents=[
    {project_id:'a',date:'2026-10-06T23:00:00'},
    {project_id:'b',date:'2026-10-06T22:00:00'},
    {project_id:'a',date:'2026-10-06T21:00:00'},
    {project_id:'c',date:'2026-10-05'}
  ];
  const entries=b.run('activityRailEntries(timelineEvents,new Map())');
  assert.deepEqual(Array.from(entries,e=>[e.id,e.index,e.dayStart]),[['a',0,true],['b',1,false],['c',3,true]]);
  assert.equal(entries[2].day,'2026-10-05');
  mockTimeline(b);
  b.run("activityRenderedEvents=timelineEvents;activityRenderedCount=0;activityTimelineEntries=activityRailEntries(timelineEvents,new Map());bookmarks=new Set(['b']);renderActivityRail()");
  const html=b.context.railBody.innerHTML;
  assert.equal((html.match(/data-timeline-index=/g)||[]).length,3);
  assert.match(html,/timeline-bookmarked[^>]+data-timeline-index="1"/);
  assert.match(html,/aria-label="Jump to c/);
});
test('bookmark updates all occurrences in place without rendering or scrolling',()=>{
  const b=browser();
  b.run(`
    const makeStar=()=>({dataset:{bookmark:'p'},isConnected:true,setAttribute(name,value){this[name]=value;},closest:()=>({classList:{toggle:(name,on)=>{}}}),getBoundingClientRect:()=>{throw Error('forced layout');}});
    const stars=[makeStar(),makeStar()];
    document.querySelectorAll=selector=>selector==='[data-bookmark]'||selector==='.view-panel.active [data-bookmark]'?stars:[];
    render=()=>{throw Error('project rebuilt');};renderActivity=()=>{throw Error('activity rebuilt');};
    renderActivityRail=()=>{};window.scrollBy=()=>{throw Error('scrolled');};
    bookmarkClick({target:{closest:()=>stars[0]},preventDefault(){},stopPropagation(){}});
    globalThis.result=stars.map(star=>[star.textContent,star['aria-pressed'],star['aria-label']]);
  `);
  assert.deepEqual(Array.from(b.context.result,row=>Array.from(row)),[['★','true','Remove bookmark for Project'],['★','true','Remove bookmark for Project']]);
  b.run("bookmarkClick({target:{closest:()=>stars[0]},preventDefault(){},stopPropagation(){}})");
  assert.equal(b.run("bookmarks.has('p')"),false);
});
test('timeline jumps load bounded batches, then focus the target; stale navigation is cancelled',()=>{
  const queue=[];const b=browser({}, {setTimeout:callback=>queue.push(callback)});
  b.context.many=Array.from({length:460},(_,i)=>commit(String(i)));
  b.run(`activityData.events=many;ingestReadingSnapshot();renderActivity();
    globalThis.jumped=false;
    const target={scrollIntoView(){globalThis.jumped=true;},focus(){}};
    document.querySelectorAll=selector=>selector==='#activityFeed [data-reading-anchor]'?activityRenderedEvents.slice(0,activityRenderedCount).map(event=>({dataset:{readingAnchor:reading.ids(event)[0]},closest:()=>target})):[];
    navigateActivity(400);`);
  assert.equal(b.run('activityRenderedCount'),300);
  while(queue.length)queue.shift()();
  assert.equal(b.run('activityRenderedCount'),450);assert.equal(b.context.jumped,true);
  b.run('jumped=false;renderActivity();navigateActivity(400);activityRenderRevision++');
  while(queue.length)queue.shift()();
  assert.equal(b.context.jumped,false);
});

test('bookmark-only removal drops every project occurrence and empty days while retaining other nodes',()=>{
  const b=browser();
  b.context.events=[commit('a'),commit('b'),{...commit('c'),project_id:'q'}];
  b.run(`
    inboxView='bookmarks';bookmarks=new Set(['p','q']);saveBookmarks();
    activityRenderedEvents=events;activityRenderedCount=3;
    activityTimelineEntries=activityRailEntries(events,new Map());
    globalThis.groups=['p','p','q'].map(id=>({dataset:{projectId:id},removed:false,remove(){this.removed=true;},classList:{toggle(){}}}));
    globalThis.stars=groups.map(group=>({dataset:{bookmark:group.dataset.projectId},get isConnected(){return !group.removed;},setAttribute(){},closest:()=>group,getBoundingClientRect:()=>({top:100}),focus(){globalThis.focused=this.dataset.bookmark;}}));
    globalThis.dayRemoved=false;
    const day={querySelector:()=>groups[0].removed?null:groups[0],remove(){globalThis.dayRemoved=true;}};
    document.querySelectorAll=selector=>selector==='[data-bookmark]'?stars:selector==='.view-panel.active [data-bookmark]'?stars:selector==='#activityFeed .activity-project'?groups:selector==='#activityFeed .activity-day'&&!dayRemoved?[day]:[];
    render=renderActivity=()=>{throw Error('rebuilt feed');};renderActivityRail=()=>{};window.scrollBy=()=>{};
    bookmarkClick({target:{closest:()=>stars[0]},preventDefault(){},stopPropagation(){}});
  `);
  assert.deepEqual(Array.from(b.context.groups,group=>group.removed),[true,true,false]);
  assert.equal(b.context.dayRemoved,true);assert.equal(b.context.focused,'q');
  assert.equal(b.run('activityRenderedCount'),1);assert.equal(b.get('activityCount').textContent,1);
  assert.equal(b.run('activityTimelineEntries.length'),1);
});

test('current timeline day follows scrolling in both directions without IntersectionObserver',()=>{
  const b=browser();
  b.run(`
    globalThis.bottoms=[100,300,600];
    activityDayNodes=['2026-10-06','2026-10-05','2026-10-04'].map((day,index)=>({dataset:{day},getBoundingClientRect:()=>({bottom:bottoms[index]})}));
    updateCurrentActivityDay();
  `);
  assert.equal(b.get('timelineCurrentDay').textContent,'2026-10-06');
  b.run('bottoms=[-100,-20,300];updateCurrentActivityDay()');
  assert.equal(b.get('timelineCurrentDay').textContent,'2026-10-04');
  b.run('bottoms=[-20,200,500];updateCurrentActivityDay()');
  assert.equal(b.get('timelineCurrentDay').textContent,'2026-10-05');
  b.run('bottoms=[100,300,600];updateCurrentActivityDay()');
  assert.equal(b.get('timelineCurrentDay').textContent,'2026-10-06');
});
test('current day highlights all matching notches but announces only one current location',()=>{
  const b=browser();
  b.run(`
    globalThis.marks=['2026-10-06','2026-10-06','2026-10-05'].map(day=>({dataset:{day},classList:{toggle(){}},setAttribute(name,value){this[name]=value;},removeAttribute(name){delete this[name];}}));
    document.querySelectorAll=selector=>selector==='#activityRail [data-day]'?marks:[];
    highlightActivityDay('2026-10-06');
  `);
  assert.equal(b.context.marks.filter(mark=>mark['aria-current']==='location').length,1);
  b.run("highlightActivityDay('2026-10-05')");
  assert.equal(b.context.marks.filter(mark=>mark['aria-current']==='location').length,1);
  assert.equal(b.context.marks[2]['aria-current'],'location');
});

test('following the current day scrolls only the rail and leaves rail browsing undisturbed',()=>{
  const b=browser();mockTimeline(b);
  b.run(`
    activityTimelineEntries=Array.from({length:100},(_,index)=>({index,id:'p',day:'2026-10-06',label:'Project'}));
    currentActivityDay='2026-10-06';timelineDayIndices=new Map([[currentActivityDay,30]]);
    window.scrollTo=window.scrollBy=()=>{throw Error('page scrolled');};
    revealCurrentTimelineDay();
  `);
  assert.equal(b.context.track.scrollTop,264);
  b.run('timelineDayIndices.set(currentActivityDay,1);revealCurrentTimelineDay()');
  assert.equal(b.context.track.scrollTop,24);
  b.run('timelinePointerInside=true;timelineDayIndices.set(currentActivityDay,60);revealCurrentTimelineDay()');
  assert.equal(b.context.track.scrollTop,24);
  b.run("timelinePointerInside=false;$('activityRail').contains=()=>true;revealCurrentTimelineDay()");
  assert.equal(b.context.track.scrollTop,24);
});
test('twenty thousand individual timeline entries use a bounded DOM window and keyboard reaches both ends',()=>{
  const b=browser();mockTimeline(b);
  b.run(`
    activityTimelineEntries=Array.from({length:20000},(_,index)=>({index,id:'p'+index,day:index<10000?'2026-10-06':'2026-10-05',dayStart:index===0||index===10000,label:'Project '+index}));
    activityRenderedEvents=[{date:'2026-10-06'},{date:'2026-10-05'}];
    renderActivityRail();
  `);
  const count=()=> (b.context.railBody.innerHTML.match(/data-rail-index=/g)||[]).length;
  assert.ok(count()>0&&count()<=64);
  assert.equal((b.get('activityRail').innerHTML.match(/<option /g)||[]).length,2);
  assert.match(b.get('activityRail').innerHTML,/height:480000px/);
  b.handlers.get('activityRail:keydown')({key:'End',preventDefault(){},target:{closest:()=>({dataset:{railIndex:'0'}})}});
  assert.equal(b.run('timelineFocusIndex'),19999);assert.ok(count()<=64);
  assert.match(b.context.railBody.innerHTML,/data-rail-index="19999"/);
  b.handlers.get('activityRail:keydown')({key:'Home',preventDefault(){},target:{closest:()=>({dataset:{railIndex:'19999'}})}});
  assert.equal(b.run('timelineFocusIndex'),0);assert.equal(b.context.track.scrollTop,0);
  assert.match(b.context.railBody.innerHTML,/data-rail-index="0"/);
  b.run('navigateActivity=index=>{globalThis.dayJumpTarget=index;}');
  b.handlers.get('activityRail:change')({target:{matches:()=>true,value:'10000'}});
  assert.equal(b.context.dayJumpTarget,10000);assert.ok(count()<=64);
});
test('a newer timeline jump cancels an older jump that is still loading batches',()=>{
  const queue=[],b=browser({}, {setTimeout:callback=>queue.push(callback)});
  b.context.many=Array.from({length:600},(_,i)=>commit(String(i)));
  b.run(`activityData.events=many;ingestReadingSnapshot();renderActivity();
    globalThis.jumps=[];
    document.querySelectorAll=selector=>selector==='#activityFeed [data-reading-anchor]'?activityRenderedEvents.slice(0,activityRenderedCount).map((event,index)=>({dataset:{readingAnchor:reading.ids(event)[0]},closest:()=>({scrollIntoView(){jumps.push(index);},focus(){}})})):[];
    navigateActivity(550);navigateActivity(10);`);
  while(queue.length)queue.shift()();
  assert.deepEqual(Array.from(b.context.jumps),[10]);
  assert.equal(b.run('activityRenderedCount'),300);
});

test('rail Home/End focuses only the final notch without page scrolling or transient focus',()=>{
  const b=browser();mockTimeline(b);
  b.run(`
    activityTimelineEntries=Array.from({length:20000},(_,index)=>({index,id:'p',day:'2026-10-06',label:'Project'}));
    globalThis.focuses=[];
    document.activeElement={dataset:{railIndex:'0'}};
    railBody.querySelector=selector=>({focus(options){focuses.push({selector,options,transient:true});}});
    $('activityRail').querySelector=selector=>selector==='.timeline-marks'?track:{focus(options){focuses.push({selector,options,transient:false});}};
    window.scrollTo=window.scrollBy=()=>{throw Error('page scroll requested');};
    focusTimelineIndex(19999);
  `);
  assert.equal(b.context.focuses.length,1);
  assert.equal(b.context.focuses[0].transient,false);
  assert.equal(b.context.focuses[0].options.preventScroll,true);
  assert.equal(b.context.focuses[0].selector,'[data-rail-index="19999"]');
  b.run("document.activeElement={dataset:{railIndex:'19999'}};focuses=[];focusTimelineIndex(0)");
  assert.equal(b.context.focuses.length,1);
  assert.equal(b.context.focuses[0].selector,'[data-rail-index="0"]');
  const css=fs.readFileSync(require.resolve('../web/tracker.css'),'utf8');
  assert.match(css,/\.activity-timeline\{[^}]*overflow-anchor:none/);
  assert.match(css,/\.timeline-marks\{[^}]*overscroll-behavior:contain/);
});

const unavailableSource={status:'unavailable',http_status:404,retryable:true};
test('only explicit retryable root 404 metadata produces an unavailable marker',()=>{
  const b=browser();b.context.status=unavailableSource;
  assert.equal(b.run('repositoryUnavailable({github:{source_availability:status}})'),true);
  assert.equal(b.run('repositoryUnavailable({repo:"https://gitlab.com/g/p",gitlab:{source_availability:status}})'),true);
  for(const httpStatus of [401,403,429,500,503]){
    b.context.status={...unavailableSource,http_status:httpStatus};
    assert.equal(b.run('repositoryUnavailable({github:{source_availability:status}})'),false);
  }
  for(const status of [{status:'available',http_status:404,retryable:true},{status:'unavailable',http_status:404},{status:'error',http_status:404,retryable:true}]){
    b.context.status=status;assert.equal(b.run('repositoryUnavailable({github:{source_availability:status}})'),false);
  }
  b.context.status=unavailableSource;
  assert.equal(b.run('repositoryUnavailable({repo:"https://gitlab.com/g/p",gitlab:{},github:{source_availability:status}})'),false);
  assert.equal(b.run('repositoryUnavailable({repo:"https://github.com/g/p",github:{latest_release:null},gitlab:{source_availability:status}})'),false);
});

test('one bookmarked warning covers the whole catalogue independent of events, filters and read status',()=>{
  const b=browser();b.context.status=unavailableSource;
  b.run(`projects=[{id:'p',title:'Affected without events',github:{source_availability:status}},
    {id:'q',title:'Affected GitLab',gitlab:{source_availability:status}},
    {id:'r',title:'Not bookmarked',github:{source_availability:status}},
    {id:'healthy',title:'Healthy'}];
    bookmarks=new Set(['p','q','healthy','removed']);
    activityData.events=[{type:'commit',project_id:'q',date:'${date}',sha:'one'},{type:'project_removed',project_id:'removed',date:'${date}',project:{id:'removed',github:{source_availability:status}}}];
    ingestReadingSnapshot();
    $('activityQ').value='nothing matches';activityFilterState.days='2';activityFilterState.type.add('release');
    renderActivity();`);
  assert.equal(b.get('sourceAvailabilityWarning').hidden,false);
  assert.equal(b.get('sourceAvailabilitySummary').textContent,'Updates may be incomplete for 2 bookmarked projects.');
  assert.equal((b.get('sourceAvailabilityProjects').innerHTML.match(/data-source-details=/g)||[]).length,2);
  assert.match(b.get('sourceAvailabilityProjects').innerHTML,/Affected without events/);
  assert.doesNotMatch(b.get('sourceAvailabilityProjects').innerHTML,/Not bookmarked|removed/);
  assert.equal(b.get('activityCount').textContent,0);assert.equal(b.get('unreadCount').textContent,2);
  b.handlers.get('markRead:click')();
  assert.equal(b.get('unreadCount').textContent,0);assert.equal(b.get('sourceAvailabilityWarning').hidden,false);
  for(const scope of ['unread','all','bookmarks']){
    b.run(`inboxView='${scope}';renderActivity()`);
    assert.equal(b.get('sourceAvailabilityWarning').hidden,false);assert.equal(b.get('activityCount').textContent,0);
  }
  b.run('activityData.events=[];ingestReadingSnapshot();renderActivity()');
  assert.equal(b.get('unreadCount').textContent,0);assert.equal(b.get('sourceAvailabilityWarning').hidden,false);
  assert.equal(b.run('combinedActivityEvents().length'),0);
});

test('bookmark warning updates in place, escapes titles and keeps unchanged notice DOM',()=>{
  const b=browser();b.context.status=unavailableSource;
  b.run(`projects[0].title="Project <unsafe> & O'Neil";projects[0].github={source_availability:status};
    render=renderActivity=()=>{throw Error('feed rebuilt');};
    globalThis.click={target:{closest:()=>({dataset:{bookmark:'p'},isConnected:true})},preventDefault(){},stopPropagation(){}};
    bookmarkClick(click);`);
  assert.equal(b.get('sourceAvailabilityWarning').hidden,false);
  assert.match(b.get('sourceAvailabilityProjects').innerHTML,/Project &lt;unsafe&gt; &amp; O&#39;Neil/);
  const list=b.get('sourceAvailabilityProjects');let rewrites=0;const content=list.innerHTML;
  Object.defineProperty(list,'innerHTML',{get:()=>content,set:()=>{rewrites++;}});
  b.run('updateSourceAvailabilityWarning();updateSourceAvailabilityWarning(true)');assert.equal(rewrites,0);
  b.run('bookmarkClick(click)');assert.equal(b.get('sourceAvailabilityWarning').hidden,true);
});

test('bookmark imports and other-tab changes immediately update source warnings',async()=>{
  const b=browser();b.context.status=unavailableSource;
  b.run('projects[0].github={source_availability:status};updateSourceAvailabilityWarning()');
  assert.equal(b.get('sourceAvailabilityWarning').hidden,true);
  await b.handlers.get('importBookmarks:change')({target:{files:[{size:30,text:async()=>'{"version":1,"project_ids":["p"]}'}]}});
  assert.equal(b.get('sourceAvailabilityWarning').hidden,false);
  b.handlers.get('window:storage')({key:r.BOOKMARKS,newValue:'{"version":1,"project_ids":[]}'});
  assert.equal(b.get('sourceAvailabilityWarning').hidden,true);
  b.handlers.get('window:storage')({key:r.BOOKMARKS,newValue:'{"version":1,"project_ids":["p"]}'});
  assert.equal(b.get('sourceAvailabilityWarning').hidden,false);
});

test('successful snapshot recovery clears source notice without inventing activity or unread items',async()=>{
  const b=browser();b.context.status=unavailableSource;
  b.run('projects[0].github={source_availability:status};bookmarks.add("p");renderActivity()');
  assert.equal(b.get('sourceAvailabilityWarning').hidden,false);
  b.run(`loadProjectCatalogue=async()=>[{id:'p',title:'Recovered',github:{}}];loadActivitySnapshot=async()=>({generated_at:'${date}',events:[]});`);
  await b.run('fetchUpdates()');
  assert.equal(b.get('sourceAvailabilityWarning').hidden,true);assert.equal(b.get('unreadCount').textContent,0);
  assert.equal(b.run('combinedActivityEvents().length'),0);assert.equal(b.run('bookmarks.has("p")'),true);
});

test('notice height changes above the viewport preserve feed position without measuring activity groups',()=>{
  const b=browser();b.context.status=unavailableSource;
  b.run(`projects[0].github={source_availability:status};updateSourceAvailabilityWarning();
    window.scrollY=700;window.scrollTo=(x,y)=>{window.scrollY=y;};
    $('sourceAvailabilitySlot').getBoundingClientRect=()=>({top:-500,height:$('sourceAvailabilityWarning').hidden?0:40});
    document.querySelectorAll=()=>{throw Error('measured activity groups');};
    bookmarks.add('p');updateSourceAvailabilityWarning(true);`);
  assert.equal(b.run('window.scrollY'),740);
  b.run('bookmarks.delete("p");updateSourceAvailabilityWarning(true)');assert.equal(b.run('window.scrollY'),700);
  b.run(`window.scrollY=0;$('sourceAvailabilitySlot').getBoundingClientRect=()=>({top:200,height:$('sourceAvailabilityWarning').hidden?0:40});bookmarks.add('p');updateSourceAvailabilityWarning(true)`);
  assert.equal(b.run('window.scrollY'),0);
});

test('GitLab release fallback deduplicates durable release events by project and tag',()=>{
  const b=browser();
  b.run(`projects=[{id:'p',repo:'https://gitlab.com/g/sub/p',gitlab:{repository:'gitlab.com/g/sub/p',latest_release:{tag:'v2',name:'Version 2',published_at:'2026-10-28',url:'https://gitlab.com/g/sub/p/-/releases/v2'}}}];`);
  const synthetic=b.run('combinedActivityEvents()');
  assert.equal(synthetic.length,1);assert.equal(synthetic[0].repository,'gitlab.com/g/sub/p');assert.equal(synthetic[0].tag,'v2');
  b.run(`activityData.events=[{type:'release',project_id:'p',tag:'v2',sha:'associated-commit',title:'Canonical release',date:'2026-10-28T15:00:00Z',url:'https://gitlab.com/g/sub/p/-/releases/v2'}];`);
  assert.equal(b.run('combinedActivityEvents().length'),1);assert.equal(b.run('combinedActivityEvents()[0].title'),'Canonical release');
  b.run(`activityData.events.push({type:'release',project_id:'p',tag:'v1',title:'Earlier release',date:'2026-10-20T15:00:00Z'});`);
  assert.equal(b.run('combinedActivityEvents().length'),2);
  b.run(`activityData.events=[];projects[0].gitlab.latest_release.published_at='2026-11-15';`);assert.equal(b.run('combinedActivityEvents().length'),0);
  b.run(`projects[0].gitlab.latest_release.published_at='invalid';`);assert.equal(b.run('combinedActivityEvents().length'),0);
});

test('GitLab addition display uses provider metadata and preserves frozen release context',()=>{
  const b=browser();
  b.run(`projects[0].repo='https://gitlab.com/g/p';projects[0].gitlab={repository:'gitlab.com/g/p',latest_commit:{date:'2026-10-28',url:'https://gitlab.com/g/p/-/commit/a'},latest_release:{tag:'v2',published_at:'2026-10-27',url:'https://gitlab.com/g/p/-/releases/v2'}};`);
  const html=b.run('additionContextHtml({type:"project_added"},projects[0])');
  assert.match(html,/Last commit/);assert.match(html,/releases\/v2/);assert.match(html,/Initial scan pending/);
  const frozen=b.run('additionContextHtml({type:"project_added",activity_context:{latest_release:{tag:"v1",published_at:"2026-10-20"},window_days:30,commits:1,active_days:1}},projects[0])');
  assert.match(frozen,/v1/);assert.doesNotMatch(frozen,/v2/);
});


test('source-status observation date is labelled first observed, never an invented last-check timestamp',()=>{
  const b=browser();b.context.status={...unavailableSource,checked_at:'2026-10-27T14:25:00Z'};
  const message=b.run('repositoryAvailability({github:{source_availability:status}})');
  assert.match(message,/First observed unavailable: 2026-10-27T14:25:00Z/);
  assert.doesNotMatch(message,/Last checked:|Last check:|Next check:/);
  for(const checked_at of [undefined,null,'invalid']){
    b.context.status={...unavailableSource,checked_at};
    assert.doesNotMatch(b.run('repositoryAvailability({github:{source_availability:status}})'),/First observed/);
  }
});

test('frozen addition release failures remain explicit and do not borrow newer status or releases',()=>{
  const b=browser();b.context.releaseStatus={status:'unavailable',http_status:403,retryable:true,checked_at:'2026-10-27T14:25:00Z'};
  b.run(`projects[0].repo='https://gitlab.com/g/p';projects[0].gitlab={latest_release:{tag:'v2',published_at:'2026-10-28'},release_availability:releaseStatus};`);
  const unknown=b.run('additionContextHtml({type:"project_added",activity_context:{release_availability:releaseStatus,window_days:30,commits:1,active_days:1}},projects[0])');
  assert.match(unknown,/Release information/);assert.match(unknown,/Unavailable to the tracker at addition \(HTTP 403\)/);
  assert.doesNotMatch(unknown,/v2|[Nn]o releases|Repository unavailable|Source unavailable/);
  const cached=b.run('additionContextHtml({type:"project_added",activity_context:{release_availability:releaseStatus,latest_release:{tag:"v1",published_at:"2026-10-20",url:"https://gitlab.com/g/p/-/releases/v1"}}},projects[0])');
  assert.match(cached,/releases\/v1/);assert.match(cached,/cached release retained/);assert.doesNotMatch(cached,/v2/);
  const healthy=b.run('additionContextHtml({type:"project_added",activity_context:{latest_release:{tag:"v1",published_at:"2026-10-20"}}},projects[0])');
  assert.doesNotMatch(healthy,/Release information|Unavailable to the tracker/);
  const current=b.run('additionContextHtml({type:"project_added"},projects[0])');
  assert.match(current,/v2/);assert.match(current,/Unavailable to the tracker \(HTTP 403\)/);assert.doesNotMatch(current,/at addition \(HTTP 403\)/);
});


test('hidden project state loads independently from bookmarks and malformed hidden state warns',()=>{
  const b=browser({[r.HIDDEN]:JSON.stringify({version:1,project_ids:['p','p','gone']}),[r.BOOKMARKS]:JSON.stringify({version:1,project_ids:['p']})});
  assert.equal(b.run('hiddenProjects.size'),2);assert.equal(b.run("bookmarks.has('p')"),true);
  assert.equal(b.run("hiddenProjects.has('gone')"),true);
  const invalid=browser({[r.HIDDEN]:'{"version":1,"project_ids":[7]}'});
  assert.equal(invalid.get('storageWarning').hidden,false);
});
test('hide and unhide persist IDs without changing bookmarks or unread identities',()=>{
  const b=browser();
  b.run(`activityData.events=[${JSON.stringify(commit('hidden'))}];ingestReadingSnapshot();bookmarks.add('p');saveBookmarks();renderActivity()`);
  const beforeReading=b.storage[r.KEY],beforeBookmarks=b.storage[r.BOOKMARKS];
  b.context.button={dataset:{hideProject:'p'},closest:()=>null,getBoundingClientRect:()=>({top:200}),isConnected:true};
  b.context.click={target:{closest:()=>b.context.button},preventDefault(){},stopPropagation(){}};
  b.run('hideProjectClick(click)');
  assert.deepEqual(r.parseBookmarks(b.storage[r.HIDDEN]),['p']);assert.equal(b.get('unreadCount').textContent,0);
  assert.equal(b.storage[r.KEY],beforeReading);assert.equal(b.storage[r.BOOKMARKS],beforeBookmarks);
  b.run('hideProjectClick(click)');assert.deepEqual(r.parseBookmarks(b.storage[r.HIDDEN]),[]);
  assert.equal(b.get('unreadCount').textContent,1);assert.equal(b.storage[r.KEY],beforeReading);
});
test('mark all read skips hidden entries, which become unread again when restored',()=>{
  const b=browser();
  b.context.events=[commit('hidden'),{...commit('visible'),project_id:'q'}];
  b.run("activityData.events=events;hiddenProjects.add('p');ingestReadingSnapshot();renderActivity()");
  assert.equal(b.get('unreadCount').textContent,1);
  b.handlers.get('markRead:click')();
  assert.equal(b.get('unreadCount').textContent,0);
  assert.equal(b.get('activityCount').textContent,0);
  assert.equal(b.get('activityProjectCount').textContent,0);
  assert.equal(b.get('activityRail').hidden,true);
  assert.match(b.get('activityFeed').innerHTML,/No unread activity matches/);
  assert.equal(b.run("readingState.seen[reading.ids(events[0])[0]]"),true);
  assert.equal(b.run("readingState.seen[reading.ids(events[1])[0]]"),false);
  b.run("hiddenProjects.delete('p');updateReadingControls()");assert.equal(b.get('unreadCount').textContent,1);
});
test('hidden-only unread stays empty after fetching the same snapshot and reload',async()=>{
  const b=browser({[r.HIDDEN]:JSON.stringify({version:1,project_ids:['p']})});
  b.context.events=[commit('hidden'),{...commit('visible'),project_id:'q'}];
  b.run(`activityData.events=events;loadActivitySnapshot=async()=>({generated_at:'${date}',events});ingestReadingSnapshot();renderActivity()`);
  b.handlers.get('markRead:click')();
  await b.run('fetchUpdates()');
  assert.match(b.get('readingStatus').textContent,/0 new items found/);
  assert.equal(b.get('unreadCount').textContent,0);
  assert.equal(b.get('activityCount').textContent,0);
  assert.equal(b.run('activityRenderedEvents.length'),0);
  assert.match(b.get('activityFeed').innerHTML,/No unread activity matches/);
  b.run('readingState=reading.parse(localStorage.getItem(reading.KEY));ingestReadingSnapshot();renderActivity()');
  assert.equal(b.run('activityRenderedEvents.length'),0);
  assert.equal(b.run('hasUnreadIdentity(events[0])'),true);
});
test('unhiding from the manager restores an empty unread feed without a fetch',()=>{
  const b=browser({[r.HIDDEN]:JSON.stringify({version:1,project_ids:['p']})});
  b.run(`activityData.events=[${JSON.stringify(commit('hidden'))}];ingestReadingSnapshot();renderActivity()`);
  assert.equal(b.run('activityRenderedEvents.length'),0);
  b.context.button={dataset:{hideProject:'p'},closest:()=>null,getBoundingClientRect:()=>({top:200}),isConnected:true};
  b.context.click={target:{closest:()=>b.context.button},preventDefault(){},stopPropagation(){}};
  b.run('hideProjectClick(click)');
  assert.equal(b.get('unreadCount').textContent,1);
  assert.equal(b.get('activityCount').textContent,1);
  assert.match(b.get('activityFeed').innerHTML,/data-reading-anchor=/);
});
test('hidden markers remain eligible beside visible unread matches and in All or Bookmarked activity',()=>{
  const b=browser();
  b.context.events=[{...commit('hidden'),title:'Hidden title'},{...commit('visible'),project_id:'q',title:'Visible title'}];
  b.run("projects.push({id:'q',title:'Other project'});activityData.events=events;hiddenProjects.add('p');bookmarks.add('p');ingestReadingSnapshot();renderActivity()");
  assert.equal(b.run('activityRenderedEvents.length'),2);
  b.run("$('activityQ').value='hidden';renderActivity()");
  assert.equal(b.run('activityRenderedEvents.length'),0);
  b.run("$('activityQ').value='';setInboxView('all');renderActivity()");
  assert.equal(b.run('activityRenderedEvents.length'),2);
  b.run("setInboxView('bookmarks');renderActivity()");
  assert.equal(b.run('activityRenderedEvents.length'),1);
});
test('hidden run partitioning merges adjacent hidden projects only and preserves order and duplicates',()=>{
  const groups=['a','b','a','visible','a','b','visible','c'].map(id=>({id}));
  const runs=r.hiddenRuns(groups,new Set(['a','b','c']));
  assert.deepEqual(runs.map(run=>({hidden:run.hidden,ids:run.groups.map(g=>g.id)})),[
    {hidden:true,ids:['a','b','a']},{hidden:false,ids:['visible']},{hidden:true,ids:['a','b']},{hidden:false,ids:['visible']},{hidden:true,ids:['c']}
  ]);
  assert.deepEqual(runs.flatMap(run=>run.groups),groups);
  assert.deepEqual(r.hiddenRuns([],new Set(['a'])),[]);
  const day1=r.hiddenRuns([{id:'a'}],new Set(['a'])),day2=r.hiddenRuns([{id:'a'}],new Set(['a']));
  assert.equal(day1.length,1);assert.equal(day2.length,1);assert.notEqual(day1[0],day2[0]);
});
test('hidden icons have escaped project-specific labels, pressed state, and appear beside bookmarks in both views',()=>{
  const b=browser();
  b.context.project={id:'x"<&',title:'A <B>'};
  const icon=b.run('hideButton(project)');
  assert.match(icon,/type="button"/);assert.match(icon,/aria-pressed="false"/);
  assert.match(icon,/aria-label="Hide activity for A &lt;B&gt;"/);assert.match(icon,/data-hide-project="x&quot;&lt;&amp;"/);
  assert.match(icon,/<svg[^>]*aria-hidden="true"/);assert.match(icon,/m3 3 18 18/);
  b.run('hiddenProjects.add(project.id)');assert.match(b.run('hideButton(project)'),/aria-label="Show activity for A &lt;B&gt;"/);
  assert.match(b.run('projectRowHtml(project)'),/data-bookmark=[\s\S]*data-hide-project=/);
  assert.match(b.run('activityProjectHeader(project)'),/data-bookmark=[\s\S]*data-hide-project=/);
});
test('near-bottom collapse adds enough scroll tail and restores clicked anchor offset',()=>{
  const b=browser();let scrolled;
  b.context.document.documentElement.style={overflowAnchor:'auto'};
  b.context.document.documentElement.scrollHeight=1000;
  b.context.window.innerHeight=800;b.context.window.scrollY=500;
  b.get('activityScrollSpace').style={height:'0px'};
  b.context.source={getBoundingClientRect:()=>({top:100})};
  b.context.target={isConnected:true,getBoundingClientRect:()=>({top:50}),focus(){}};
  b.context.window.scrollTo=(_,y)=>{scrolled=y;};
  b.run('keepActivityPosition(source,()=>{},()=>target)');
  assert.equal(scrolled,450);assert.equal(b.get('activityScrollSpace').style.height,'250px');
  assert.equal(b.context.document.documentElement.style.overflowAnchor,'auto');
});
test('hidden toggles merge a concurrent tab selection and storage events update exclusions',()=>{
  const b=browser();
  b.storage[r.HIDDEN]=JSON.stringify({version:1,project_ids:['other']});
  b.context.button={dataset:{hideProject:'p'},closest:()=>null,getBoundingClientRect:()=>({top:200}),isConnected:true};
  b.context.click={target:{closest:()=>b.context.button},preventDefault(){},stopPropagation(){}};
  b.run('hideProjectClick(click)');assert.deepEqual(r.parseBookmarks(b.storage[r.HIDDEN]),['other','p']);
  b.handlers.get('window:storage')({key:r.HIDDEN,newValue:JSON.stringify({version:1,project_ids:['q']})});
  assert.equal(b.run("hiddenProjects.has('q')"),true);assert.equal(b.run("hiddenProjects.has('p')"),false);
  b.handlers.get('window:storage')({key:r.HIDDEN,newValue:null});assert.equal(b.run('hiddenProjects.size'),0);
});
test('hidden storage write failure retains session selection and reports lack of persistence',()=>{
  const b=browser();
  b.context.button={dataset:{hideProject:'p'},closest:()=>null,getBoundingClientRect:()=>({top:200}),isConnected:true};
  b.context.click={target:{closest:()=>b.context.button},preventDefault(){},stopPropagation(){}};
  b.run("localStorage.setItem=()=>{throw Error('quota')};hideProjectClick(click)");
  assert.equal(b.run("hiddenProjects.has('p')"),true);assert.match(b.get('storageWarning').textContent,/tab only/);
});
test('hidden feeds retain manual pagination even when IntersectionObserver is supported',()=>{
  const b=browser();b.context.IntersectionObserver=function(){};
  b.context.many=Array.from({length:180},(_,i)=>commit(String(i)));
  b.run('activityData.events=many;ingestReadingSnapshot();renderActivity()');assert.equal(b.get('activityMore').hidden,true);
  b.run("hiddenProjects.add('p');updateActivityCounts()");assert.equal(b.get('activityMore').hidden,false);
  b.run('renderActivity(true)');assert.equal(b.get('activityMore').hidden,true);
});
test('restoration distinguishes hidden marker and expanded first commit and falls back after unhide',()=>{
  const b=browser();let scroll;
  b.context.window.scrollY=500;b.context.window.scrollTo=(_,y)=>{scroll=y;};
  b.context.marker={dataset:{readingAnchor:'hidden:anchor'},getBoundingClientRect:()=>({top:-200}),closest:()=>null};
  b.context.entry={dataset:{readingAnchor:'anchor'},getBoundingClientRect:()=>({top:100}),closest:()=>null};
  b.run("document.querySelectorAll=()=>[marker,entry];restorePosition({view:'activityView',anchor:'anchor',offset:25,y:0})");assert.equal(scroll,575);
  b.run("restorePosition({view:'activityView',anchor:'hidden:anchor',offset:25,y:0})");assert.equal(scroll,275);
  b.run("document.querySelectorAll=()=>[entry];restorePosition({view:'activityView',anchor:'hidden:anchor',offset:25,y:0})");assert.equal(scroll,575);
});
test('timeline navigation focuses the collapsed summary rather than its non-focusable details container',()=>{
  const b=browser();let focused=false,scrolled=false;
  const run={open:false,matches:()=>true,scrollIntoView(){scrolled=true;},querySelector:()=>summary};
  const summary={closest:()=>run,focus(){focused=true;}};
  const event=commit('nav');
  b.context.entry={dataset:{readingAnchor:r.ids(event)[0]},closest:()=>run};b.context.navEvent=event;
  b.run('activityRenderedEvents=[navEvent];activityRenderedCount=1;document.querySelectorAll=()=>[entry];highlightActivityDay=()=>{};navigateActivity(0)');
  assert.equal(scrolled,true);assert.equal(focused,true);
});
