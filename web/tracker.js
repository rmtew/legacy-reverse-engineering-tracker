let projects = [];
let sort = { key: "title", dir: 1 };

const $ = id => document.getElementById(id);
const arr = value => Array.isArray(value) ? value : (value === null || value === undefined || value === "" ? [] : [value]);
const text = value => arr(value).join(", ");
const esc = value => String(value ?? "").replace(/[&<>"']/g, char => ({
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#39;"
}[char]));
const tri = value => value === true ? "Yes" : value === false ? "No" : "Unknown";
const projectTitle = record => record?.display_title || record?.title || record?.upstream_name || record?.id || "?";
const upstreamName = record => record?.upstream_name || record?.title || projectTitle(record);

// Published matches are keyed by project and original subject, not repository title.
let gameLinkIndex={};
function gameLinkGroups(record){
  const matches=gameLinkIndex[record?.id];
  if(!Array.isArray(matches))return [];
  const groups=[];
  for(const game of matches){
    if(!game || typeof game.subject!=="string" || !arr(record.subjects).includes(game.subject))continue;
    const links=[];
    for(const [field,label,base] of [
      ["lemon_amiga","Lemon Amiga","https://www.lemonamiga.com/games/details.php?id="],
      ["lemon64","Lemon64","https://www.lemon64.com/?game_id="],
      ["moby","MobyGames","https://www.mobygames.com/game/"]
    ]){
      const id=String(game[field]??"");
      if(!/^[1-9][0-9]*$/.test(id))continue;
      links.push({label,url:base+id+(field==="moby"?"/":"")});
    }
    if(links.length)groups.push({subject:game.subject,links});
  }
  return groups;
}
function projectLinksHtml(record, scope="project"){
  const safeUrl=value=>typeof value==="string" && /^https?:\/\/[^\s/]+(?:[/?#]|$)/i.test(value) ? value : "";
  const repo=safeUrl(record.repo), website=safeUrl(record.project_url);
  const sameUrl=(left,right)=>left.replace(/\/$/,"")===right.replace(/\/$/,"");
  const sourceLabel=/^https?:\/\/(?:www\.)?github\.com(?:[/:]|$)/i.test(repo)?"GitHub"
    :/^https?:\/\/(?:www\.)?gitlab\.com(?:[/:]|$)/i.test(repo)?"GitLab":"Source repository";
  const link=(url,label,subject)=>'<a href="'+esc(url)+'" target="_blank" rel="noopener noreferrer" aria-label="'+esc(label+' for '+subject+' (opens in a new tab)')+'"><span>'+esc(label)+'</span><span aria-hidden="true">↗</span></a>';
  const primary=(website && (!repo || !sameUrl(website,repo))?link(website,"Website",projectTitle(record)):"")
    +(repo?link(repo,sourceLabel,projectTitle(record)):"");
  const groups=gameLinkGroups(record);
  const catalogues=groups.map(group=>'<div class="project-link-group"><span class="project-link-subject">'+esc(group.subject)+'</span>'+group.links.map(item=>link(item.url,item.label,group.subject)).join("")+'</div>').join("");
  if(!primary && !catalogues)return "";
  return '<details class="project-links" name="'+scope+'-links"><summary aria-label="'+esc('Links for '+projectTitle(record))+'">Links <span aria-hidden="true">▾</span></summary><div class="project-links-menu"><p>Opens in a new tab</p>'+primary+catalogues+'</div></details>';
}
function projectLinksKeydown(event){
  if(event.key!=="Escape")return;
  const disclosure=event.target.closest('.project-links[open]');
  if(!disclosure)return;
  event.preventDefault();event.stopPropagation();
  disclosure.open=false;
  disclosure.querySelector('summary').focus();
}

const reading=TrackerReading;
let readingState=reading.empty(), bookmarks=new Set(), inboxView='unread', displayedSnapshotIds=[];
let fetchingUpdates=false, readingInitialized=false, initialRequestsPending=2;
let storageBroken=false;
function storageFailure(message){
  storageBroken=true;
  $('storageWarning').hidden=false;
  $('storageWarning').textContent=message+' Changes are kept for this tab only; export bookmarks before leaving.';
}
try{readingState=reading.parse(localStorage.getItem(reading.KEY));}
catch{storageFailure('Reading storage is unavailable or damaged.');}
try{const raw=localStorage.getItem(reading.BOOKMARKS);if(raw)bookmarks=new Set(reading.parseBookmarks(raw));}
catch{storageFailure('Bookmark storage is unavailable or damaged.');}
function saveReading(){
  if(storageBroken)return;
  try{localStorage.setItem(reading.KEY,JSON.stringify(readingState));}
  catch{storageFailure('Could not save reading progress.');}
}
function latestReading(){
  if(storageBroken)return readingState;
  try{return reading.parse(localStorage.getItem(reading.KEY));}
  catch{storageFailure('Could not read saved progress.');return readingState;}
}
function saveBookmarks(){
  if(storageBroken)return;
  try{localStorage.setItem(reading.BOOKMARKS,JSON.stringify({version:1,project_ids:[...bookmarks].sort()}));}
  catch{storageFailure('Could not save bookmarks.');}
}
function bookmarkButton(project){
  const selected=bookmarks.has(project.id);
  return '<button type="button" class="bookmark-star" data-bookmark="'+esc(project.id)+'" aria-pressed="'+selected+'" aria-label="'+esc((selected?'Remove bookmark for ':'Bookmark ')+projectTitle(project))+'" title="'+(selected?'Remove bookmark':'Bookmark project')+'">'+(selected?'★':'☆')+'</button>';
}
function unreadEvent(event){return reading.ids(event).some(id=>readingState.seen[id]===true);}
function updateReadingControls(message){
  const count=combinedActivityEvents().filter(unreadEvent).length;
  $('unreadCount').textContent=count;
  $('markRead').disabled=fetchingUpdates||!displayedSnapshotIds.some(id=>readingState.seen[id]===true)||!activityVisible();
  $('fetchUpdates').disabled=fetchingUpdates||initialRequestsPending>0;
  $('fetchUpdates').textContent=fetchingUpdates?'Fetching…':'Fetch updates';
  if(message!==undefined)$('readingStatus').textContent=message+(readingState.checked?' Last successful check: '+new Date(readingState.checked).toLocaleString()+'.':'');
}
function captureFilters(){
  const serialize=state=>Object.fromEntries(Object.entries(state).map(([key,value])=>[key,value instanceof Set?[...value]:value]));
  return {project:serialize(projectFilterState),activity:serialize(activityFilterState),q:$('q').value,activityQ:$('activityQ').value,bookmarkedProjects:$('bookmarkedProjects').checked,sort:{...sort}};
}
function restoreFilters(saved){
  if(!saved)return true;
  const short=value=>typeof value==='string'&&value.length<=2000;
  if(!short(saved.q)||!short(saved.activityQ)||typeof saved.bookmarkedProjects!=='boolean')return false;
  const enums={directionMode:['quick','route'],side:['either','source','target'],days:['2','7','30'],ai:['','Yes','No','Unknown'],compilable:['','Yes','No','Unknown'],playable:['','Yes','No','Unknown'],exact:['','Yes','No','Unknown']};
  for(const [name,target] of [['project',projectFilterState],['activity',activityFilterState]]){
    const source=saved[name];if(!source||typeof source!=='object')return false;
    for(const [key,current] of Object.entries(target)){
      const value=source[key];
      if(current instanceof Set){if(!Array.isArray(value)||value.length>500||value.some(v=>!short(v)))return false;}
      else if(typeof value!==typeof current||(typeof value==='string'&&!short(value))||(enums[key]&&!enums[key].includes(value)))return false;
    }
  }
  if(!saved.sort||!['title','source','target','language','classification','started','updated','compilable','playable','exact','ai'].includes(saved.sort.key)||![1,-1].includes(saved.sort.dir))return false;
  for(const [name,target] of [['project',projectFilterState],['activity',activityFilterState]])for(const key of Object.keys(target))target[key]=target[key] instanceof Set?new Set(saved[name][key]):saved[name][key];
  $('q').value=saved.q;$('activityQ').value=saved.activityQ;$('bookmarkedProjects').checked=saved.bookmarkedProjects;sort={...saved.sort};
  $('directionSide').value=projectFilterState.side;$('sameCpuFamily').checked=projectFilterState.sameFamily;$('activityDirectionSide').value=activityFilterState.side;
  return true;
}
function capturePosition(){
  const items=[...document.querySelectorAll(activityVisible()?'[data-reading-anchor]':'#rows [data-id]')];
  const item=items.find(node=>node.getBoundingClientRect().bottom>0);
  return {view:activityVisible()?'activityView':'projects',scope:inboxView,anchor:item?.dataset.readingAnchor||item?.dataset.id||null,offset:item?.getBoundingClientRect().top||0,y:window.scrollY||0,visible:activityVisibleCount,filters:captureFilters()};
}
function restorePosition(position,revision=activityRenderRevision,targetIndex){
  if(!position||revision!==activityRenderRevision)return;
  if(position.view==='activityView'&&position.anchor){
    if(targetIndex===undefined){
      targetIndex=activityRenderedEvents.findIndex(event=>reading.ids(event)[0]===position.anchor);
      // Old saved positions used day/project groups instead of individual event anchors.
      if(targetIndex<0&&position.anchor.startsWith('['))try{
        const [day,projectId]=JSON.parse(position.anchor);
        targetIndex=activityRenderedEvents.findIndex(event=>event.project_id===projectId&&localDayKey(event.date)===day);
        if(targetIndex>=0)position={...position,anchor:reading.ids(activityRenderedEvents[targetIndex])[0]};
      }catch{}
    }
    if(targetIndex>=activityRenderedCount){
      positionRestoreRevision=revision;
      // Restore deep positions in small batches rather than a giant synchronous DOM rebuild.
      setTimeout(()=>{if(revision!==activityRenderRevision)return;renderActivity(true);restorePosition(position,revision,targetIndex);},0);
      return;
    }
  }
  if(position.view==='projects'&&position.anchor&&!ensureProjectAnchorRendered(position.anchor)){
    const projectRevision=projectRenderRevision;
    positionRestoreRevision=revision;
    setTimeout(()=>{if(projectRevision===projectRenderRevision)restorePosition(position,revision);},0);
    return;
  }
  const node=[...document.querySelectorAll(position.view==='projects'?'#rows [data-id]':'[data-reading-anchor]')].find(node=>(node.dataset.readingAnchor||node.dataset.id)===position.anchor);
  positionRestoreRevision=null;
  window.scrollTo?.(0,node?(window.scrollY||0)+node.getBoundingClientRect().top-position.offset:position.y||0);
}

function setInboxView(value){
  inboxView=['all','bookmarks'].includes(value)?value:'unread';
  document.querySelectorAll('[data-inbox]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.inbox===inboxView)));
}
function ingestReadingSnapshot(){
  const result=reading.reconcile(latestReading(),combinedActivityEvents(),activityData.generated_at);
  readingState=result.state;saveReading();
  $('migrationNotice').hidden=!readingState.migrationNotice;
  $('migrationNotice').textContent='Inbox rule updated: available activity has been restored to unread once. The old version could not distinguish automatic read status from your explicit choices. Bookmarks are unchanged; only Mark all read acknowledges activity now.';
  $('historyNotice').hidden=!(result.limited||activityData.events.some(e=>e.type==='daily_commits'&&!e.shas?.length));
  $('historyNotice').textContent=result.limited?'History is limited to the available 30 days. Some unread activity has expired or is no longer available; older content cannot be recovered.':'Some older summaries lack commit identities. They stay unread until explicitly acknowledged; a changed or newly compacted summary may reappear as unread because individual read states cannot be matched.';
  updateReadingControls(result.stale?'This published snapshot is older than your saved check. Saved unread progress is preserved; fetch again shortly.':result.firstVisit?'All available activity starts unread. Only Mark all read acknowledges it; visiting, reloading and fetching do not.':result.added+' new item'+(result.added===1?'':'s')+' found; unread items stay until you mark them read.');
}
$('fetchUpdates').addEventListener('click',()=>fetchUpdates());
$('markRead').addEventListener('click',()=>{
  if(fetchingUpdates)return;
  const captured=[...displayedSnapshotIds];
  readingState=reading.acknowledge(latestReading(),captured);saveReading();$("migrationNotice").hidden=true;
  const position=capturePosition();renderActivity();restorePosition(position);
  updateReadingControls('All activity in this loaded snapshot marked read. Subsequently fetched activity remains unread.');
});
document.querySelectorAll('[data-inbox]').forEach(button=>button.addEventListener('click',()=>{
  setInboxView(button.dataset.inbox);requestActivityRender();
}));
$('bookmarkedProjects').addEventListener('change',()=>{if(projectUiReady)render();});
function syncBookmarkNodes(){
  const map=projectById();
  for(const event of activityRenderedEvents)if(event.project&&!map.has(event.project_id))map.set(event.project_id,event.project);
  document.querySelectorAll('[data-bookmark]').forEach(button=>{
    const id=button.dataset.bookmark,selected=bookmarks.has(id);
    button.textContent=selected?'★':'☆';
    button.setAttribute('aria-pressed',String(selected));
    button.setAttribute('aria-label',(selected?'Remove bookmark for ':'Bookmark ')+projectTitle(map.get(id)||{id}));
    button.title=selected?'Remove bookmark':'Bookmark project';
    button.closest('.activity-project,.project-row')?.classList.toggle('bookmarked',selected);
  });
}
function bookmarkClick(event){
  const button=event.target.closest('[data-bookmark]');if(!button)return;
  event.preventDefault();event.stopPropagation();
  if(!storageBroken)try{const raw=localStorage.getItem(reading.BOOKMARKS);bookmarks=new Set(raw?reading.parseBookmarks(raw):[]);}catch{storageFailure('Could not read bookmarks.');}
  const id=button.dataset.bookmark;
  if(bookmarks.has(id))bookmarks.delete(id);else bookmarks.add(id);
  saveBookmarks();
  if(inboxView==='bookmarks'&&bookmarks.has(id))activityDirty=true;
  // Keep existing nodes (and the focused star) rather than rebuilding either view.
  // Geometry reads in skipped content-visibility groups can themselves move scroll anchoring.
  // Measure a replacement only when this click actually removes the focused visible entry.
  const removingVisible=!bookmarks.has(id)&&(activityVisible()?inboxView==='bookmarks':$('bookmarkedProjects').checked);
  const survivors=removingVisible?[...document.querySelectorAll('.view-panel.active [data-bookmark]')].filter(node=>bookmarks.has(node.dataset.bookmark)):[];
  const anchor=survivors.find(node=>node.getBoundingClientRect().top>=0)||survivors.at(-1);
  const top=anchor?.getBoundingClientRect().top;
  syncBookmarkNodes();
  if(projectUiReady&&$('bookmarkedProjects').checked)refreshProjectBookmarkMembership();
  if(activityUiReady&&inboxView==='bookmarks'){
    activityRenderRevision++;
    const previous=activityRenderedEvents;
    activityRenderedCount=previous.slice(0,activityRenderedCount).filter(event=>bookmarks.has(event.project_id)).length;
    activityVisibleCount=activityRenderedCount;
    activityRenderedEvents=previous.filter(event=>bookmarks.has(event.project_id));
    document.querySelectorAll('#activityFeed .activity-project').forEach(node=>{if(!bookmarks.has(node.dataset.projectId))node.remove();});
    document.querySelectorAll('#activityFeed .activity-day').forEach(node=>{if(!node.querySelector('.activity-project'))node.remove();});
    activityDayNodes=[...document.querySelectorAll('#activityFeed .activity-day')];
    updateActivityCounts();
    if(!activityRenderedEvents.length)$('activityFeed').innerHTML='<div class="activity-empty">No activity matches the current filters.</div>';
  }
  if(activityUiReady&&inboxView==='bookmarks'){
    const indices=new Map(activityRenderedEvents.map((event,index)=>[reading.ids(event)[0],index]));
    const retained=activityTimelineEntries.filter(entry=>bookmarks.has(entry.id)&&indices.get(entry.anchor)<activityRenderedCount);
    activityTimelineEntries=retained.map((entry,index)=>({...entry,index:indices.get(entry.anchor),dayStart:index===0||retained[index-1].day!==entry.day}));
    activityTimelineEntries.push(...activityRailEntries(activityRenderedEvents.slice(activityRenderedCount),projectById()).map(entry=>({...entry,index:entry.index+activityRenderedCount})));
    renderActivityRail();
  }else document.querySelectorAll('#activityRail [data-project-id]').forEach(node=>node.classList.toggle('timeline-bookmarked',bookmarks.has(node.dataset.projectId)));
  if(!button.isConnected){
    if(anchor?.isConnected){window.scrollBy(0,anchor.getBoundingClientRect().top-top);anchor.focus({preventScroll:true});}
    else (activityVisible()?document.querySelector('[data-inbox="bookmarks"]'):$('bookmarkedProjects'))?.focus({preventScroll:true});
  }
  if(inboxView==='bookmarks')updateCurrentActivityDay();
  updateSourceAvailabilityWarning(true);
}
$('rows').addEventListener('click',bookmarkClick);
$('activityFeed').addEventListener('click',bookmarkClick);
$('exportBookmarks').addEventListener('click',()=>{
  const blob=new Blob([JSON.stringify({version:1,project_ids:[...bookmarks].sort()},null,2)],{type:'application/json'});
  const url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download='retro-tracker-bookmarks.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
});
$('importBookmarks').addEventListener('change',async event=>{
  const file=event.target.files?.[0];if(!file)return;
  try{
    if(file.size>2*1024*1024)throw Error('Bookmark file must be under 2 MB.');
    const incoming=reading.parseBookmarks(await file.text());
    if(!storageBroken){const raw=localStorage.getItem(reading.BOOKMARKS);if(raw)bookmarks=new Set(reading.parseBookmarks(raw));}
    incoming.forEach(id=>bookmarks.add(id));saveBookmarks();
    const position=capturePosition();
    if(projectUiReady)render();if(activityUiReady)renderActivity();updateSourceAvailabilityWarning();restorePosition(position);updateReadingControls('Imported bookmarks; existing bookmarks preserved.');
  }catch(error){updateReadingControls('Import failed: '+error.message);}
  finally{event.target.value='';}
});
window.addEventListener?.('storage',event=>{
  if(storageBroken)return;
  const position=readingInitialized?capturePosition():null;
  try{
    if(event.key===reading.KEY){readingState=reading.parse(event.newValue);if(!readingState.checked&&readingInitialized)readingState=reading.reconcile(readingState,combinedActivityEvents(),activityData.generated_at).state;$('migrationNotice').hidden=!readingState.migrationNotice;}
    else if(event.key===reading.BOOKMARKS)bookmarks=new Set(event.newValue?reading.parseBookmarks(event.newValue):[]);
    else return;
    if(projectUiReady)render();if(activityUiReady)renderActivity();updateSourceAvailabilityWarning();restorePosition(position);
    updateReadingControls('Local state updated from another tab.');
  }catch{storageFailure('Another tab saved unreadable local state.');}
});
function persistPosition(){if(!readingInitialized||positionRestoreRevision===activityRenderRevision)return;const position=capturePosition();readingState=latestReading();readingState.position=position;saveReading();}
window.addEventListener?.('pagehide',persistPosition);
for(const event of ['wheel','touchstart','keydown'])window.addEventListener?.(event,()=>{
  if(positionRestoreRevision===activityRenderRevision){activityRenderRevision++;positionRestoreRevision=null;}
},{passive:true});
let scrollSaveTimer;
window.addEventListener?.('scroll',()=>{clearTimeout(scrollSaveTimer);scrollSaveTimer=setTimeout(persistPosition,250);},{passive:true});

const THEME_STORAGE_KEY="retro-development-tracker.theme";
const browserDarkMode=window.matchMedia("(prefers-color-scheme: dark)");
const effectiveTheme = () => {
  const explicit=document.documentElement.dataset.theme;
  if(explicit==="dark"||explicit==="light") return explicit;
  return browserDarkMode.matches?"dark":"light";
};
function updateThemeToggle(){
  const value=effectiveTheme();
  const button=$("themeToggle");
  const label=$("themeToggleLabel");
  const next=value==="dark"?"light":"dark";
  if(label) label.textContent=next==="dark"?"Dark mode":"Light mode";
  if(button){
    const text=next==="dark"?"Switch to dark mode":"Switch to light mode";
    button.setAttribute("aria-label",text);
    button.title=text;
    button.setAttribute("aria-pressed",value==="dark"?"true":"false");
  }
}
function applyManualTheme(theme){
  const value=theme==="dark"?"dark":"light";
  document.documentElement.dataset.theme=value;
  try { localStorage.setItem(THEME_STORAGE_KEY,value); } catch {}
  updateThemeToggle();
}
updateThemeToggle();
browserDarkMode.addEventListener?.("change",()=>{
  if(!document.documentElement.dataset.theme) updateThemeToggle();
});
$("themeToggle").addEventListener("click",()=>{
  applyManualTheme(effectiveTheme()==="dark"?"light":"dark");
});
const flag = value => {
  const label = tri(value);
  return '<span class="flag ' + label.toLowerCase() + '" title="' + label + '">' +
    (label === "Unknown" ? "?" : label) + "</span>";
};
const tags = value => {
  const values = arr(value);
  return values.length
    ? '<span class="tags">' + values.map(item => '<span class="tag">' + esc(item) + "</span>").join("") + "</span>"
    : "?";
};

const classificationLabels = {
  subject:"Retro software", tooling:"Development tools", hybrid:"Retro software + development tools", game:"Game", application:"Application", demo:"Demo",
  "operating-system":"Operating system", "firmware-rom":"Firmware / ROM", "system-software":"System software",
  "game-engine":"Game engine", "game-subsystem":"Game subsystem", "development-tool":"Development tool",
  disassembly:"Disassembly", decompilation:"Decompilation", "source-reconstruction":"Source reconstruction",
  "source-restoration":"Source restoration", "binary-analysis":"Binary analysis", "data-format-analysis":"Data-format analysis",
  "copy-protection-analysis":"Copy-protection analysis", reimplementation:"Reimplementation",
  "reverse-engineering-derived-port":"RE-derived port", patching:"Patching", translation:"Translation",
  "subsystem-reconstruction":"Subsystem reconstruction", emulator:"Emulator", debugger:"Debugger", profiler:"Profiler",
  "graphics-debugger":"Graphics debugger", disassembler:"Disassembler", reassembler:"Reassembler", ide:"IDE",
  "compiler-toolchain":"Compiler/toolchain", "assembler-toolchain":"Assembler/toolchain", "static-analysis":"Static analysis",
  "language-tooling":"Language tooling", "cycle-analysis":"Cycle analysis", "rom-tool":"ROM tool",
  "disk-filesystem-tool":"Disk/filesystem tool", "asset-tool":"Asset tool", automation:"Automation",
  "development-environment":"Development environment"
};
const classificationLabel = value => classificationLabels[value] || String(value ?? "");
const projectTypeLabels = {software:"Retro software",tools:"Development tools"};
const projectTypeLabel = value => projectTypeLabels[value] || value;
const projectTypeValues = record => record?.record_class === "hybrid"
  ? ["software","tools"]
  : record?.record_class === "tooling" ? ["tools"] : ["software"];

const cpuFamily = value => {
  const raw=String(value??"").trim();
  const cpu=raw.toLowerCase().replaceAll(" ","");
  if(!cpu) return "";
  if(/6502|6507|6510|7501|8501|2a03|huc6280|65c0?2|65c12|65c102|65816|6500\/1/.test(cpu)) return "6502 family";
  if(cpu.includes("m68k")||cpu.includes("68000")||cpu.includes("68010")||cpu.includes("68020")||cpu.includes("68030")||cpu.includes("68040")||cpu.includes("68060")) return "68000 family";
  if(/^(?:8086|80186|80286|80386|80486|i[3456]86)$/.test(cpu)||cpu.includes("x86")) return "x86";
  if(cpu.includes("z80")) return "Z80";
  if(cpu.includes("8080")) return "8080";
  if(cpu.includes("6809")) return "6809";
  if(cpu.includes("arm")) return "ARM";
  if(cpu.includes("sh-2")||cpu.includes("sh2")) return "SH-2";
  if(cpu.includes("jaguar")) return "Jaguar GPU/DSP";
  return raw;
};
let platformVocabulary={aliases:{},non_platform_values:[]};
function platformLabel(value){
  const key=String(value||"").trim().toLowerCase();
  if(platformVocabulary.non_platform_values.includes(key)) return "";
  return platformVocabulary.aliases[key]||String(value||"").trim();
}
const platformValues = record => [...new Set([...arr(record?.source_platforms),...arr(record?.target_platforms)].map(platformLabel).filter(Boolean))];
const runtimeProfiles = record => arr(record?.runtime_profiles).filter(profile=>profile&&profile.platform);
const cpuFamilyValues = record => [...new Set([
  ...arr(record?.source_cpu),...arr(record?.target_cpu),
  ...runtimeProfiles(record).flatMap(profile=>[profile.cpu_family,profile.min_cpu])
].map(cpuFamily).filter(Boolean))];
const sourceCpuFamilies = record => [...new Set(arr(record?.source_cpu).map(cpuFamily).filter(Boolean))];
const targetCpuFamilies = record => [...new Set(arr(record?.target_cpu).map(cpuFamily).filter(Boolean))];

const cpuRank = value => {
  const cpu=String(value??"").toUpperCase().replaceAll(" ","").replace(/^M(?=680)/,"");
  const m68k={"68000":0,"68010":1,"68020":2,"68030":3,"68040":4,"68060":5};
  const mos={"6502":0,"65C02":1,"65816":2};
  const x86={"8086":0,"80186":1,"80286":2,"80386":3,"80486":4};
  return m68k[cpu] ?? mos[cpu] ?? x86[cpu] ?? null;
};
const cpuCompatible = (minimum,available) => {
  if(!minimum||!available) return true;
  if(cpuFamily(minimum)!==cpuFamily(available)) return false;
  const minRank=cpuRank(minimum), availableRank=cpuRank(available);
  if(minRank!==null&&availableRank!==null) return minRank<=availableRank;
  return String(minimum).toLowerCase()===String(available).toLowerCase();
};
const formatRam = kib => kib<1024 ? kib+"K" : (kib%1024===0 ? (kib/1024)+"M" : (kib/1024).toFixed(1)+"M");
const classificationValueTags = value => {
  const values = arr(value);
  return values.length ? tags(values.map(classificationLabel)) : "?";
};
const classificationChip = (value,kind,prefix) =>
  '<span class="classification-chip '+kind+'-chip" title="'+esc(prefix+': '+classificationLabel(value))+'">'+esc(classificationLabel(value))+'</span>';

const executionLabels = {
  "baked-emulation":"BAKED EMULATION",
  "native-translation":"Native translation"
};
const executionLabel = value => executionLabels[value] || String(value ?? "");
const executionPaths = record => arr(record?.execution_paths).filter(path=>path?.method);
const executionSearchValues = record => executionPaths(record).flatMap(path=>[executionLabel(path.method),path.method,path.method.replaceAll("-"," "),path.name,path.status,path.notes]);
const executionMethods = record => [...new Set(executionPaths(record).map(path=>path.method))];
// Prefer the current repository's provider, not metadata left from a former host.
const repositoryProvider = record => /^https?:\/\/(?:www\.)?gitlab\.com\//i.test(record?.repo||"") ? "gitlab"
  : /^https?:\/\/(?:www\.)?github\.com\//i.test(record?.repo||"") ? "github"
  : (record?.gitlab?.repository || (record?.gitlab && !record?.github)) ? "gitlab" : "github";
const repositoryMetadata = record => record?.[repositoryProvider(record)] || {};
// A missing release is not an unavailable repository.
const repositoryUnavailable = record => {
  const status=repositoryMetadata(record).source_availability;
  return status?.status === "unavailable" && status.http_status === 404 && status.retryable === true;
};
const repositoryAvailability = record => {
  if(!repositoryUnavailable(record))return "";
  const checkedAt=repositoryMetadata(record).source_availability.checked_at;
  // This public timestamp is the first failed observation, not each retry.
  const observed=typeof checkedAt==="string"&&Number.isFinite(Date.parse(checkedAt))
    ? " First observed unavailable: "+checkedAt+"." : "";
  return "Repository unavailable to the tracker at the last check (HTTP 404); cached metadata retained; retryable."
    +observed+" Checks retry automatically. This does not establish whether the repository is private, moved or deleted.";
};
const unavailableReleaseStatus = status => status?.status === "unavailable" && status.http_status === 403 && status.retryable === true;
const releaseUnavailable = record => unavailableReleaseStatus(repositoryMetadata(record).release_availability);
const releaseAvailability = record => {
  if(!releaseUnavailable(record))return "";
  const metadata=repositoryMetadata(record),checkedAt=metadata.release_availability.checked_at;
  const observed=typeof checkedAt==="string"&&Number.isFinite(Date.parse(checkedAt))
    ? " First observed unavailable: "+checkedAt+"." : "";
  return "Release information unavailable to the tracker (HTTP 403)."
    +(metadata.latest_release?" Cached release information is retained and may be outdated.":" The latest release could not be checked.")
    +observed+" Checks retry automatically.";
};
const sourceAvailabilityMarker = record => repositoryUnavailable(record)
  ? '<button type="button" class="source-unavailable-marker" aria-haspopup="dialog" data-source-details="'+esc(record.id)+'" aria-label="'+esc('Source unavailable at last check for '+projectTitle(record)+'. View details')+'" title="'+esc(repositoryAvailability(record))+'"><span aria-hidden="true">⚠</span><span>Source unavailable</span></button>' : "";
function bookmarkedUnavailableProjects(){
  return projects.filter(project=>bookmarks.has(project.id)&&repositoryUnavailable(project));
}
let sourceAvailabilityWarningKey=null;
function updateSourceAvailabilityWarning(preservePosition=false){
  const affected=bookmarkedUnavailableProjects();
  const key=JSON.stringify(affected.map(project=>[project.id,projectTitle(project)]));
  if(key===sourceAvailabilityWarningKey)return;
  sourceAvailabilityWarningKey=key;
  const warning=$('sourceAvailabilityWarning');
  const summary=affected.length?'Updates may be incomplete for '+affected.length+' bookmarked project'+(affected.length===1?'':'s')+'.':'';
  const list=affected.map(project=>'<li><button type="button" class="source-project-details" aria-haspopup="dialog" data-source-details="'+esc(project.id)+'">'+esc(projectTitle(project))+'</button></li>').join('');
  // Measure only this ordinary flow container, never skipped activity groups. Keep
  // a scrolled feed stationary if a bookmark changes the notice above the viewport.
  const slot=$('sourceAvailabilitySlot');
  const before=preservePosition&&activityVisible()?slot.getBoundingClientRect?.():null;
  const y=window.scrollY||0;
  $('sourceAvailabilitySummary').textContent=summary;
  if($('sourceAvailabilityProjects').innerHTML!==list)$('sourceAvailabilityProjects').innerHTML=list;
  warning.hidden=!affected.length;
  if(before?.top<0){
    const after=slot.getBoundingClientRect();
    if(after.height!==before.height)window.scrollTo?.(0,Math.max(0,y+after.height-before.height));
  }
}
function sourceDetailsClick(event){
  const button=event.target.closest('[data-source-details]');if(!button)return;
  const project=projectById().get(button.dataset.sourceDetails);if(!project)return;
  event.preventDefault();event.stopPropagation();showDetails(project);
}
$('rows').addEventListener('click',sourceDetailsClick);
$('sourceAvailabilityWarning').addEventListener('click',sourceDetailsClick);
const executionBadges = record => executionPaths(record).map(path=>{
  const label=executionLabel(path.method)+(path.status==="partial"?": partial":"");
  const hint=[path.name,path.status,path.notes].filter(Boolean).join(" · ");
  return '<span class="execution-badge" title="'+esc(hint||label)+'">'+esc(label)+'</span>';
}).join("");
const executionPathsHtml = record => executionPaths(record).length
  ? '<ul class="execution-paths">'+executionPaths(record).map(path=>{
      const sources=arr(path.evidence).map(url=>'<a href="'+esc(url)+'" target="_blank" rel="noopener">Source</a>').join(" · ");
      return '<li><strong>'+esc(path.name)+'</strong> · '+esc(executionLabel(path.method))
        +' · '+esc(path.status)+(path.notes?'<br>'+esc(path.notes):"")
        +(sources?'<br>'+sources:"")+'</li>';
    }).join("")+'</ul>' : "?";

const compactToolKinds = record => {
  const values=arr(record.tool_kinds);
  const priority=[
    "development-environment","ide","emulator","debugger","profiler","graphics-debugger",
    "disassembler","reassembler","binary-analysis","compiler-toolchain","assembler-toolchain",
    "static-analysis","language-tooling","cycle-analysis","rom-tool","disk-filesystem-tool",
    "asset-tool","automation"
  ];
  const omit=new Set();
  if(values.includes("development-environment")){
    omit.add("compiler-toolchain");
    omit.add("assembler-toolchain");
  }
  if(values.some(value=>["emulator","debugger","profiler","graphics-debugger","disassembler","reassembler"].includes(value))){
    omit.add("binary-analysis");
    omit.add("automation");
  }
  return priority.filter(value=>values.includes(value)&&!omit.has(value)).slice(0,3);
};

const classificationTags = (record,{compact=false}={}) => {
  const chips=[];
  for(const value of projectTypeValues(record)){
    chips.push('<span class="classification-chip class-chip" title="Project type">'+esc(projectTypeLabel(value))+'</span>');
  }
  if(compact){
    if(projectTypeValues(record).includes("tools")){
      for(const value of compactToolKinds(record)) chips.push(classificationChip(value,"tool","Tool"));
    }else{
      for(const value of arr(record.target_kinds).slice(0,1)) chips.push(classificationChip(value,"target","Software type"));
      for(const value of arr(record.work_kinds).slice(0,2)) chips.push(classificationChip(value,"work","Work"));
    }
  }else{
    for(const value of arr(record.target_kinds)) chips.push(classificationChip(value,"target","Software type"));
    for(const value of arr(record.work_kinds)) chips.push(classificationChip(value,"work","Work"));
    for(const value of arr(record.tool_kinds)) chips.push(classificationChip(value,"tool","Development tool"));
  }
  return chips.length?'<span class="classification-tags'+(compact?' compact-classification':'')+'">'+chips.join("")+"</span>":"?";
};
const classificationSortValue = record => [
  ...projectTypeValues(record).map(projectTypeLabel),
  ...arr(record.target_kinds),...arr(record.work_kinds),...arr(record.tool_kinds)
].filter(Boolean).join(" ");

const projectFilterState = {
  projectType:new Set(), platform:new Set(), targetKind:new Set(), workKind:new Set(), execution:new Set(),
  toolKind:new Set(), cpu:new Set(), language:new Set(),
  directionMode:"quick", side:"either", sourcePlatform:new Set(), sourceCpu:new Set(),
  targetPlatform:new Set(), targetCpu:new Set(), sameFamily:false,
  runsOnCpu:"", runsOnRam:"", runsOnChipset:"",
  ai:"", compilable:"", playable:"", exact:""
};
const activityFilterState = {
  type:new Set(), projectType:new Set(), platform:new Set(), cpu:new Set(), targetKind:new Set(),
  workKind:new Set(), toolKind:new Set(), ai:"", days:"30", directionMode:"quick", side:"either"
};

const sortedUnique = (values,labeler=value=>value) =>
  [...new Set(values.filter(Boolean))].sort((a,b)=>
    String(labeler(a)).localeCompare(String(labeler(b)),undefined,{numeric:true,sensitivity:"base"})
  );
const facetMatch = (selected,values) => !selected.size || arr(values).some(value=>selected.has(value));
const projectSideMatch = (record,side,platform,cpu) =>
  facetMatch(platform,arr(record[side+"_platforms"]).map(platformLabel).filter(Boolean))
  && facetMatch(cpu,side==="source"?sourceCpuFamilies(record):targetCpuFamilies(record));
function projectDirectionMatch(record,state=projectFilterState){
  if(state.directionMode==="route"){
    const source=sourceCpuFamilies(record),target=targetCpuFamilies(record);
    return projectSideMatch(record,"source",state.sourcePlatform,state.sourceCpu)
      && projectSideMatch(record,"target",state.targetPlatform,state.targetCpu)
      && (!state.sameFamily || source.some(value=>target.includes(value)));
  }
  if(!state.platform.size && !state.cpu.size) return true;
  if(state.side==="source" || state.side==="target") return projectSideMatch(record,state.side,state.platform,state.cpu);
  if(!state.platform.size) return facetMatch(state.cpu,cpuFamilyValues(record));
  if(!state.cpu.size) return facetMatch(state.platform,platformValues(record));
  return projectSideMatch(record,"source",state.platform,state.cpu)
    || projectSideMatch(record,"target",state.platform,state.cpu)
    || runtimeProfiles(record).some(profile=>state.platform.has(platformLabel(profile.platform))
      && [profile.cpu_family,profile.min_cpu].some(value=>state.cpu.has(cpuFamily(value))));
}

function bindFacet(containerId,values,selected,labeler,onChange){
  const container=$(containerId);
  container.innerHTML=sortedUnique(values,labeler).map(value=>
    '<button type="button" class="facet-chip'+(selected.has(value)?' selected':'')+'" data-value="'+esc(value)+'" aria-pressed="'+(selected.has(value)?'true':'false')+'">'+esc(labeler(value))+'</button>'
  ).join("");
  container.querySelectorAll(".facet-chip").forEach(button=>button.addEventListener("click",()=>{
    const value=button.dataset.value;
    if(selected.has(value)) selected.delete(value); else selected.add(value);
    button.classList.toggle("selected",selected.has(value));
    button.setAttribute("aria-pressed",selected.has(value)?"true":"false");
    onChange();
  }));
}

const directionPickerKeys={
  quickPlatform:"platform",quickCpu:"cpu",sourcePlatform:"sourcePlatform",
  sourceCpu:"sourceCpu",targetPlatform:"targetPlatform",targetCpu:"targetCpu"
};
const facetPickerBindings=new Map();
let pickerDismissBound=false;
function updatePickerSummary(id){
  const picker=$(id),binding=facetPickerBindings.get(id);
  const selected=binding.state[binding.key],labeler=binding.labeler;
  const values=sortedUnique([...selected],labeler);
  const summary=picker.querySelector("summary");
  summary.textContent=values.length===0?picker.dataset.empty:values.length===1?labeler(values[0]):`${labeler(values[0])} +${values.length-1}`;
  summary.title=values.map(labeler).join(", ")||picker.dataset.empty;
  summary.setAttribute("aria-label",`${picker.dataset.label}: ${values.length?values.map(labeler).join(", "):picker.dataset.empty}`);
  picker.classList.toggle("has-selection",values.length>0);
  picker.querySelectorAll('input[type="checkbox"]').forEach(input=>{input.checked=selected.has(input.value);});
  const chips=$(id+"Selected");
  chips.innerHTML=values.map(value=>'<button type="button" class="facet-chip selected" data-value="'+esc(value)+'" aria-label="Remove '+esc(labeler(value))+'">'+esc(labeler(value))+' ×</button>').join("");
}
function initFacetPicker(id,values,state=projectFilterState,key=directionPickerKeys[id],onChange=()=>{updateClearButtons();render();},labeler=value=>value){
  const picker=$(id),options=picker.querySelector(".picker-options");
  if(!pickerDismissBound){
    pickerDismissBound=true;
    document.addEventListener("click",event=>{
      if(!event.target.closest(".facet-picker")) document.querySelectorAll(".facet-picker[open]").forEach(p=>{p.open=false;});
    });
  }
  facetPickerBindings.set(id,{state,key,onChange,labeler});
  options.innerHTML=sortedUnique(values,labeler).map(value=>
    '<label><input type="checkbox" value="'+esc(value)+'"><span>'+esc(labeler(value))+'</span></label>'
  ).join("");
  if(!picker.dataset.bound){
    picker.dataset.bound="true";
    const chips=document.createElement("div");chips.id=id+"Selected";chips.className="picker-selected";
    picker.insertAdjacentElement("afterend",chips);
    chips.addEventListener("click",event=>{
      const button=event.target.closest("button[data-value]");if(!button)return;
      const binding=facetPickerBindings.get(id);binding.state[binding.key].delete(button.dataset.value);
      updatePickerSummary(id);binding.onChange();
    });
    options.addEventListener("change",event=>{
      if(event.target.tagName!=="INPUT") return;
      const binding=facetPickerBindings.get(id),selected=binding.state[binding.key];
      if(event.target.checked)selected.add(event.target.value);else selected.delete(event.target.value);
      updatePickerSummary(id);binding.onChange();
    });
    picker.querySelector(".picker-search").addEventListener("input",event=>{
      const query=event.target.value.trim().toLowerCase();
      options.querySelectorAll("label").forEach(label=>{label.hidden=!label.textContent.toLowerCase().includes(query);});
    });
    picker.addEventListener("toggle",()=>{
      if(!picker.open)return;
      document.querySelectorAll(".facet-picker[open]").forEach(other=>{if(other!==picker)other.open=false;});
      picker.querySelector(".picker-search").focus();
    });
    picker.addEventListener("keydown",event=>{if(event.key==="Escape"){picker.open=false;picker.querySelector("summary").focus();}});
  }
  updatePickerSummary(id);
}
function clearPicker(id){
  const binding=facetPickerBindings.get(id);if(!binding)return;
  binding.state[binding.key].clear();$(id).open=false;
  $(id).querySelector(".picker-search").value="";
  $(id).querySelectorAll(".picker-options label").forEach(label=>{label.hidden=false;});
  updatePickerSummary(id);
}

function resetDirectionPickers(){
  for(const id of Object.keys(directionPickerKeys)){
    projectFilterState[directionPickerKeys[id]].clear();
    const picker=$(id);
    picker.open=false;
    picker.querySelectorAll('input[type="checkbox"]').forEach(input=>{input.checked=false;});
    const search=picker.querySelector(".picker-search");
    search.value="";
    picker.querySelectorAll(".picker-options label").forEach(label=>{label.hidden=false;});
    updatePickerSummary(id);
  }
  projectFilterState.sameFamily=false;
  $("sameCpuFamily").checked=false;
}
function updateDirectionMode(){
  const route=projectFilterState.directionMode==="route";
  $("quickDirection").hidden=route;
  $("routeDirection").hidden=!route;
  const toggle=$("directionToggle");
  toggle.textContent=route?"Single side":"From → To";
  toggle.setAttribute("aria-pressed",route?"true":"false");
}
function initDirectionFilters(){
  const allPlatform=projects.flatMap(platformValues);
  const allCpu=projects.flatMap(cpuFamilyValues);
  for(const [id,values] of [
    ["quickPlatform",allPlatform],["quickCpu",allCpu],
    ["sourcePlatform",projects.flatMap(record=>arr(record.source_platforms).map(platformLabel))],
    ["sourceCpu",projects.flatMap(sourceCpuFamilies)],
    ["targetPlatform",projects.flatMap(record=>arr(record.target_platforms).map(platformLabel))],
    ["targetCpu",projects.flatMap(targetCpuFamilies)]
  ]) initFacetPicker(id,values);
  $("directionSide").addEventListener("change",event=>{
    projectFilterState.side=event.target.value;
    updateClearButtons();render();
  });
  $("directionToggle").addEventListener("click",()=>{
    resetDirectionPickers();
    projectFilterState.directionMode=projectFilterState.directionMode==="quick"?"route":"quick";
    projectFilterState.side="either";
    $("directionSide").value="either";
    updateDirectionMode();updateClearButtons();render();
  });
  $("sameCpuFamily").addEventListener("change",event=>{
    projectFilterState.sameFamily=event.target.checked;
    updateClearButtons();render();
  });
  updateDirectionMode();
}

function bindChoiceFacet(containerId,values,state,key,labeler,onChange){
  const container=$(containerId);
  const options=sortedUnique(values,labeler);
  container.innerHTML='<button type="button" class="facet-chip choice-chip selected" data-value="" aria-pressed="true">Any</button>'
    +options.map(value=>'<button type="button" class="facet-chip choice-chip" data-value="'+esc(value)+'" aria-pressed="false">'+esc(labeler(value))+'</button>').join("");
  container.querySelectorAll(".choice-chip").forEach(button=>{
    const selected=button.dataset.value===state[key];button.classList.toggle("selected",selected);button.setAttribute("aria-pressed",String(selected));
  });
  container.querySelectorAll(".choice-chip").forEach(button=>button.addEventListener("click",()=>{
    state[key]=button.dataset.value;
    container.querySelectorAll(".choice-chip").forEach(item=>{
      item.classList.toggle("selected",item===button);
      item.setAttribute("aria-pressed",item===button?"true":"false");
    });
    onChange();
  }));
}

function bindSegment(containerId,state,key,onChange){
  const container=$(containerId);
  resetSegment(containerId,state[key]);
  container.querySelectorAll("button").forEach(button=>button.addEventListener("click",()=>{
    state[key]=button.dataset.value;
    container.querySelectorAll("button").forEach(item=>item.classList.toggle("selected",item===button));
    onChange();
  }));
}

function clearFacetSet(set){ set.clear(); }
function clearFacetButtons(scope){
  scope.querySelectorAll(".facet-chip.selected").forEach(button=>{
    button.classList.remove("selected");
    button.setAttribute("aria-pressed","false");
  });
}
function resetSegment(containerId,value=""){
  const container=$(containerId);
  container.querySelectorAll("button").forEach(button=>button.classList.toggle("selected",button.dataset.value===value));
}
function projectFiltersActive(){
  const directional=projectFilterState.directionMode==="route"
    ? ["sourcePlatform","sourceCpu","targetPlatform","targetCpu"].some(key=>projectFilterState[key].size)||projectFilterState.sameFamily
    : projectFilterState.platform.size||projectFilterState.cpu.size;
  return $("q").value.trim() || directional || ["projectType","targetKind","workKind","toolKind","language","execution"].some(key=>projectFilterState[key].size)
    || ["runsOnCpu","runsOnRam","runsOnChipset","ai","compilable","playable","exact"].some(key=>projectFilterState[key]);
}
function activityFiltersActive(){
  return $("activityQ").value.trim() || activityFilterState.days!=="30" || activityFilterState.side!=="either"
    || ["type","projectType","platform","cpu","targetKind","workKind","toolKind"].some(key=>activityFilterState[key].size)
    || activityFilterState.ai;
}
function updateClearButtons(){
  $("clear").hidden=!projectFiltersActive();
  $("activityClear").hidden=!activityFiltersActive();
}

// Derived metadata belongs to a catalogue snapshot, never to a search keystroke.
let projectCacheSource=null, projectCacheVocabulary=null, projectMetadata=new WeakMap();
let projectRowById=new Map(), projectSortOrders=new Map();
const projectCollator=new Intl.Collator(undefined,{numeric:true,sensitivity:"base"});
function projectSearchText(record) {
  return [
    projectTitle(record), record.title, record.upstream_name, ...arr(record.subjects),
    record.notes, record.repo, record.project_url, record.status,
    ...arr(record.tags), ...arr(record.techniques), ...arr(record.types),
    ...projectTypeValues(record).map(projectTypeLabel),
    ...arr(record.target_kinds), ...arr(record.work_kinds), ...arr(record.tool_kinds),
    ...executionSearchValues(record),
    ...platformValues(record),...arr(record.source_platforms),...arr(record.target_platforms),...cpuFamilyValues(record),
    ...arr(record.source_cpu),...arr(record.target_cpu),...arr(record.reconstructed_languages),
    ...runtimeProfiles(record).flatMap(profile=>[
      profile.platform,profile.cpu_family,profile.min_cpu,...arr(profile.chipsets),profile.os,profile.notes
    ])
  ].join(" ").toLowerCase();

}
function projectSortKeys(record) {
  const build = record.build || {};
  const ai = record.ai || {};
  return {
    title: projectTitle(record),
    source: text(record.source_platforms),
    target: text(record.target_platforms),
    language: text(record.reconstructed_languages),
    classification: classificationSortValue(record),
    started: record.re_started ?? repositoryMetadata(record).created_at,
    updated: record.last_activity,
    compilable: tri(build.compilable),
    playable: tri(build.playable),
    exact: tri(build.byte_exact),
    ai: tri(ai.usage)
  };
}

function projectMeta(record){
  let value=projectMetadata.get(record);
  if(!value){
    value={search:projectSearchText(record),keys:projectSortKeys(record)};
    projectMetadata.set(record,value);
  }
  return value;
}
function ensureProjectCache(){
  if(projectCacheSource===projects&&projectCacheVocabulary===platformVocabulary)return;
  projectCacheSource=projects;projectCacheVocabulary=platformVocabulary;
  projectMetadata=new WeakMap();projectSortOrders=new Map();
  projectRowById=new Map(projects.map(record=>[record.id,record]));
  projects.forEach(projectMeta);
}
function sortValue(record,key){return projectMeta(record).keys[key];}
function compare(a,b){
  const av=sortValue(a,sort.key),bv=sortValue(b,sort.key);
  const missing=value=>value===null||value===undefined||value===""||value==="Unknown";
  if(missing(av)!==missing(bv))return missing(av)?1:-1;
  return projectCollator.compare(String(av??""),String(bv??""))*sort.dir;
}
function sortedProjects(){
  ensureProjectCache();
  const key=sort.key+":"+sort.dir;
  if(!projectSortOrders.has(key))projectSortOrders.set(key,projects.slice().sort(compare));
  return projectSortOrders.get(key);
}
function matches(record,query=$("q").value.trim().toLowerCase()) {
  const build=record.build||{},ai=record.ai||{};
  const haystack=query?projectMeta(record).search:"";
  const profiles=runtimeProfiles(record);
  const runtimeRequested=projectFilterState.runsOnCpu||projectFilterState.runsOnRam||projectFilterState.runsOnChipset;
  const runtimePlatform=projectFilterState.directionMode==="route"?projectFilterState.targetPlatform
    :projectFilterState.side==="target"?projectFilterState.platform:new Set();
  const runtimeMatch=!runtimeRequested || profiles.some(profile=>
    (!runtimePlatform.size || runtimePlatform.has(profile.platform))
    && (!projectFilterState.runsOnCpu || (profile.min_cpu && cpuCompatible(profile.min_cpu,projectFilterState.runsOnCpu)))
    && (!projectFilterState.runsOnRam || (Number.isFinite(profile.min_ram_kib) && profile.min_ram_kib<=Number(projectFilterState.runsOnRam)))
    && (!projectFilterState.runsOnChipset || arr(profile.chipsets).includes(projectFilterState.runsOnChipset))
  );

  return (!query || haystack.includes(query))
    && facetMatch(projectFilterState.projectType,projectTypeValues(record))
    && projectDirectionMatch(record)
    && facetMatch(projectFilterState.targetKind,record.target_kinds)
    && facetMatch(projectFilterState.workKind,record.work_kinds)
    && facetMatch(projectFilterState.execution,executionMethods(record))
    && facetMatch(projectFilterState.toolKind,record.tool_kinds)
    && facetMatch(projectFilterState.language,record.reconstructed_languages)
    && runtimeMatch
    && (!projectFilterState.ai || tri(ai.usage)===projectFilterState.ai)
    && (!projectFilterState.compilable || tri(build.compilable)===projectFilterState.compilable)
    && (!projectFilterState.playable || tri(build.playable)===projectFilterState.playable)
    && (!projectFilterState.exact || tri(build.byte_exact)===projectFilterState.exact);
}

function projectCell(record) {
  const shown=projectTitle(record), upstream=upstreamName(record);
  const tooltip=upstream && upstream!==shown?' title="'+esc('Upstream: '+upstream)+'"':'';
  const name='<button type="button" class="project-title" data-open-project="'+esc(record.id)+'" aria-haspopup="dialog" aria-label="'+esc('Details for '+shown)+'"'+tooltip+'>'+esc(shown)+'</button>';
  return name;
}

const PROJECT_BATCH_SIZE=100;
// Keep status rows spanning the visible columns, including during resize/loading.
const compactProjectTable=window.matchMedia("(max-width:760px)");
const projectTableColumnSpan=()=>compactProjectTable.matches?2:11;
function updateProjectStatusColumns(){
  $("rows").querySelectorAll("td[colspan]").forEach(cell=>cell.colSpan=projectTableColumnSpan());
}
compactProjectTable.addEventListener?.("change",updateProjectStatusColumns);
updateProjectStatusColumns();
let projectRenderedRows=[],projectRenderedCount=0,projectVisibleLimit=PROJECT_BATCH_SIZE;
let projectRenderRevision=0;
const projectShortDateFormat=new Intl.DateTimeFormat("en-GB",{day:"numeric",month:"short",year:"2-digit",timeZone:"UTC"});
const projectFullDateFormat=new Intl.DateTimeFormat("en-GB",{day:"numeric",month:"long",year:"numeric",timeZone:"UTC"});
function mobileProjectPlatforms(record){
  const groups=[["Source",record.source_platforms],["Target",record.target_platforms]]
    .filter(([,values])=>arr(values).length)
    .map(([label,values])=>'<div class="project-platform-group"><span class="project-platform-label">'+label+'</span>'+tags(values)+'</div>');
  return groups.length?'<div class="mobile-project-platforms">'+groups.join("")+'</div>':"";
}
function projectUpdatedHtml(value){
  const raw=String(value??"?");
  // Preserve partial/unknown dates as authored, without inventing a day or timezone.
  if(!/^\d{4}-\d{2}-\d{2}$/.test(raw))return esc(raw);
  const date=new Date(raw+"T00:00:00Z");
  if(!Number.isFinite(date.getTime())||date.toISOString().slice(0,10)!==raw)return esc(raw);
  const short=projectShortDateFormat.format(date),full=projectFullDateFormat.format(date);
  return '<time datetime="'+raw+'" title="'+esc(full)+'"><span class="project-date-accessible">'+esc(full)+'</span><span class="project-date-full" aria-hidden="true">'+raw+'</span><span class="project-date-short" aria-hidden="true">'+esc(short)+'</span></time>';
}
function projectRowHtml(record){
    const build = record.build || {};
    const ai = record.ai || {};
    const created=repositoryMetadata(record).created_at;
    const started = record.re_started ?? (created ? created.slice(0, 4) + "*" : "?");

    return '<tr class="project-row '+(bookmarks.has(record.id)?'bookmarked':'')+'" data-id="' + esc(record.id) + '">'
      + '<td class="project-name"><div class="project-name-line">' + projectCell(record) + bookmarkButton(record) + projectLinksHtml(record) + '</div>' + mobileProjectPlatforms(record) + sourceAvailabilityMarker(record) + (executionPaths(record).length?'<div class="execution-badges">'+executionBadges(record)+'</div>':"") + "</td>"
      + '<td class="project-secondary">' + tags(record.source_platforms) + "</td>"
      + '<td class="project-secondary">' + tags(record.target_platforms) + "</td>"
      + '<td class="project-secondary">' + tags(record.reconstructed_languages) + "</td>"
      + '<td class="project-secondary">' + classificationTags(record) + "</td>"
      + '<td class="project-secondary">' + esc(started) + "</td>"
      + '<td class="project-updated">' + projectUpdatedHtml(record.last_activity) + "</td>"
      + '<td class="project-secondary">' + flag(build.compilable) + "</td>"
      + '<td class="project-secondary">' + flag(build.playable) + "</td>"
      + '<td class="project-secondary">' + flag(build.byte_exact) + "</td>"
      + '<td class="project-secondary">' + flag(ai.usage) + "</td>"
      + "</tr>";

}
function updateProjectPageControls(){
  const remaining=projectRenderedRows.length-projectRenderedCount;
  $("projectPageStatus").textContent="Showing "+projectRenderedCount+" of "+projectRenderedRows.length+" matching projects.";
  $("projectShowMore").hidden=remaining<=0;
  $("projectShowMore").textContent="Show "+Math.min(PROJECT_BATCH_SIZE,remaining)+" more";
  $("projectShowAll").hidden=remaining<=0;
  $("projectFindHint").hidden=remaining<=0;
}
function appendProjectRows(limit=projectVisibleLimit){
  const end=Math.min(limit,projectRenderedRows.length);
  if(end>projectRenderedCount){
    $("rows").insertAdjacentHTML("beforeend",projectRenderedRows.slice(projectRenderedCount,end).map(projectRowHtml).join(""));
    projectRenderedCount=end;
  }
  updateProjectPageControls();
}
function render(preserveLimit=false) {
  projectRenderRevision++;
  $("projectShowAll").disabled=false;
  if(!preserveLimit)projectVisibleLimit=PROJECT_BATCH_SIZE;
  const query=$("q").value.trim().toLowerCase(),onlyBookmarks=$("bookmarkedProjects").checked;
  projectRenderedRows=sortedProjects().filter(record=>(!onlyBookmarks||bookmarks.has(record.id))&&matches(record,query));
  projectRenderedCount=0;
  $("count").textContent=projectRenderedRows.length;
  $("total").textContent=projects.length;
  $("sortnote").textContent="Sorted by "+sort.key+(sort.dir<0?" ↓":" ↑");
  $("projectSort").value=sort.key;
  $("projectSortDirection").textContent=sort.dir>0?"↑":"↓";
  const nextDirection=sort.dir>0?"Sort descending":"Sort ascending";
  $("projectSortDirection").setAttribute("aria-label",nextDirection);
  $("projectSortDirection").title=nextDirection;
  document.querySelectorAll("th[data-key]").forEach(th=>{
    th.removeAttribute("data-sort");
    th.setAttribute("aria-sort",th.dataset.key===sort.key?(sort.dir>0?"ascending":"descending"):"none");
    if(th.dataset.key===sort.key)th.dataset.sort=sort.dir>0?"asc":"desc";
  });
  $("rows").innerHTML=projectRenderedRows.length?"":'<tr><td colspan="'+projectTableColumnSpan()+'" class="empty">No projects match the current filters.</td></tr>';
  appendProjectRows();
}
function refreshProjectBookmarkMembership(){
  const query=$("q").value.trim().toLowerCase();
  const next=sortedProjects().filter(record=>bookmarks.has(record.id)&&matches(record,query));
  const previous=new Set(projectRenderedRows);
  if(next.some(record=>!previous.has(record))){render(true);return;}
  projectRenderRevision++;
  $("projectShowAll").disabled=false;
  const retained=new Set(next.map(record=>record.id));
  $("rows").querySelectorAll("tr.project-row").forEach(row=>{
    if(!retained.has(row.dataset.id)){row.remove();projectRenderedCount--;}
  });
  projectRenderedRows=next;
  $("count").textContent=next.length;
  if(!next.length)$("rows").innerHTML='<tr><td colspan="'+projectTableColumnSpan()+'" class="empty">No projects match the current filters.</td></tr>';
  appendProjectRows();
}
function ensureProjectAnchorRendered(id){
  const index=projectRenderedRows.findIndex(record=>record.id===id);
  if(index>=projectRenderedCount){projectVisibleLimit=Math.min(index+1,projectRenderedCount+PROJECT_BATCH_SIZE);appendProjectRows();}
  return index<projectRenderedCount;
}
$("projectShowMore").addEventListener("click",()=>{
  projectVisibleLimit+=PROJECT_BATCH_SIZE;appendProjectRows();
});
$("projectShowAll").addEventListener("click",()=>{
  if($("projectShowAll").disabled)return;
  $("projectShowAll").disabled=true;
  const revision=projectRenderRevision;
  // Explicit full-list access for browser Find/assistive technology, without a long task.
  function next(){
    if(revision!==projectRenderRevision)return;
    projectVisibleLimit+=PROJECT_BATCH_SIZE;appendProjectRows();
    if(projectRenderedCount<projectRenderedRows.length)setTimeout(next,0);
  }
  next();
});
// Append near the end while keeping the explicit button as a keyboard/no-observer fallback.
if(typeof IntersectionObserver!=="undefined"){
  const projectObserver=new IntersectionObserver(entries=>{
    if(entries.some(entry=>entry.isIntersecting)&&projectRenderedCount<projectRenderedRows.length){
      projectVisibleLimit+=PROJECT_BATCH_SIZE;appendProjectRows();
    }
  },{rootMargin:"400px"});
  projectObserver.observe($("projectShowMore"));
}
function projectDetailsClick(event){
  const button=event.target.closest('[data-open-project]');
  if(!button)return;
  const id=button.dataset.openProject;
  const day=button.closest('.activity-day')?.dataset.day;
  const snapshot=day && activityRenderedEvents.find(item=>item.project_id===id && localDayKey(item.date)===day && item.project)?.project;
  const record=projectById().get(id) || (snapshot ? {...snapshot,id} : null);
  if(record)showDetails(record);
}
$("rows").addEventListener("click",projectDetailsClick);
$("activityFeed").addEventListener("click",projectDetailsClick);
for(const id of ["rows","activityFeed","detailbody"]) $(id).addEventListener("keydown",projectLinksKeydown);
$("rows").addEventListener("click",event=>{
  if(event.target.closest("a,button,details,summary"))return;
  const row=event.target.closest("tr.project-row");
  const record=row&&projectRowById.get(row.dataset.id);
  if(record)showDetails(record);
});

function evidenceHtml(entries) {
  const items = arr(entries);
  if (!items.length) return "?";
  return '<ul class="evidence-list">' + items.map(item => {
    const value = item.value === true ? "Yes" : item.value === false ? "No" : item.value;
    const label = '<strong>' + esc(value ?? "?") + '</strong>';
    const excerpt = item.excerpt ? '<span class="evidence-excerpt">“' + esc(item.excerpt) + '”</span>' : "";
    const source = item.url
      ? '<a href="' + esc(item.url) + '" target="_blank" rel="noopener">' + esc(item.source || "source") + '</a>'
      : esc(item.source || "source");
    return '<li>' + label + ' · ' + source + (excerpt ? '<br>' + excerpt : '') + '</li>';
  }).join("") + '</ul>';
}

function runtimeProfilesHtml(record) {
  const profiles=runtimeProfiles(record);
  if(!profiles.length) return "?";
  return '<ul class="evidence-list">'+profiles.map(profile=>{
    const bits=[
      profile.name,profile.platform,
      profile.min_cpu?("CPU ≥ "+profile.min_cpu):null,
      Number.isFinite(profile.min_ram_kib)?("RAM ≥ "+formatRam(profile.min_ram_kib)):null,
      Number.isFinite(profile.min_chip_ram_kib)?("Chip RAM ≥ "+formatRam(profile.min_chip_ram_kib)):null,
      Number.isFinite(profile.min_fast_ram_kib)?("Fast RAM ≥ "+formatRam(profile.min_fast_ram_kib)):null,
      arr(profile.chipsets).length?arr(profile.chipsets).join("/") : null,
      profile.os
    ].filter(Boolean);
    return '<li>'+esc(bits.join(" · "))+(profile.notes?'<br><span class="evidence-excerpt">'+esc(profile.notes)+'</span>':"")+'</li>';
  }).join("")+'</ul>';
}

function ciEvidenceHtml(entries) {
  const items = arr(entries);
  if (!items.length) return "?";
  return '<ul class="evidence-list">' + items.map(item => {
    const title = item.url
      ? '<a href="' + esc(item.url) + '" target="_blank" rel="noopener">' + esc(item.workflow || "workflow") + '</a>'
      : esc(item.workflow || "workflow");
    return '<li>' + title + ' · ' + esc(item.conclusion || "?")
      + (item.completed_at ? ' · ' + esc(item.completed_at) : '') + '</li>';
  }).join("") + '</ul>';
}

function correctionUrl(record){
  const base="https://github.com/rmtew/legacy-reverse-engineering-tracker/issues/new";
  const fields={template:"correction.yml",title:"Correction: "+projectTitle(record),"record-id":record.id || "","project-name":projectTitle(record),"project-url":record.project_url || record.repo || ""};
  return base+"?"+Object.entries(fields).map(([key,value])=>encodeURIComponent(key)+"="+encodeURIComponent(value)).join("&");
}

function showDetails(record) {
  const build = record.build || {};
  const ai = record.ai || {};
  const autoEvidence = record.evidence?.automated || {};
  const missing = '<span class="details-empty">Not recorded</span>';
  const line = (label, value) => "<dt>" + esc(label) + "</dt><dd>" + (value === "?" || value === "" ? missing : value) + "</dd>";
  const section = (title, content, expandable = false) => expandable
    ? '<details class="details-section details-disclosure"><summary><h3>'+esc(title)+'</h3></summary><div class="details-section-content">'+content+'</div></details>'
    : '<section class="details-section"><h3>'+esc(title)+'</h3>'+content+'</section>';
  const grid = content => '<dl class="details-grid">'+content+'</dl>';
  const external = (url, label, className = "") => '<a'+(className?' class="'+className+'"':'')+' href="'+esc(url)+'" target="_blank" rel="noopener noreferrer">'+esc(label)+'</a>';
  const repo = record.repo ? external(record.repo, record.repo) : "?";
  const project = record.project_url ? external(record.project_url, record.project_url) : null;
  const metadata = repositoryMetadata(record);
  const latestCommit = metadata.latest_commit?.url
    ? external(metadata.latest_commit.url, (metadata.latest_commit.date || "?") + " — " + (metadata.latest_commit.message || ""))
    : "?";
  const release = metadata.latest_release;
  const releaseLabel = release ? (release.tag || release.name || "release")+(release.published_at?" — "+release.published_at:"") : "";
  const latestRelease = release
    ? (release.url ? external(release.url, releaseLabel) : esc(releaseLabel))
    : releaseUnavailable(record) ? "Release information unavailable" : "?";
  const shownTitle = projectTitle(record);
  const upstream = upstreamName(record);
  const availability = repositoryAvailability(record);
  const actions = projectLinksHtml(record, "detail");
  const buildSummary = '<dl class="details-build">'+[
    ["Compilable", build.compilable], ["Runnable", build.runnable],
    ["Playable", build.playable], ["Byte exact", build.byte_exact]
  ].map(([label, value])=>'<div><dt>'+label+'</dt><dd class="'+(value===true?'yes':value===false?'no':'unknown')+'">'+tri(value)+'</dd></div>').join("")+'</dl>';
  const platformEvidence = ["source_cpu","target_cpu","source_platforms","target_platforms"].map(field=>{
    const entries = autoEvidence[field]?.length ? autoEvidence[field] : record.evidence?.routine?.[field];
    return entries?.length ? line(field.replaceAll("_"," ")+" evidence",evidenceHtml(entries)) : "";
  }).join("");

  $("detail-title").textContent = shownTitle;
  $("detailbody").innerHTML = (actions ? '<div class="details-actions">'+actions+'</div>' : "")
    + (availability ? '<aside class="details-notice"><strong>Source unavailable at last check</strong><p>'+esc(availability)+'</p></aside>' : "")
    + section("Overview", grid(
      (upstream && upstream !== shownTitle ? line("Upstream name", esc(upstream)) : "")
      + line("Subjects", tags(record.subjects))
      + line("Status", esc(record.status ?? "?"))
      + line("Started", esc(record.re_started ?? "?"))
      + line("Last activity", esc(record.last_activity ?? "?"))
      + line("Notes", '<span class="details-notes">'+(record.notes ? esc(record.notes) : missing)+'</span>')))
    + section("Build & playability", buildSummary)
    + section("Platforms & languages", grid(
      line("Source platform", tags(record.source_platforms))
      + line("Target platform", tags(record.target_platforms))
      + line("CPU family", tags(cpuFamilyValues(record)))
      + line("Source CPU", tags(record.source_cpu))
      + (arr(record.target_cpu).length ? line("Target CPU", tags(record.target_cpu)) : "")
      + (runtimeProfiles(record).length ? line("Runs on", runtimeProfilesHtml(record)) : "")
      + line("Original/source language", tags(record.source_language))
      + line("Reconstructed language", tags(record.reconstructed_languages))))
    + section("Project classification", grid(
      line("Project type", tags(projectTypeValues(record).map(projectTypeLabel)))
      + line("Software type", classificationValueTags(record.target_kinds))
      + line("Work", classificationValueTags(record.work_kinds))
      + (executionPaths(record).length ? line("Execution paths", executionPathsHtml(record)) : "")
      + line("Development tool", classificationValueTags(record.tool_kinds))
      + line("Legacy type descriptors", tags(record.types))
      + line("Techniques", tags(record.techniques))
      + line("Tags", tags(record.tags))), true)
    + section("Repository & activity", grid(
      (project ? line("Project page", project) : "")
      + line("Repository", repo)
      + line("Last checked", esc(record.last_checked ?? "?"))
      + line("Repository created", esc(metadata.created_at ?? "?"))
      + line("Repository activity", esc(metadata.activity_state ?? "?"))
      + line("Default branch", esc(metadata.default_branch ?? "?"))
      + line("Tracked branch", esc(metadata.tracking_branch ?? "?"))
      + line("Tracked path", esc(metadata.tracking_path ?? "?"))
      + line("Repository languages", tags(metadata.languages))
      + line("Latest commit", latestCommit)
      + line("Latest release", latestRelease)
      + (releaseAvailability(record) ? line("Release availability", esc(releaseAvailability(record))) : "")), true)
    + section("Evidence & sources", grid(
      line("Compile evidence", evidenceHtml(autoEvidence.compilable))
      + line("Playable evidence", evidenceHtml(autoEvidence.playable))
      + line("Byte-exact evidence", evidenceHtml(autoEvidence.byte_exact))
      + line("Start-date evidence", evidenceHtml(autoEvidence.re_started))
      + line("CI signals", ciEvidenceHtml(autoEvidence.ci))
      + platformEvidence), true)
    + section("AI usage", grid(
      line("AI usage", tri(ai.usage))
      + line("AI tools", tags(ai.tools))
      + line("AI evidence", tags(ai.evidence))
      + (autoEvidence.ai_config?.length ? line("Agent configuration observations", evidenceHtml(autoEvidence.ai_config)) : "")), true)
    + '<footer class="details-feedback">'+external(correctionUrl(record), "Suggest correction on GitHub ↗")+'</footer>';

  $("detailbody").scrollTop = 0;
  $("details").scrollTop = 0;
  if (!$("details").open) $("details").showModal();
}

function initCompatibilityFilters(){
  const profiles=projects.flatMap(runtimeProfiles);
  const empty=$("compatibilityEmpty");
  const controls=$("compatibilityControls");
  if(!profiles.length){
    empty.hidden=false;
    controls.hidden=true;
    return;
  }
  empty.hidden=true;
  controls.hidden=false;
  bindChoiceFacet("runsOnCpuFacet",profiles.map(profile=>profile.min_cpu).filter(Boolean),projectFilterState,"runsOnCpu",value=>value,()=>{updateClearButtons();render();});
  bindChoiceFacet("runsOnRamFacet",profiles.map(profile=>profile.min_ram_kib).filter(Number.isFinite).map(String),projectFilterState,"runsOnRam",value=>formatRam(Number(value)),()=>{updateClearButtons();render();});
  bindChoiceFacet("runsOnChipsetFacet",profiles.flatMap(profile=>arr(profile.chipsets)),projectFilterState,"runsOnChipset",value=>value,()=>{updateClearButtons();render();});
}

function init() {
  bindFacet("projectTypeFacet",["software","tools"],projectFilterState.projectType,projectTypeLabel,()=>{updateClearButtons();render();});
  initDirectionFilters();
  bindFacet("targetKindFacet",projects.flatMap(record=>arr(record.target_kinds)),projectFilterState.targetKind,classificationLabel,()=>{updateClearButtons();render();});
  bindFacet("workKindFacet",projects.flatMap(record=>arr(record.work_kinds)),projectFilterState.workKind,classificationLabel,()=>{updateClearButtons();render();});
  bindFacet("executionFacet",projects.flatMap(executionMethods),projectFilterState.execution,executionLabel,()=>{updateClearButtons();render();});
  bindFacet("toolKindFacet",projects.flatMap(record=>arr(record.tool_kinds)),projectFilterState.toolKind,classificationLabel,()=>{updateClearButtons();render();});
  bindFacet("languageFacet",projects.flatMap(record=>arr(record.reconstructed_languages)),projectFilterState.language,value=>value,()=>{updateClearButtons();render();});
  bindSegment("aiSegment",projectFilterState,"ai",()=>{updateClearButtons();render();});
  bindSegment("compilableSegment",projectFilterState,"compilable",()=>{updateClearButtons();render();});
  bindSegment("playableSegment",projectFilterState,"playable",()=>{updateClearButtons();render();});
  bindSegment("exactSegment",projectFilterState,"exact",()=>{updateClearButtons();render();});
  initCompatibilityFilters();
  $("total").textContent = projects.length;
  updateClearButtons();
  render();
}

// Each view is initialized when its data and visible panel are ready.

$("q").addEventListener("input",()=>{updateClearButtons();if(projectUiReady) render();});
$("clear").addEventListener("click", () => {
  $("q").value = "";
  for(const key of ["projectType","targetKind","workKind","toolKind","language","execution"]) clearFacetSet(projectFilterState[key]);
  resetDirectionPickers();
  projectFilterState.side="either";
  projectFilterState.directionMode="quick";
  $("directionSide").value="either";
  updateDirectionMode();
  for(const key of ["runsOnCpu","runsOnRam","runsOnChipset","ai","compilable","playable","exact"]) projectFilterState[key]="";
  clearFacetButtons($("projects"));
  for(const id of ["runsOnCpuFacet","runsOnRamFacet","runsOnChipsetFacet"]) {
    const container=$(id);
    if(container) container.querySelectorAll(".choice-chip").forEach(button=>{
      const selected=button.dataset.value==="";
      button.classList.toggle("selected",selected);
      button.setAttribute("aria-pressed",selected?"true":"false");
    });
  }
  for(const id of ["aiSegment","compilableSegment","playableSegment","exactSegment"]) resetSegment(id);
  updateClearButtons();
  if(projectUiReady) render();
});

document.querySelectorAll("th[data-key]").forEach(th => th.addEventListener("click", () => {
  sort = sort.key === th.dataset.key
    ? { key: sort.key, dir: -sort.dir }
    : { key: th.dataset.key, dir: 1 };
  if(projectUiReady) render();
}));
$("projectSort").addEventListener("change",()=>{
  sort={key:$("projectSort").value,dir:sort.dir};
  if(projectUiReady)render();
});
$("projectSortDirection").addEventListener("click",()=>{
  sort={key:sort.key,dir:-sort.dir};
  if(projectUiReady)render();
});

document.querySelector("#details .close").addEventListener("click", () => $("details").close());
$("details").addEventListener("click", event => {
  if(event.target!==$("details"))return;
  const box=$("details").getBoundingClientRect();
  if(event.clientX<box.left||event.clientX>box.right||event.clientY<box.top||event.clientY>box.bottom)$("details").close();
});


let activityData = { generated_at: null, window_days: 30, events: [] };
let activityDirty = true;
const ACTIVITY_PAGE_SIZE=150;
let activityVisibleCount=ACTIVITY_PAGE_SIZE;
let activityRenderedCount=0,activityRenderedEvents=[],activityRenderRevision=0,positionRestoreRevision=null;
const activityVisible = () => $("activityView").classList.contains("active");
const projectById = () => new Map(projects.map(project => [project.id, project]));
const isProjectActivity = event => String(event.type || "").startsWith("project_");
const activityKind = event => isProjectActivity(event) ? "project" : (event.type==="daily_commits" ? "commit" : event.type);
const projectForEvent = (event, map) => map.get(event.project_id) || event.project || null;


function combinedActivityEvents() {
  const events=[...activityData.events];
  const seen=new Set(events.map(event=>event.type+":"+event.project_id+":"+(event.type==="release"?event.tag||event.url||event.date:event.sha||event.tag||event.url||event.date)));
  const snapshotTime=new Date(activityData.generated_at||Date.now()).getTime();
  for(const project of projects){
    const metadata=repositoryMetadata(project),release=metadata.latest_release;
    const releaseTime=Date.parse(release?.published_at);
    if(!Number.isFinite(releaseTime)||releaseTime<snapshotTime-30*86400000||releaseTime>snapshotTime)continue;
    const tag=release.tag||release.name||"release";
    const key="release:"+project.id+":"+tag;
    if(seen.has(key)) continue;
    seen.add(key);
    events.push({
      type:"release",
      // The catalogue records a calendar date, not a release timestamp.
      date:release.published_at,
      project_id:project.id,
      repository:metadata.repository||"",
      tag,
      title:"Release "+tag,
      message:release.name&&release.name!==tag?release.name:"",
      url:release.url||project.project_url||project.repo,
      author:"",
      branches:[]
    });
  }
  return events;
}

function formatFreshness(value) {
  if(!value) return "Data refresh pending";
  const date=new Date(value);
  if(Number.isNaN(date.getTime())) return "Data refreshed "+value;
  return "Data refreshed "+date.toLocaleString(undefined,{dateStyle:"medium",timeStyle:"short"});
}

const activityPickerKeys={activityTypeFacet:"type",activityProjectTypeFacet:"projectType",activityPlatformFacet:"platform",activityCpuFacet:"cpu",activityTargetKindFacet:"targetKind",activityWorkKindFacet:"workKind",activityToolKindFacet:"toolKind"};
function bindActivityProjectFacets(){
  const filterProjects=[...projects,...activityData.events.map(event=>event.project).filter(Boolean)];
  const changed=()=>{updateClearButtons();requestActivityRender();};
  for(const [id,values,labeler] of [
    ["activityTypeFacet",["commit","release","project"],value=>({commit:"Commits",release:"Releases",project:"Project changes"}[value]||value)],
    ["activityProjectTypeFacet",["software","tools"],projectTypeLabel],
    ["activityPlatformFacet",filterProjects.flatMap(platformValues),value=>value],
    ["activityCpuFacet",filterProjects.flatMap(cpuFamilyValues),value=>value],
    ["activityTargetKindFacet",filterProjects.flatMap(p=>arr(p.target_kinds)),classificationLabel],
    ["activityWorkKindFacet",filterProjects.flatMap(p=>arr(p.work_kinds)),classificationLabel],
    ["activityToolKindFacet",filterProjects.flatMap(p=>arr(p.tool_kinds)),classificationLabel]
  ])initFacetPicker(id,values,activityFilterState,activityPickerKeys[id],changed,labeler);
}

function initActivityFilters() {
  bindActivityProjectFacets();
  $("activityDirectionSide").addEventListener("change",event=>{activityFilterState.side=event.target.value;updateClearButtons();requestActivityRender();});
  bindSegment("activityDaysSegment",activityFilterState,"days",()=>{updateClearButtons();requestActivityRender();});
  bindSegment("activityAiSegment",activityFilterState,"ai",()=>{updateClearButtons();requestActivityRender();});
}

function activityMatches(event,map,cutoff,q) {
  const project=projectForEvent(event,map);
  if(!project) return false;
  if(activityEventTime(event.date)<cutoff) return false;
  if(q){
    const hay=[
      event.type,event.title,event.latest_title,event.message,event.repository,event.tag,
      projectTitle(project),project.title,project.upstream_name,...arr(project.subjects),
      ...projectTypeValues(project).map(projectTypeLabel),...platformValues(project),
      ...arr(project.source_platforms),...arr(project.target_platforms),...cpuFamilyValues(project),
      ...arr(project.target_kinds),...arr(project.work_kinds),...arr(project.tool_kinds),
      ...arr(project.tags),...arr(project.ai?.tools),...executionSearchValues(project),
      ...arr(event.changes),JSON.stringify(event.change_details||[])
    ].join(" ").toLowerCase();
    if(!hay.includes(q)) return false;
  }
  return facetMatch(activityFilterState.type,[activityKind(event)])
    && facetMatch(activityFilterState.projectType,projectTypeValues(project))
    && projectDirectionMatch(project,activityFilterState)
    && facetMatch(activityFilterState.targetKind,project.target_kinds)
    && facetMatch(activityFilterState.workKind,project.work_kinds)
    && facetMatch(activityFilterState.toolKind,project.tool_kinds)
    && (!activityFilterState.ai||tri(project.ai?.usage)===activityFilterState.ai);
}

function activityPlatformTags(project) {
  const sources=arr(project.source_platforms);
  const targets=arr(project.target_platforms);
  const same=sources.length===targets.length && sources.every(value=>targets.includes(value));
  const tag=(value,kind,label)=>'<span class="platform-tag '+kind+'" title="'+label+'">'+esc(value)+'</span>';
  if(same){
    return '<div class="activity-platforms">'+sources.map(value=>tag(value,"same-platform","Source and target platform")).join("")+'</div>';
  }
  const source=sources.map(value=>tag(value,"source-platform","Source platform")).join("");
  const target=targets.map(value=>tag(value,"target-platform","Target platform")).join("");
  if(!source&&!target) return "";
  return '<div class="activity-platforms">'+source+(source&&target?'<span class="platform-arrow" aria-hidden="true">→</span>':"")+target+'</div>';
}

function activityProjectHeader(project) {
  return '<div class="project-name-line">'+projectCell(project)+bookmarkButton(project)+projectLinksHtml(project)+'</div>'+activityPlatformTags(project)+classificationTags(project,{compact:true})
    +(executionPaths(project).length?'<div class="execution-badges">'+executionBadges(project)+'</div>':"");
}

const activityFieldLabels={
  title:"Legacy title",
  upstream_name:"Upstream name",
  display_title:"Display title",
  subjects:"Subject",
  repo:"Repository",
  project_url:"Project page",
  github_path:"Tracked path",
  github_branch:"Tracked branch",
  gitlab_path:"Tracked path",
  gitlab_branch:"Tracked branch",
  source_platforms:"Source platform",
  target_platforms:"Target platform",
  source_cpu:"Source CPU",
  source_language:"Source language",
  reconstructed_languages:"Output language",
  target_cpu:"Target CPU",
  runtime_profiles:"Runtime compatibility",
  execution_paths:"Execution paths",
  record_class:"Project type",
  target_kinds:"Target kind",
  work_kinds:"Work kind",
  tool_kinds:"Tool kind",
  types:"Legacy type",
  re_started:"RE start date",
  status:"Status",
  techniques:"Technique",
  tags:"Tag",
  notes:"Project notes"
};

function legacyChangeValue(value) {
  const textValue=String(value??"").trim();
  if(textValue==="unknown") return null;
  if(textValue==="none") return [];
  if(textValue==="True") return true;
  if(textValue==="False") return false;
  try { return JSON.parse(textValue); } catch { return textValue; }
}

function projectChangeDetails(event) {
  if(Array.isArray(event.change_details) && event.change_details.length) return event.change_details;
  if(!event.message || !Array.isArray(event.changes)) return [];

  const pieces=event.message.split("; ");
  return event.changes.flatMap(field=>{
    const prefix=field.replaceAll("_"," ")+": ";
    const piece=pieces.find(item=>item.startsWith(prefix));
    if(!piece) return [];
    const transition=piece.slice(prefix.length);
    const splitAt=transition.indexOf(" → ");
    if(splitAt<0) return [];
    return [{
      field,
      before:legacyChangeValue(transition.slice(0,splitAt)),
      after:legacyChangeValue(transition.slice(splitAt+3))
    }];
  });
}

function activityValue(value) {
  if(value===null || value===undefined || value==="") return "Unknown";
  if(value===true) return "Yes";
  if(value===false) return "No";
  if(Array.isArray(value)) return value.length?value.join(", "):"None";
  return String(value);
}

function listDelta(before,after) {
  const oldValues=arr(before).map(String);
  const newValues=arr(after).map(String);
  return {
    added:newValues.filter(value=>!oldValues.includes(value)),
    removed:oldValues.filter(value=>!newValues.includes(value))
  };
}

function humanizeProjectChange(detail) {
  const field=detail.field;
  const before=detail.before;
  const after=detail.after;

  if(field==="ai"){
    const oldAi=before||{}, newAi=after||{};
    const tools=listDelta(oldAi.tools||[],newAi.tools||[]);
    if(oldAi.usage!==true && newAi.usage===true){
      return [{
        label:"AI usage detected",
        value:tools.added.join(", ") || arr(newAi.tools).join(", ")
      }];
    }
    const lines=[];
    if(oldAi.usage!==newAi.usage){
      lines.push({label:"AI usage changed",value:activityValue(oldAi.usage)+" → "+activityValue(newAi.usage)});
    }
    if(tools.added.length) lines.push({label:tools.added.length===1?"AI tool added":"AI tools added",value:tools.added.join(", ")});
    if(tools.removed.length) lines.push({label:tools.removed.length===1?"AI tool removed":"AI tools removed",value:tools.removed.join(", ")});
    return lines;
  }

  if(field==="build"){
    const oldBuild=before||{}, newBuild=after||{};
    const labels={
      compilable:"Compilable status",
      runnable:"Runnable status",
      playable:"Playable status",
      byte_exact:"Byte-exact build"
    };
    const lines=[];
    for(const key of Object.keys(labels)){
      if(oldBuild[key]===newBuild[key]) continue;
      if(newBuild[key]===true && oldBuild[key]!==true){
        lines.push({label:labels[key]+" confirmed",value:""});
      }else{
        lines.push({label:labels[key]+" changed",value:activityValue(oldBuild[key])+" → "+activityValue(newBuild[key])});
      }
    }
    return lines;
  }

  const listFields=new Set([
    "subjects","source_platforms","target_platforms","source_cpu","target_cpu","source_language",
    "reconstructed_languages","target_kinds","work_kinds","tool_kinds",
    "types","techniques","tags"
  ]);
  if(listFields.has(field)){
    const delta=listDelta(before,after);
    const label=activityFieldLabels[field]||field.replaceAll("_"," ");
    const lines=[];
    if(delta.added.length) lines.push({label:label+(delta.added.length===1?" added":"s added"),value:delta.added.join(", ")});
    if(delta.removed.length) lines.push({label:label+(delta.removed.length===1?" removed":"s removed"),value:delta.removed.join(", ")});
    return lines.length?lines:[{label:label+" changed",value:activityValue(before)+" → "+activityValue(after)}];
  }

  if(field==="runtime_profiles"){
    return [{label:"Runtime compatibility updated",value:""}];
  }
  if(field==="execution_paths"){
    const names=arr(after).map(path=>executionLabel(path.method)+(path.status==="partial"?" (partial)":""));
    return [{label:"Execution paths updated",value:names.join(", ")||"Unknown"}];
  }
  if(field==="record_class"){
    const toTypes=value=>value==="hybrid"?["Retro software","Development tools"]:
      value==="tooling"?["Development tools"]:["Retro software"];
    return [{label:"Project type changed",value:toTypes(before).join(" + ")+" → "+toTypes(after).join(" + ")}];
  }
  if(field==="title"){
    return [{label:"Project renamed",value:activityValue(before)+" → "+activityValue(after)}];
  }
  if(field==="re_started" && (before===null || before===undefined || before==="")){
    return [{label:"RE start date identified",value:activityValue(after)}];
  }
  if(field==="notes"){
    return [{label:"Project notes updated",value:""}];
  }

  const label=activityFieldLabels[field]||field.replaceAll("_"," ");
  return [{label:label+" changed",value:activityValue(before)+" → "+activityValue(after)}];
}

function activityDate(value) {
  if(!value) return "";
  const [year,month,day]=String(value).slice(0,10).split("-").map(Number);
  return new Date(year,month-1,day).toLocaleDateString(undefined,{day:"numeric",month:"short",year:"numeric"});
}

function additionContextHtml(event, project) {
  if(!["project_added","project_restored"].includes(event.type)) return "";
  const context=event.activity_context;
  const metadata=repositoryMetadata(project);
  const commit=context?.last_commit || metadata.latest_commit;
  const lastActivity=context?.last_activity || project?.last_activity;
  const release=context?.latest_release || (!context && metadata.latest_release);
  const lines=[];
  const entry=(label,value,url)=>'<div class="activity-change-line"><span class="activity-change-label">'+label+'</span>'+
    '<span class="detail-separator">·</span>'+(url?'<a href="'+esc(url)+'" target="_blank" rel="noopener">'+esc(value)+'</a>':esc(value))+'</div>';
  if(commit?.date) lines.push(entry("Last commit",activityDate(commit.date),commit.url));
  else if(lastActivity) lines.push(entry("Last upstream activity",activityDate(lastActivity)));
  else if(context){
    const unavailable=context.last_commit_lookup==="unavailable" || metadata.latest_commit_lookup==="unavailable";
    lines.push(entry("Last commit",unavailable?"None found on tracked branch/path":"Historical lookup pending"));
  }
  if(release?.published_at) lines.push(entry("Latest release",(release.tag||release.name||"Release")+" · "+activityDate(release.published_at),release.url));
  // Frozen addition context owns its release status; today's status must not
  // rewrite what was known at addition, or imply that a failed lookup found none.
  const releaseStatus=context?context.release_availability:metadata.release_availability;
  if(unavailableReleaseStatus(releaseStatus))lines.push(entry("Release information",
    (context?"Unavailable to the tracker at addition (HTTP 403)":"Unavailable to the tracker (HTTP 403)")
    +(release?"; cached release retained":"")));
  if(context){
    const count=context.commits??context.commits_90d??0;
    const days=context.active_days??context.active_days_90d??0;
    const window=context.window_days||("commits_90d" in context?90:30);
    lines.push(entry("At addition ("+window+"-day window)",count+" commit"+(count===1?"":"s")+" across "+days+" active day"+(days===1?"":"s")));
  }else{
    const trackedRepo=metadata.repository || /^https?:\/\/(?:www\.)?(?:github|gitlab)\.com\//i.test(project?.repo||"");
    lines.push(entry("Activity", trackedRepo?"Initial scan pending":"Repository activity unavailable"));
  }
  return lines.join("");
}

function projectChangeHtml(event, project) {
  if(event.type==="project_added" || event.type==="project_restored"){
    return additionContextHtml(event,project);
  }
  const lines=projectChangeDetails(event).flatMap(humanizeProjectChange);
  if(!lines.length){
    return event.message?'<div class="activity-change-line">'+esc(event.message)+'</div>':"";
  }
  return lines.map(line=>
    '<div class="activity-change-line"><span class="activity-change-label">'+esc(line.label)+'</span>'
    +(line.value?'<span class="detail-separator">·</span><span>'+esc(line.value)+'</span>':"")
    +'</div>'
  ).join("");
}

function localDayKey(value) {
  if(/^\d{4}-\d{2}-\d{2}$/.test(value)) return value;
  const date=new Date(value);
  if(Number.isNaN(date.getTime())) return String(value||"").slice(0,10);
  return [
    date.getFullYear(),
    String(date.getMonth()+1).padStart(2,"0"),
    String(date.getDate()).padStart(2,"0")
  ].join("-");
}

function activityEventTime(value) {
  if(/^\d{4}-\d{2}-\d{2}$/.test(value)) {
    const [year,month,day]=value.split("-").map(Number);
    return new Date(year,month-1,day).getTime();
  }
  return new Date(value).getTime();
}

function localDayLabel(day) {
  const [year,month,date]=day.split("-").map(Number);
  return new Date(year,month-1,date).toLocaleDateString(
    undefined,
    {weekday:"long",year:"numeric",month:"long",day:"numeric"}
  );
}

// Match the actual paged day/project grouping, not interleaved commit timestamps.
function activityRailEntries(events,map){
  const entries=[],labels=new Map();
  for(let start=0;start<events.length;start+=ACTIVITY_PAGE_SIZE){
    const days=new Map();
    events.slice(start,start+ACTIVITY_PAGE_SIZE).forEach((event,offset)=>{
      const day=localDayKey(event.date);
      if(!days.has(day))days.set(day,new Map());
      const groups=days.get(day);
      if(!groups.has(event.project_id))groups.set(event.project_id,{day,id:event.project_id,index:start+offset,anchor:reading.ids(event)[0],project:map.get(event.project_id)||event.project});
    });
    for(const [day,groups] of days){
      if(!labels.has(day))labels.set(day,localDayLabel(day));
      for(const [position,group] of [...groups.values()].entries())entries.push({...group,dayStart:position===0,label:projectTitle(group.project||{id:group.id})+' · '+labels.get(day)});
    }
  }
  return entries;
}
let activityTimelineEntries=[],timelineDayIndices=new Map(),timelineFocusIndex=0,timelineWindowStart=-1,timelineWindowEnd=-1;
let currentActivityDay='',timelinePointerInside=false;
const TIMELINE_ROW_HEIGHT=24;
function timelineWindowRange(length,scrollTop,height){
  const start=Math.max(0,Math.min(Math.max(0,length-1),Math.floor(scrollTop/TIMELINE_ROW_HEIGHT)-6));
  return [start,Math.min(length,start+Math.min(64,Math.ceil((height||480)/TIMELINE_ROW_HEIGHT)+12))];
}
function renderTimelineWindow(force=false,restoreFocus=true){
  const track=$('activityRail').querySelector('.timeline-marks'),body=track?.querySelector('.timeline-window');
  if(!body)return;
  const [start,end]=timelineWindowRange(activityTimelineEntries.length,track.scrollTop,track.clientHeight);
  if(!force&&start===timelineWindowStart&&end===timelineWindowEnd)return;
  timelineWindowStart=start;timelineWindowEnd=end;
  const focused=document.activeElement?.dataset?.railIndex;
  const tabIndex=Math.max(start,Math.min(end-1,timelineFocusIndex));
  body.innerHTML=activityTimelineEntries.slice(start,end).map((entry,offset)=>{
    const index=start+offset,current=entry.day===currentActivityDay;
    return '<button type="button" class="timeline-mark'+(entry.dayStart?' timeline-day':'')+(bookmarks.has(entry.id)?' timeline-bookmarked':'')+(current?' timeline-current':'')+'" style="top:'+index*TIMELINE_ROW_HEIGHT+'px" tabindex="'+(index===tabIndex?'0':'-1')+'" data-rail-index="'+index+'" data-timeline-index="'+entry.index+'" data-project-id="'+esc(entry.id)+'" data-day="'+esc(entry.day)+'"'+(current&&Math.max(start,timelineDayIndices.get(entry.day))===index?' aria-current="location"':'')+' title="'+esc(entry.label)+'" aria-label="'+esc('Jump to '+entry.label)+'"><span class="timeline-notch" aria-hidden="true"></span>'+(entry.dayStart?'<span class="timeline-day-label" aria-hidden="true">'+esc(entry.day.slice(5))+'</span>':'')+'</button>';
  }).join('');
  if(restoreFocus&&focused!==undefined)body.querySelector('[data-rail-index="'+Math.max(start,Math.min(end-1,Number(focused)))+'"]')?.focus({preventScroll:true});
}
function renderActivityRail(){
  const rail=$('activityRail'),events=activityRenderedEvents;
  rail.hidden=!events.length;
  if(!events.length){rail.innerHTML='';return;}
  timelineDayIndices=new Map();
  activityTimelineEntries.forEach((entry,index)=>{if(!timelineDayIndices.has(entry.day))timelineDayIndices.set(entry.day,index);});
  timelineFocusIndex=Math.min(timelineFocusIndex,activityTimelineEntries.length-1);
  const scroll=rail.querySelector('.timeline-marks')?.scrollTop||0;
  const options=[...timelineDayIndices].map(([day,index])=>'<option value="'+index+'">'+esc(day)+'</option>').join('');
  rail.innerHTML='<time id="timelineCurrentDay" class="timeline-current-date"></time><span class="timeline-boundary">'+esc(localDayKey(events[0].date))+'<br>to '+esc(localDayKey(events.at(-1).date))+'</span><select class="timeline-day-jump" aria-label="Jump to activity day">'+options+'</select><div class="timeline-marks" aria-label="Project entries; use arrow keys, Home and End"><div class="timeline-window" style="height:'+activityTimelineEntries.length*TIMELINE_ROW_HEIGHT+'px"></div></div>';
  const track=rail.querySelector('.timeline-marks');
  track.scrollTop=scroll;
  track.addEventListener('scroll',()=>renderTimelineWindow(),{passive:true});
  highlightActivityDay(timelineDayIndices.has(currentActivityDay)?currentActivityDay:localDayKey(events[0].date));
  renderTimelineWindow(true);
}
function revealTimelineIndex(index,restoreFocus=true){
  const track=$('activityRail').querySelector('.timeline-marks');
  if(!track)return;
  const top=index*TIMELINE_ROW_HEIGHT,bottom=top+TIMELINE_ROW_HEIGHT;
  if(top<track.scrollTop)track.scrollTop=top;
  else if(bottom>track.scrollTop+track.clientHeight)track.scrollTop=bottom-track.clientHeight;
  renderTimelineWindow(false,restoreFocus);
}
function revealCurrentTimelineDay(){
  const rail=$('activityRail'),index=timelineDayIndices.get(currentActivityDay);
  if(index===undefined||timelinePointerInside||rail.contains(document.activeElement))return;
  revealTimelineIndex(index);
}
$('activityRail').addEventListener('pointerenter',()=>{timelinePointerInside=true;});
$('activityRail').addEventListener('pointerleave',()=>{timelinePointerInside=false;});
function highlightActivityDay(day=currentActivityDay,reveal=false){
  currentActivityDay=day;
  const label=$('timelineCurrentDay');
  if(label){label.textContent=day;label.setAttribute('datetime',day);label.title='Currently reading '+(day?localDayLabel(day):'');}
  const select=$('activityRail').querySelector('.timeline-day-jump');
  if(select&&timelineDayIndices.has(day))select.value=String(timelineDayIndices.get(day));
  let announced=false;
  document.querySelectorAll('#activityRail [data-day]').forEach(node=>{
    const current=node.dataset.day===day;
    node.classList.toggle('timeline-current',current);
    if(current&&!announced){node.setAttribute('aria-current','location');announced=true;}else node.removeAttribute('aria-current');
  });
  if(reveal)revealCurrentTimelineDay();
}
function focusTimelineIndex(index){
  timelineFocusIndex=Math.max(0,Math.min(activityTimelineEntries.length-1,index));
  // Focus only the final destination: transient overscan buttons must not become anchors.
  revealTimelineIndex(timelineFocusIndex,false);
  renderTimelineWindow(true,false);
  $('activityRail').querySelector('[data-rail-index="'+timelineFocusIndex+'"]')?.focus({preventScroll:true});
}
$('activityRail').addEventListener('keydown',event=>{
  const button=event.target.closest('[data-rail-index]');
  if(!button)return;
  const index=Number(button.dataset.railIndex),last=activityTimelineEntries.length-1;
  const targets={ArrowDown:index+1,ArrowUp:index-1,Home:0,End:last,PageDown:index+10,PageUp:index-10};
  if(event.key in targets){event.preventDefault();focusTimelineIndex(targets[event.key]);}
});
$('activityRail').addEventListener('change',event=>{
  if(!event.target.matches('.timeline-day-jump'))return;
  const index=Number(event.target.value),entry=activityTimelineEntries[index];
  if(entry){timelineFocusIndex=index;revealTimelineIndex(index);navigateActivity(entry.index);}
});
// Read the actual viewport, rather than only the observer entries that changed.
// This also works in browsers without IntersectionObserver and in either scroll direction.
let activityDayNodes=[],activityDayFramePending=false;
function updateCurrentActivityDay(){
  if(!activityVisible()||!activityDayNodes.length)return;
  let low=0,high=activityDayNodes.length-1;
  while(low<high){
    const middle=Math.floor((low+high)/2);
    if(activityDayNodes[middle].getBoundingClientRect().bottom<=32)low=middle+1;else high=middle;
  }
  const day=activityDayNodes[low].dataset.day;
  if(day&&day!==currentActivityDay)highlightActivityDay(day,true);
  else revealCurrentTimelineDay();
}
function scheduleActivityDayUpdate(){
  if(activityDayFramePending)return;
  activityDayFramePending=true;
  const run=()=>{activityDayFramePending=false;updateCurrentActivityDay();};
  if(window.requestAnimationFrame)window.requestAnimationFrame(run);else setTimeout(run,16);
}
window.addEventListener?.('scroll',scheduleActivityDayUpdate,{passive:true});
window.addEventListener?.('resize',scheduleActivityDayUpdate,{passive:true});
let activityNavigationRequest=0;
function navigateActivity(index,revision=activityRenderRevision,request=++activityNavigationRequest){
  if(request!==activityNavigationRequest||revision!==activityRenderRevision||!activityRenderedEvents[index])return;
  if(index>=activityRenderedCount){renderActivity(true);setTimeout(()=>navigateActivity(index,revision,request),0);return;}
  const anchor=reading.ids(activityRenderedEvents[index])[0];
  const node=[...document.querySelectorAll('#activityFeed [data-reading-anchor]')].find(node=>node.dataset.readingAnchor===anchor)?.closest('.activity-project');
  if(node){node.scrollIntoView({block:'start'});node.focus({preventScroll:true});highlightActivityDay(localDayKey(activityRenderedEvents[index].date));}
}
$('activityRail').addEventListener('click',event=>{
  const button=event.target.closest('[data-timeline-index]');
  if(button)navigateActivity(Number(button.dataset.timelineIndex));
});
function updateActivityCounts(){
  const events=activityRenderedEvents,shown=activityRenderedCount;
  $('activityCount').textContent=events.length;
  $('activityProjectCount').textContent=new Set(events.map(event=>event.project_id)).size;
  $('activityMore').hidden=shown===events.length||typeof IntersectionObserver!=='undefined';
  $('activitySentinel').hidden=shown===events.length;
  $('activitySentinel').textContent=`${shown} of ${events.length} displayed. More loads as you scroll.`;
  $('activityMore').textContent=`Show more (${shown} of ${events.length})`;
}

function renderActivity(append=false) {
  if(!append)updateSourceAvailabilityWarning();
  activityDirty=false;
  const map=projectById();
  const cutoff=inboxView==="unread"?-Infinity:Date.now()-Number(activityFilterState.days||30)*86400000;
  const query=$("activityQ").value.trim().toLowerCase();
  if(!append)activityRenderRevision++;
  const events=append?activityRenderedEvents:combinedActivityEvents().filter(event=>(inboxView!=="unread"||unreadEvent(event))&&(inboxView!=="bookmarks"||bookmarks.has(event.project_id))&&activityMatches(event,map,cutoff,query)).sort((a,b)=>activityEventTime(b.date)-activityEventTime(a.date));
  activityRenderedEvents=events;
  if(!append)activityTimelineEntries=activityRailEntries(events,map);
  const start=append?activityRenderedCount:0;
  const shown=Math.min(start+ACTIVITY_PAGE_SIZE,events.length);
  activityRenderedCount=shown;activityVisibleCount=shown;
  if(!append){
    displayedSnapshotIds=combinedActivityEvents().flatMap(reading.ids);
    updateReadingControls();
  }
  updateActivityCounts();


  if(!events.length){
    activityDayNodes=[];
    renderActivityRail();
    $("activityFeed").innerHTML='<div class="activity-empty">'+(inboxView==='unread'?'No unread activity matches. Fetch updates to check for more, or browse All activity.':'No activity matches the current filters.')+'</div>';
    return;
  }

  const days=new Map();
  for(const event of events.slice(start,shown)){
    const day=localDayKey(event.date);
    if(!days.has(day)) days.set(day,new Map());
    const byProject=days.get(day);
    if(!byProject.has(event.project_id)) byProject.set(event.project_id,[]);
    byProject.get(event.project_id).push(event);
  }

  const html=[...days.entries()].map(([day,byProject])=>{
    const dateLabel=localDayLabel(day)+(append&&start>0&&day===localDayKey(events[start-1].date)?" (continued)":"");
    const projectsHtml=[...byProject.entries()].sort((a,b)=>{
      const ad=Math.max(...a[1].map(e=>activityEventTime(e.date)));
      const bd=Math.max(...b[1].map(e=>activityEventTime(e.date)));
      return bd-ad;
    }).map(([projectId,commits])=>{
      const snapshot=commits.find(event=>event.project)?.project;
      const project=map.get(projectId) || (snapshot ? {...snapshot,id:projectId} : {id:projectId});
      const commitHtml=commits.sort((a,b)=>activityEventTime(b.date)-activityEventTime(a.date)).map(event=>{
        const time=/^\d{4}-\d{2}-\d{2}$/.test(event.date)
          ? '<span title="Time not recorded">—</span>'
          : new Date(event.date).toLocaleTimeString(undefined,{hour:"2-digit",minute:"2-digit",hour12:false});
        const summary=event.type==="daily_commits";
        const title=summary?(event.count+" commit"+(event.count===1?"":"s")):(event.url?'<a href="'+esc(event.url)+'" target="_blank" rel="noopener">'+esc(event.title)+'</a>':esc(event.title));
        const identity=event.type==="release"?(event.tag?esc(event.tag):"release"):(event.sha?esc(event.sha.slice(0,8)):"");
        const detailParts=[];
        let details="";
        if(event.type==="release"){
          detailParts.push('<span class="activity-kind">release</span>');
          if(identity) detailParts.push('<span class="activity-identity">'+identity+'</span>');
          details=detailParts.join('<span class="detail-separator">·</span>');
        }else if(isProjectActivity(event)){
          const kind=esc(event.type.replace(/^project_/,"").replaceAll("_"," "));
          details='<span class="activity-kind">'+kind+'</span>'
            +'<div class="activity-change-lines">'+projectChangeHtml(event,project)+'</div>';
        }else if(summary){
          const latest=event.latest_url?'<a href="'+esc(event.latest_url)+'" target="_blank" rel="noopener">'+esc(event.latest_title||"Latest commit")+'</a>':esc(event.latest_title||"Latest commit");
          details='<span class="activity-kind">'+esc(activityDate(event.day))+'</span><span class="detail-separator">·</span><span>Latest: '+latest+'</span>';
        }else{
          if(event.author) detailParts.push('<span class="activity-author">'+esc(event.author)+'</span>');
          if(identity) detailParts.push('<span class="activity-identity">'+identity+'</span>');
          for(const branch of arr(event.branches)){
            detailParts.push('<span class="branch">'+esc(branch)+'</span>');
          }
          details=detailParts.join('<span class="detail-separator">·</span>');
        }
        const classes=event.type==="release"?"commit release-event":(isProjectActivity(event)?"commit project-event":"commit");
        return '<div class="'+classes+'" data-reading-anchor="'+esc(reading.ids(event)[0])+'"><div class="commit-time">'+time+'</div><div class="commit-main"><div class="commit-title">'+title+'</div><div class="commit-detail">'+details+'</div></div></div>';
      }).join("");
      return '<div class="activity-project '+(bookmarks.has(projectId)?'bookmarked':'')+'" data-project-id="'+esc(projectId)+'" tabindex="-1"><div class="activity-project-head">'+activityProjectHeader(project)+'</div><div class="commit-list">'+commitHtml+'</div></div>';
    }).join("");
    return '<section class="activity-day" data-day="'+esc(day)+'"><h2>'+esc(dateLabel)+'</h2>'+projectsHtml+'</section>';
  }).join("");
  if(append)$("activityFeed").insertAdjacentHTML("beforeend",html);else $("activityFeed").innerHTML=html;
  if(!append)renderActivityRail();
  activityDayNodes=[...document.querySelectorAll('#activityFeed .activity-day')];
  updateCurrentActivityDay();
}

function requestActivityRender(){
  activityDirty=true;
  activityVisibleCount=ACTIVITY_PAGE_SIZE;
  if(activityVisible()) renderReadyActivity();
}

document.querySelectorAll(".view-tab").forEach(button=>button.addEventListener("click",()=>{
  if(button.classList.contains("active")) return;
  document.querySelectorAll(".view-tab").forEach(x=>x.classList.toggle("active",x===button));
  document.querySelectorAll(".view-panel").forEach(panel=>panel.classList.toggle("active",panel.id===button.dataset.view));
  initializeReadyViews();
  updateReadingControls();
}));

$("activityMore").addEventListener("click",()=>{
  renderActivity(true);
});

if(typeof IntersectionObserver!=='undefined'){
  const observer=new IntersectionObserver(entries=>{
    if(entries.some(entry=>entry.isIntersecting)&&activityVisible()&&activityRenderedCount<activityRenderedEvents.length)renderActivity(true);
  },{rootMargin:'800px 0px'});
  observer.observe($('activitySentinel'));
}

$("activityQ").addEventListener("input",()=>{updateClearButtons();requestActivityRender();});
$("activityClear").addEventListener("click",()=>{
  $("activityQ").value="";
  for(const key of ["type","projectType","platform","cpu","targetKind","workKind","toolKind"]) clearFacetSet(activityFilterState[key]);
  activityFilterState.ai="";
  activityFilterState.days="30";
  activityFilterState.side="either";$("activityDirectionSide").value="either";
  for(const id of Object.keys(activityPickerKeys))clearPicker(id);
  clearFacetButtons($("activityView"));
  resetSegment("activityDaysSegment","30");
  resetSegment("activityAiSegment","");
  updateClearButtons();
  requestActivityRender();
});

let projectsReady=false;
let projectUiReady=false;
let activityReady=false;
let activityUiReady=false;

function renderReadyActivity(){
  if(!projectsReady||!activityReady||!activityUiReady) return;
  if(activityDirty) renderActivity();
}

function initializeReadyViews(){
  if(projectsReady)updateSourceAvailabilityWarning();
  if(projectsReady&&activityReady&&!readingInitialized){
    let position=readingState.position;
    if(position&&!restoreFilters(position.filters))position=null;
    if(position){
      setInboxView(position.scope);
      activityVisibleCount=Math.max(ACTIVITY_PAGE_SIZE,Math.min(position.visible||0,100000));
      document.querySelectorAll('.view-tab').forEach(button=>button.classList.toggle('active',button.dataset.view===position.view));
      document.querySelectorAll('.view-panel').forEach(panel=>panel.classList.toggle('active',panel.id===position.view));
    }
    ingestReadingSnapshot();readingInitialized=true;
    if(position)setTimeout(()=>restorePosition(position),0);
  }
  if(projectsReady&&activityReady&&!activityUiReady){
    initActivityFilters();
    activityUiReady=true;
  }
  if(projectsReady&&!projectUiReady&&$("projects").classList.contains("active")){
    init();
    projectUiReady=true;
  }
  updateClearButtons();
  if(activityVisible()) renderReadyActivity();
}

// Optional enrichment must never prevent the tracker from loading.
async function loadGameLinks(){
  try{
    const response=await fetch("data/game-links.json",{cache:"no-cache"});
    if(!response.ok)throw Error("game links unavailable");
    const data=await response.json();
    if(!data || data.format!=="tracker-game-links/v1" || !data.projects || typeof data.projects!=="object" || Array.isArray(data.projects))throw Error("invalid game links");
    gameLinkIndex=data.projects;
    const position=readingInitialized?capturePosition():null;
    if(projectUiReady)render(true);
    if(activityUiReady && activityVisible())renderActivity();
    if(position)restorePosition(position);
  }catch{} // Preserve the previous snapshot if the optional file is unavailable.
}
loadGameLinks();

const platformVocabularyRequest=fetch("web/platform-vocabulary.json",{cache:"no-cache"})
  .then(response=>{if(!response.ok)throw new Error("platform vocabulary unavailable");return response.json();})
  .catch(()=>({aliases:{},non_platform_values:[]}));

async function loadProjectCatalogue(fetcher=fetch){
  const response=await fetcher("data/projects.index.json",{cache:"no-cache"});
  if(!response.ok) throw new Error("projects index HTTP "+response.status);
  const index=await response.json();
  if(index.format!=="tracker-partitions/v1"||index.kind!=="projects"||
     !Array.isArray(index.order)||!Array.isArray(index.shards)||
     index.order.some(id=>typeof id!=="string")||new Set(index.order).size!==index.order.length)
    throw new Error("Invalid projects index");
  const paths=new Set(),prefixes=[];
  for(const ref of index.shards){
    const match=/^projects\/([0-9a-f]{1,64})\.json$/.exec(ref.path);
    if(!match||paths.has(ref.path)||prefixes.some(p=>p.startsWith(match[1])||match[1].startsWith(p))) throw new Error("Invalid project shard reference");
    paths.add(ref.path);prefixes.push(match[1]);
  }
  const records=new Map();
  // Bound concurrent reads instead of opening hundreds of requests at once.
  let next=0;
  async function worker(){
    while(next<index.shards.length){
      const ref=index.shards[next++];
      const result=await fetcher("data/"+ref.path,{cache:"no-cache"});
      if(!result.ok) throw new Error("project shard HTTP "+result.status);
      const bytes=await result.arrayBuffer();
      const digest=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes)),b=>b.toString(16).padStart(2,"0")).join("");
      if(digest!==ref.sha256) throw new Error("Project shard digest mismatch");
      const items=JSON.parse(new TextDecoder().decode(bytes));
      if(!Array.isArray(items)||items.length!==ref.count) throw new Error("Project shard count mismatch");
      for(const record of items){
        if(typeof record.id!=="string"||records.has(record.id)) throw new Error("Duplicate/invalid project ID");
        records.set(record.id,record);
      }
    }
  }
  await Promise.all(Array.from({length:Math.min(8,index.shards.length)},worker));
  if(records.size!==index.order.length||index.order.some(id=>!records.has(id))) throw new Error("Project index coverage mismatch");
  return index.order.map(id=>records.get(id));
}

loadProjectCatalogue()
  .then(async data=>{platformVocabulary=await platformVocabularyRequest;projects=data;projectsReady=true;initializeReadyViews();})
  .catch(error=>{
    $("rows").innerHTML='<tr><td colspan="'+projectTableColumnSpan()+'" class="empty">Could not load projects: '+esc(error.message)+'</td></tr>';
    $("activityFeed").innerHTML='<div class="activity-empty">Could not load projects: '+esc(error.message)+'</div>';
    updateReadingControls('Could not load projects. Use Fetch updates to retry.');
  }).finally(()=>{initialRequestsPending--;updateReadingControls();});

async function loadActivitySnapshot(){
  const response=await fetch("data/activity-30d.json",{cache:"no-cache"});
  if(!response.ok)throw Error('activity HTTP '+response.status);
  const data=await response.json();
  if(!Array.isArray(data.events)||!Number.isFinite(Date.parse(data.generated_at))||data.events.some(event=>!event||typeof event.project_id!=='string'||typeof event.type!=='string'||!Number.isFinite(Date.parse(event.date))))throw Error('Invalid activity snapshot');
  return data;
}
loadActivitySnapshot().then(data=>{
  activityData=data;activityReady=true;
  $("dataFreshness").textContent=formatFreshness(data.generated_at);initializeReadyViews();
}).catch(error=>{
  $("activityFeed").innerHTML='<div class="activity-empty">Could not load activity: '+esc(error.message)+'</div>';
  updateReadingControls('Could not load activity. Use Fetch updates to retry.');
}).finally(()=>{initialRequestsPending--;updateReadingControls();});
async function fetchUpdates(){
  if(fetchingUpdates)return;
  fetchingUpdates=true;updateReadingControls('Checking published activity and project metadata…');
  try{
    const [newProjects,newActivity]=await Promise.all([loadProjectCatalogue(),loadActivitySnapshot()]);
    void loadGameLinks();
    if(activityReady&&Date.parse(newActivity.generated_at)<Date.parse(activityData.generated_at))throw Error('Received an older snapshot; please retry.');
    const position=readingInitialized?capturePosition():null;
    projects=newProjects;activityData=newActivity;projectsReady=true;activityReady=true;activityDirty=true;
    if(readingInitialized)ingestReadingSnapshot();
    initializeReadyViews();
    bindActivityProjectFacets();
    if(projectUiReady)render();
    if(activityVisible())renderActivity();
    $("dataFreshness").textContent=formatFreshness(activityData.generated_at);
    restorePosition(position);
  }catch(error){updateReadingControls('Fetch failed: '+error.message+'. Your unread items and last successful check are unchanged.');}
  finally{fetchingUpdates=false;updateReadingControls();}
}
