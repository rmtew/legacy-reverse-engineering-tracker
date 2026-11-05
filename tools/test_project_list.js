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
    classList:{contains:()=>false,toggle:()=>{}},attributes:{},setAttribute(key,value){this.attributes[key]=value;},removeAttribute(key){delete this.attributes[key];},close(){},
    addEventListener(name,callback){(this.listeners[name]??=[]).push(callback);},
    set innerHTML(value){this.html=value;this.children=[];},get innerHTML(){return this.html;},
    insertAdjacentHTML(_,value){this.html+=value;for(const match of value.matchAll(/<tr class="project-row [^"]*" data-id="([^"]*)"/g)){const row={dataset:{id:match[1]},remove:()=>{this.children.splice(this.children.indexOf(row),1);}};this.children.push(row);}},
    querySelectorAll(){return this.children;}};}
  const headers=[...fs.readFileSync(path.join(root,'index.html'),'utf8').matchAll(/<th[^>]+data-key="([^"]+)"[^>]*>/g)].map(match=>{const header=node();header.dataset.key=match[1];return header;});
  const get=id=>{if(!elements.has(id))elements.set(id,node());return elements.get(id);};
  const context=vm.createContext({document:{documentElement:{dataset:{}},getElementById:get,querySelector:()=>node(),querySelectorAll:selector=>selector==='th[data-key]'?headers:[]},window:{matchMedia:()=>({matches:false,addEventListener(){}})},fetch:()=>new Promise(()=>{}),localStorage:{getItem(){return null;},setItem(){}},console,setTimeout:fn=>timers.push(fn),clearTimeout(){},...extra});
  vm.runInContext(fs.readFileSync(path.join(root,'web/reading-state.js'),'utf8'),context);
  vm.runInContext(fs.readFileSync(path.join(root,'web/tracker.js'),'utf8'),context);
  const run=code=>vm.runInContext(code,context);
  const records=Array.from({length:251},(_,i)=>({id:'p'+i,title:'Project '+i,source_platforms:['Amiga'],notes:i===250?'needle outside first batch':''}));
  context.records=records;run('projects=records;render()');
  return {get,run,context,timers,records,headers};
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

test('all sort headers have native keyboard buttons and preserve column semantics',()=>{
  const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
  const headers=[...html.matchAll(/<th([^>]*data-key="[^"]+"[^>]*)>(.*?)<\/th>/g)];
  assert.equal(headers.length,11);
  for(const [,attributes,content] of headers){
    assert.match(attributes,/scope="col"/);
    assert.match(content,/^<button type="button" class="sort-heading" aria-label="Sort by [^"]+">[^<]+<\/button>$/);
  }
  // Native Enter/Space activation bubbles a click through the same header handler.
  const x=setup();x.run('projectUiReady=true');
  const source=x.headers.find(header=>header.dataset.key==='source');
  source.listeners.click[0]();assert.equal(x.run('sort.key'), 'source');assert.equal(x.run('sort.dir'),1);assert.equal(source.attributes['aria-sort'],'ascending');
  source.listeners.click[0]();assert.equal(x.run('sort.dir'),-1);assert.equal(source.attributes['aria-sort'],'descending');
  const title=x.headers.find(header=>header.dataset.key==='title');
  title.listeners.click[0]();assert.equal(title.attributes['aria-sort'],'ascending');assert.equal(source.attributes['aria-sort'],'none');
});

test('source-unavailable row marker is an accessible detail button and retains cached facts',()=>{
  const x=setup();
  x.context.unavailable={id:'lost',title:'Cached <project>',repo:'https://github.com/example/lost',last_activity:'2026-09-01',build:{playable:true},github:{source_availability:{status:'unavailable',http_status:404,retryable:true},latest_commit:{url:'https://github.com/example/lost/commit/a',date:'2026-09-01',message:'Cached commit'}}};
  x.run('projects=[unavailable];render()');
  const html=x.get('rows').innerHTML;
  assert.match(html,/class="source-unavailable-marker"[^>]*data-source-details="lost"[^>]*aria-label="Source unavailable at last check for Cached &lt;project&gt;\. View details"/);
  assert.match(html,/Source unavailable<\/span><\/button>/);
  assert.match(html,/2026-09-01/);assert.match(html,/class="flag yes"/);
  x.run('showDetails=record=>{globalThis.opened=record;}');
  const button={dataset:{sourceDetails:'lost'}};let prevented=false;
  x.context.click={target:{closest:selector=>selector==='[data-source-details]'?button:null},preventDefault:()=>{prevented=true;},stopPropagation(){}};
  x.run('sourceDetailsClick(click)');assert.equal(x.context.opened,x.context.unavailable);assert.equal(prevented,true);
});

test('GitLab provider details and started sort use current metadata rather than stale GitHub fields',()=>{
  const x=setup();x.get('details').showModal=()=>{};
  x.context.gitlab={id:'gl',title:'GitLab project',repo:'https://gitlab.com/group/subgroup/project',gitlab:{repository:'gitlab.com/group/subgroup/project',created_at:'2021-04-05',default_branch:'main',tracking_branch:'stable',tracking_path:'src',languages:['C'],activity_state:'active',latest_commit:{url:'https://gitlab.com/group/subgroup/project/-/commit/abc',date:'2026-10-28',message:'GitLab cached commit'},latest_release:{url:'https://gitlab.com/group/subgroup/project/-/releases/v2',tag:'v2',published_at:'2026-10-27'},source_availability:{status:'unavailable',http_status:404,retryable:true}},github:{created_at:'1990-01-01',latest_release:{tag:'old'}}};
  x.run('projects=[gitlab];render();showDetails(gitlab)');
  const details=x.get('detailbody').innerHTML;
  assert.match(details,/GitLab cached commit/);assert.match(details,/releases\/v2/);
  assert.match(details,/<dt>Repository activity<\/dt><dd>active<\/dd>/);
  assert.match(details,/<dt>Repository languages<\/dt>/);assert.doesNotMatch(details,/GitHub activity|GitHub languages/);
  assert.match(details,/last check \(HTTP 404\).*cached metadata retained/);
  assert.equal(x.run('projectMeta(gitlab).keys.started'),'2021-04-05');
  assert.match(x.get('rows').innerHTML,/2021\*/);assert.doesNotMatch(x.get('rows').innerHTML,/1990/);
});

test('GitLab forbidden releases show release-only uncertainty, not a missing or unavailable source',()=>{
  const x=setup();x.get('details').showModal=()=>{};
  x.context.gitlab={id:'gl',title:'GitLab project',repo:'https://gitlab.com/g/p',gitlab:{repository:'gitlab.com/g/p',release_availability:{status:'unavailable',http_status:403,retryable:true,checked_at:'2026-11-04T21:00:00Z'}}};
  x.run('projects=[gitlab];bookmarks.add("gl");render();showDetails(gitlab);updateSourceAvailabilityWarning()');
  const details=x.get('detailbody').innerHTML;
  assert.match(details,/<dt>Latest release<\/dt><dd>Release information unavailable<\/dd>/);
  assert.match(details,/<dt>Release availability<\/dt><dd>Release information unavailable to the tracker \(HTTP 403\)/);
  assert.match(details,/First observed unavailable: 2026-11-04T21:00:00Z/);
  assert.doesNotMatch(details,/Repository unavailable|Source unavailable|[Nn]o releases/);
  assert.doesNotMatch(x.get('rows').innerHTML,/source-unavailable-marker/);
  assert.equal(x.get('sourceAvailabilityWarning').hidden,true);
  assert.equal(x.run('combinedActivityEvents().length'),0);
});

test('forbidden release status is separate from retained cached release details and events',()=>{
  const x=setup();x.get('details').showModal=()=>{};
  x.context.gitlab={id:'gl',title:'GitLab project',repo:'https://gitlab.com/g/p',gitlab:{repository:'gitlab.com/g/p',release_availability:{status:'unavailable',http_status:403,retryable:true},latest_release:{tag:'v1 <cached>',published_at:'2026-10-28',url:'https://gitlab.com/g/p/-/releases/v1'}}};
  x.run('projects=[gitlab];activityData={generated_at:"2026-10-29T00:00:00Z",events:[]};showDetails(gitlab)');
  const details=x.get('detailbody').innerHTML;
  assert.match(details,/<dt>Latest release<\/dt><dd><a href="https:\/\/gitlab.com\/g\/p\/-\/releases\/v1"[^>]*>v1 &lt;cached&gt; — 2026-10-28<\/a><\/dd>/);
  assert.match(details,/<dt>Release availability<\/dt>/);assert.match(details,/Cached release information is retained and may be outdated/);
  assert.equal(x.run('combinedActivityEvents().length'),1);assert.equal(x.run('combinedActivityEvents()[0].tag'),'v1 <cached>');
  x.run('delete gitlab.gitlab.latest_release.url;showDetails(gitlab)');
  assert.match(x.get('detailbody').innerHTML,/<dt>Latest release<\/dt><dd>v1 &lt;cached&gt; — 2026-10-28<\/dd>/);
  x.run('delete gitlab.gitlab.release_availability;showDetails(gitlab)');
  assert.doesNotMatch(x.get('detailbody').innerHTML,/Release availability|Release information unavailable/);
  assert.match(x.get('detailbody').innerHTML,/v1 &lt;cached&gt;/);
});

test('release-only status requires the explicit 403 marker on the current provider',()=>{
  const x=setup();
  for(const status of [{status:'unavailable',http_status:404,retryable:true},{status:'error',http_status:403,retryable:true},{status:'unavailable',http_status:403}]){
    x.context.status=status;assert.equal(x.run('releaseAvailability({gitlab:{release_availability:status}})'),"");
  }
  x.context.status={status:'unavailable',http_status:403,retryable:true,checked_at:'invalid'};
  assert.doesNotMatch(x.run('releaseAvailability({gitlab:{release_availability:status}})'),/First observed/);
  assert.equal(x.run('releaseAvailability({repo:"https://github.com/g/p",gitlab:{release_availability:status}})'),"");
});

test('catalogue links are compact, accessible, subject-specific and safe in both views',()=>{
  const x=setup();
  x.run(`gameLinkIndex={p0:[{subject:'Game <one>',lemon_amiga:'780',lemon64:'1783',moby:'9715'},{subject:'Other',moby:'999'}]}; projects[0].subjects=['Game <one>']; render()`);
  const row=x.get('rows').innerHTML;
  assert.match(row,/lemonamiga\.com\/games\/details\.php\?id=780/);
  assert.match(row,/lemon64\.com\/\?game_id=1783/);
  assert.match(row,/mobygames\.com\/game\/9715\//);
  assert.match(row,/Lemon Amiga for Game &lt;one&gt; \(opens in a new tab\)/);
  assert.match(row,/target="_blank" rel="noopener noreferrer"/);
  assert.doesNotMatch(row,/mobygames\.com\/game\/999/);
  assert.match(x.run('activityProjectHeader(projects[0])'),/lemonamiga\.com\/games\/details/);
  x.run(`gameLinkIndex.p0=[{subject:'Game <one>',moby:'1\\" onmouseover=\\"bad'}]`);
  assert.equal(x.run('projectLinksHtml(projects[0])'),'');
});

test('multi-game references remain compact and expand with named destinations',()=>{
  const x=setup();x.run(`projects[0].subjects=['First','Second','Third'];gameLinkIndex.p0=[{subject:'First',moby:'12'},{subject:'Second',lemon64:'34'},{subject:'Third',moby:'56'}];render()`);
  const html=x.get('rows').innerHTML;
  assert.match(html,/<summary[^>]*>Links /);
  assert.match(html,/<span class="project-link-subject">Second<\/span>.*lemon64\.com\/\?game_id=34/);
  assert.match(html,/<span class="project-link-subject">Third<\/span>.*mobygames\.com\/game\/56\//);
});

test('name controls open current records in both views, with separate safe upstream links',()=>{
  const x=setup();x.run('showDetails=record=>{globalThis.opened=record;}');
  x.context.button={dataset:{openProject:'p0'},closest:()=>null};
  x.context.event={target:{closest:selector=>selector==='[data-open-project]'?x.context.button:null}};
  x.run('projectDetailsClick(event)');assert.equal(x.run('opened.id'),'p0');
  const html=x.run('projectLinksHtml({id:"x",title:"A <B>",repo:"https://example.com/r",project_url:"https://example.com/home"})');
  assert.match(x.run('projectCell({id:"x",title:"A <B>"})'),/>A &lt;B&gt;<\/button>/);
  assert.match(html,/href="https:\/\/example.com\/home"/);assert.match(html,/opens in a new tab/);
  assert.doesNotMatch(x.run('projectCell({id:"x",title:"No link"})'),/project-external/);
});

test('activity name resolves the displayed historical snapshot for its day',()=>{
  const x=setup();x.run('projects=[];showDetails=record=>{globalThis.opened=record;}');
  x.run(`activityRenderedEvents=[{project_id:'gone',date:'2026-10-01T12:00:00Z',project:{id:'gone',title:'First snapshot'}},{project_id:'gone',date:'2026-10-02T12:00:00Z',project:{title:'Second snapshot'}}]`);
  x.context.button={dataset:{openProject:'gone'},closest:selector=>selector==='.activity-day'?{dataset:{day:x.run("localDayKey('2026-10-02T12:00:00Z')")}}:null};
  x.context.event={target:{closest:selector=>selector==='[data-open-project]'?x.context.button:null}};
  x.run('projectDetailsClick(event)');assert.equal(x.run('opened.title'),'Second snapshot');
  x.run(`projects=[{id:'gone',title:'Current'}];projectDetailsClick(event)`);assert.equal(x.run('opened.title'),'Current');
});

test('dialog heading labels the modal and clicking its interior does not dismiss it',()=>{
  const x=setup();let closed=0;
  x.get('details').showModal=()=>{};x.get('details').close=()=>closed++;x.get('details').getBoundingClientRect=()=>({left:10,right:200,top:10,bottom:200});
  x.run('showDetails(projects[0])');assert.equal(x.get('detail-title').textContent,'Project 0');
  const click=x.get('details').listeners.click[0];click({target:x.get('details'),clientX:30,clientY:30});assert.equal(closed,0);
  click({target:x.get('details'),clientX:2,clientY:2});assert.equal(closed,1);
  assert.match(fs.readFileSync(path.join(root,'index.html'),'utf8'),/<dialog id="details" aria-labelledby="detail-title">/);
});

test('correction link preserves identity safely and opens the issue form on GitHub',()=>{
  const x=setup();x.get('details').showModal=()=>{};
  x.context.item={id:'p & 1',title:'Example <game> & more',repo:'https://example.com/project?a=1&b=2'};
  x.run('showDetails(item)');const html=x.get('detailbody').innerHTML;
  assert.match(html,/Suggest correction on GitHub ↗/);
  assert.match(html,/issues\/new\?template=correction.yml&amp;title=Correction%3A%20Example%20%3Cgame%3E%20%26%20more&amp;record-id=p%20%26%201&amp;project-name=Example%20%3Cgame%3E%20%26%20more&amp;project-url=https%3A%2F%2Fexample.com%2Fproject%3Fa%3D1%26b%3D2/);
  assert.match(html,/target="_blank" rel="noopener noreferrer"/);
  assert.match(fs.readFileSync(path.join(root,'index.html'),'utf8'),/issues\/new\/choose[^>]*>Suggest \/ report<\/a>/);
});

test('correction link prefills the fields declared by the issue form',()=>{
  const form=fs.readFileSync(path.join(root,'.github/ISSUE_TEMPLATE/correction.yml'),'utf8');
  for(const id of ['record-id','project-name','project-url'])assert.ok(form.includes('id: '+id));
  for(const file of ['new-project.yml','site-bug.yml','config.yml'])assert.ok(fs.existsSync(path.join(root,'.github/ISSUE_TEMPLATE',file)));
});

test('mobile sort offers every table column and stays synchronized with headings and restored state',()=>{
  const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
  const options=[...html.match(/<select id="projectSort"[\s\S]*?<\/select>/)[0].matchAll(/value="([^"]+)"/g)].map(match=>match[1]);
  const x=setup();x.run('projectUiReady=true');
  assert.deepEqual(options.slice().sort(),x.headers.map(h=>h.dataset.key).sort());
  assert.match(html,/<label for="projectSort">Sort by<\/label>/);
  x.get('projectSort').value='language';x.get('projectSort').listeners.change[0]();
  assert.equal(x.run('sort.key'),'language');assert.equal(x.run('sort.dir'),1);
  const language=x.headers.find(h=>h.dataset.key==='language');
  assert.equal(language.attributes['aria-sort'],'ascending');
  x.get('projectSortDirection').listeners.click[0]();
  assert.equal(x.run('sort.dir'),-1);assert.equal(language.attributes['aria-sort'],'descending');
  assert.equal(x.get('projectSortDirection').attributes['aria-label'],'Sort ascending');
  const updated=x.headers.find(h=>h.dataset.key==='updated');updated.listeners.click[0]();
  assert.equal(x.get('projectSort').value,'updated');assert.equal(x.get('projectSortDirection').textContent,'↑');
  updated.listeners.click[0]();assert.equal(x.get('projectSortDirection').textContent,'↓');
  x.run('sort={key:"source",dir:-1};render()');
  assert.equal(x.get('projectSort').value,'source');assert.equal(x.get('projectSortDirection').textContent,'↓');
  x.get('q').value='nothing matches';x.run('render()');
  x.get('projectSortDirection').listeners.click[0]();
  assert.equal(x.get('count').textContent,0);assert.match(x.get('rows').innerHTML,/No projects/);
});

test('compact rows retain all desktop cells and label only available source and target tags',()=>{
  const x=setup();
  const html=x.run('projectRowHtml({id:"m",title:"Example",source_platforms:["Amiga", "A <B>"],target_platforms:["Windows"],last_activity:"2026-11-05"})');
  assert.equal((html.match(/<td[ >]/g)||[]).length,11);
  assert.equal((html.match(/class="project-secondary"/g)||[]).length,9);
  assert.match(html,/class="project-name"/);assert.match(html,/class="project-updated"/);
  assert.match(html,/project-platform-label">Source<\/span>/);assert.match(html,/project-platform-label">Target<\/span>/);
  assert.match(html,/A &lt;B&gt;/);
  assert.equal(x.run('mobileProjectPlatforms({})'),'');
  const onlyTarget=x.run('mobileProjectPlatforms({target_platforms:["C64"]})');
  assert.match(onlyTarget,/Target/);assert.doesNotMatch(onlyTarget,/Source|\?/);
});

test('short dates retain complete accessible UTC dates and never invent missing precision',()=>{
  const x=setup();
  const html=x.run('projectUpdatedHtml("2026-11-05")');
  assert.match(html,/<time datetime="2026-11-05" title="5 November 2026">/);
  assert.match(html,/project-date-accessible">5 November 2026<\/span>/);
  assert.match(html,/project-date-short" aria-hidden="true">5 Nov 26<\/span>/);
  assert.match(html,/project-date-full" aria-hidden="true">2026-11-05<\/span>/);
  assert.equal(x.run('projectUpdatedHtml(null)'),'?');
  for(const value of ['2026','2026-11','2026-02-30','Unknown'])assert.equal(x.run(`projectUpdatedHtml(${JSON.stringify(value)})`),value);
  assert.equal(x.run('projectUpdatedHtml("<unknown>")'),'&lt;unknown&gt;');
});

test('mobile loading and empty rows span two columns and resize back to eleven',()=>{
  const media={matches:true,addEventListener(event,callback){this.change=callback;}};
  const x=setup({window:{matchMedia:query=>query==='(max-width:760px)'?media:{matches:false,addEventListener(){}}}});
  x.get('q').value='no matching result';x.run('render()');
  assert.match(x.get('rows').innerHTML,/colspan="2"/);
  const statusCell={colSpan:2};x.get('rows').querySelectorAll=()=>[statusCell];
  media.matches=false;media.change();assert.equal(statusCell.colSpan,11);
  x.run('render()');assert.match(x.get('rows').innerHTML,/colspan="11"/);
  media.matches=true;media.change();assert.equal(statusCell.colSpan,2);
});

test('details group all existing fields, reset scroll and safely reuse an open modal',()=>{
  const x=setup();let opened=0;x.get('details').showModal=()=>{opened++;x.get('details').open=true;x.get('detailbody').scrollTop=450;};
  x.context.item={id:'rich',display_title:'Display <title>',title:'Upstream',subjects:['Game'],repo:'https://github.com/team/project',project_url:'https://example.com',status:'In progress',notes:'Line one\nLine two <safe>',re_started:'2020',last_activity:'2026-11-01',last_checked:'2026-11-02',source_platforms:['Amiga'],target_platforms:['Windows'],source_cpu:['m68k'],target_cpu:['x86'],source_language:['Assembly'],reconstructed_languages:['C'],build:{compilable:true,runnable:false,playable:null,byte_exact:true},ai:{usage:true,tools:['Agent'],evidence:['README']},techniques:['Static analysis'],tags:['test'],evidence:{automated:{compilable:[{value:true,url:'https://example.com/build',excerpt:'Build <verified>'}],ai_config:[{value:'Observed',source:'AGENTS.md'}],source_cpu:[{value:'m68k'}]},routine:{target_cpu:[{value:'x86'}]}}};
  x.get('detailbody').scrollTop=600;x.run('showDetails(item)');
  assert.equal(x.get('detail-title').textContent,'Display <title>');assert.equal(x.get('detailbody').scrollTop,0);assert.equal(opened,1);
  const html=x.get('detailbody').innerHTML;
  for(const title of ['Overview','Build &amp; playability','Platforms &amp; languages','Project classification','Repository &amp; activity','Evidence &amp; sources','AI usage'])assert.ok(html.includes('<h3>'+title+'</h3>'));
  for(const label of ['Upstream name','Subjects','Status','Started','Last activity','Notes','Compilable','Runnable','Playable','Byte exact','Source platform','Target platform','CPU family','Source CPU','Target CPU','Original/source language','Reconstructed language','Project type','Software type','Work','Development tool','Legacy type descriptors','Techniques','Tags','Project page','Repository','Last checked','Repository created','Repository activity','Default branch','Tracked branch','Tracked path','Repository languages','Latest commit','Latest release','Compile evidence','Playable evidence','Byte-exact evidence','Start-date evidence','CI signals','source cpu evidence','target cpu evidence','AI usage','AI tools','AI evidence','Agent configuration observations'])assert.ok(html.includes('<dt>'+label+'</dt>'),label);
  assert.match(html,/Line one\nLine two &lt;safe&gt;/);assert.match(html,/Build &lt;verified&gt;/);
  assert.match(html,/<dd class="yes">Yes<\/dd>/);assert.match(html,/<dd class="no">No<\/dd>/);assert.match(html,/<dd class="unknown">Unknown<\/dd>/);
  assert.equal((html.match(/class="details-section details-disclosure"/g)||[]).length,4);
  x.get('detailbody').scrollTop=500;x.run('showDetails({id:"next",title:"Next"})');assert.equal(opened,1);assert.equal(x.get('detailbody').scrollTop,0);assert.equal(x.get('detail-title').textContent,'Next');assert.doesNotMatch(x.get('detailbody').innerHTML,/Line one|AGENTS.md/);
});

test('Links dropdown names destinations, deduplicates website and repository, and rejects unsafe URLs',()=>{
  const x=setup();
  const html=x.run('projectLinksHtml({id:"x",title:"Project <one>",project_url:"https://example.com/home",repo:"https://github.com/team/repo"})');
  assert.match(html,/Links for Project &lt;one&gt;/);assert.match(html,/>Website<\/span>/);assert.match(html,/>GitHub<\/span>/);assert.equal((html.match(/target="_blank" rel="noopener noreferrer"/g)||[]).length,2);
  const same=x.run('projectLinksHtml({id:"x",project_url:"https://gitlab.com/team/repo/",repo:"https://gitlab.com/team/repo"})');
  assert.match(same,/>GitLab<\/span>/);assert.equal((same.match(/<a /g)||[]).length,1);assert.doesNotMatch(same,/>Website</);
  for(const url of ['javascript:alert(1)','data:text/html,bad','https://'])assert.equal(x.run(`projectLinksHtml({repo:${JSON.stringify(url)}})`),'');
  assert.equal(x.run('projectLinksHtml({})'),'');
});

test('Escape closes only the current Links disclosure and returns focus to its summary',()=>{
  const x=setup();let focused=false,prevented=false,stopped=false;
  const disclosure={open:true,querySelector:selector=>{assert.equal(selector,'summary');return {focus(){focused=true;}};}};
  x.context.escape={key:'Escape',target:{closest:()=>disclosure},preventDefault(){prevented=true;},stopPropagation(){stopped=true;}};
  x.run('projectLinksKeydown(escape)');assert.equal(disclosure.open,false);assert.ok(focused&&prevented&&stopped);
  for(const id of ['rows','activityFeed','detailbody'])assert.ok(x.get(id).listeners.keydown.includes(x.run('projectLinksKeydown')));
});

test('popup has a persistent touch-sized close button and responsive independent scroll area',()=>{
  const html=fs.readFileSync(path.join(root,'index.html'),'utf8'),css=fs.readFileSync(path.join(root,'web/tracker.css'),'utf8');
  assert.match(html,/<header class="details-header">[\s\S]*<h2 id="detail-title" tabindex="0"><\/h2>[\s\S]*aria-label="Close details" autofocus[\s\S]*<\/header>\s*<div id="detailbody" class="details-body">/);
  assert.match(css,/#details \.close\{[^}]*width:44px;height:44px/);
  assert.match(css,/\.details-body\{min-height:0;overflow-y:auto;overscroll-behavior:contain/);
  assert.match(css,/@media\(max-width:600px\)/);assert.match(css,/height:calc\(100dvh - 16px\)/);
  assert.match(css,/\.details-grid\{grid-template-columns:minmax\(0,1fr\)/);
});
