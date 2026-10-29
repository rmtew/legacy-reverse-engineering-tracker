/* Local-only reading state. No timestamps are used as a proxy for discovery. */
(function(root){
  'use strict';
  const KEY='retro-development-tracker.inbox.v1', BOOKMARKS='retro-development-tracker.bookmarks.v1';
  const validId=id=>typeof id==='string'&&id.length>0&&id.length<=2048&&!/[\u0000-\u001f]/.test(id);
  const canonical=value=>JSON.stringify(value,(_,v)=>v&&typeof v==='object'&&!Array.isArray(v)?Object.fromEntries(Object.keys(v).sort().map(k=>[k,v[k]])):v);
  function fingerprint(value){
    let a=2166136261,b=5381;
    for(const c of canonical(value)){a=Math.imul(a^c.charCodeAt(0),16777619);b=Math.imul(b,33)^c.charCodeAt(0);}
    return (a>>>0).toString(16).padStart(8,'0')+(b>>>0).toString(16).padStart(8,'0');
  }
  const identity=(event,sha)=>fingerprint([event.project_id,event.type==='daily_commits'?'commit':event.type,sha||event.sha||event.tag||event.id||event.event_id||[event.date,event.url,event.type==='daily_commits'?[event.day,event.count]:null,fingerprint(event.change_details||event.changes||event.title||event.message||"")]]);
  const identityCache=new WeakMap();
  function ids(event){
    if(!identityCache.has(event))identityCache.set(event,event.type==='daily_commits'&&Array.isArray(event.shas)&&event.shas.length?event.shas.map(sha=>identity(event,sha)):[identity(event)]);
    return identityCache.get(event);
  }
  const empty=()=>({version:2,checked:null,snapshot:null,seen:{},position:null});
  function parse(raw){
    if(!raw)return empty();
    const value=JSON.parse(raw);
    if(![1,2].includes(value.version)||!value.seen||typeof value.seen!=='object'||Array.isArray(value.seen)||Object.entries(value.seen).some(([id,v])=>!validId(id)||typeof v!=='boolean')|| (value.checked!==null&&!Number.isFinite(value.checked)))throw Error('Invalid reading state');
    if(value.snapshot!==null&&(typeof value.snapshot!=='string'||!Number.isFinite(Date.parse(value.snapshot))))throw Error('Invalid snapshot boundary');
    const p=value.position;
    if(p&&(!['activityView','projects'].includes(p.view)||!['unread','all','bookmarks'].includes(p.scope)||!Number.isFinite(p.y)||p.y<0||p.y>1e9||!Number.isFinite(p.offset)||Math.abs(p.offset)>1e9||!Number.isInteger(p.visible)||p.visible<0||p.visible>100000||(p.anchor!==null&&!validId(p.anchor))))value.position=null;
    // v1 false values mix implicit baseline and explicit acknowledgements: neither is provable.
    if(value.version===1)return {...empty(),position:value.position,migrationNotice:true};
    return value;
  }
  function reconcile(state,events,snapshot,now=Date.now()){
    if(state.snapshot&&Date.parse(snapshot)<Date.parse(state.snapshot))return {state,added:0,firstVisit:false,limited:false,expired:0,stale:true};
    const next=JSON.parse(JSON.stringify(state)),firstVisit=!state.checked;
    const available=new Set(),cutoff=Date.parse(snapshot)-30*86400000;
    let added=0,expired=0;
    for(const event of events)for(const id of ids(event)){
      available.add(id);
      if(!Object.hasOwn(next.seen,id)){
        next.seen[id]=true;
        added++;
      }
    }
    for(const [id,value] of Object.entries(next.seen))if(!available.has(id)){
      if(value)expired++;
      delete next.seen[id];
    }
    next.checked=now;next.snapshot=snapshot;
    return {state:next,added,firstVisit,limited:!!state.checked&&(Date.parse(state.snapshot)<cutoff||expired>0),expired};
  }
  function acknowledge(state,shownIds){
    const next=JSON.parse(JSON.stringify(state));
    next.migrationNotice=false;
    for(const id of shownIds)if(Object.hasOwn(next.seen,id))next.seen[id]=false;
    return next;
  }
  function parseBookmarks(raw){
    const data=typeof raw==='string'?JSON.parse(raw):raw;
    if(!data||data.version!==1||!Array.isArray(data.project_ids)||data.project_ids.length>20000||data.project_ids.some(id=>!validId(id)))throw Error('Choose a valid version 1 bookmark export.');
    return [...new Set(data.project_ids)];
  }
  const api={KEY,BOOKMARKS,empty,parse,ids,reconcile,acknowledge,parseBookmarks};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  else root.TrackerReading=api;
})(globalThis);
