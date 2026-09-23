let projects=[];
let sort={key:"title",dir:1};

const $=id=>document.getElementById(id);
const arr=v=>Array.isArray(v)?v:(v===null||v===undefined||v===""?[]:[v]);
const text=v=>arr(v).join(", ");
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const tri=v=>v===true?"Yes":v===false?"No":"Unknown";
const flag=v=>{const t=tri(v);return '<span class="flag '+t.toLowerCase()+'" title="'+t+'">'+(t==="Unknown"?"?":t)+'</span>'};
const tags=v=>{const xs=arr(v);return xs.length?'<span class="tags">'+xs.map(x=>'<span class="tag">'+esc(x)+'</span>').join("")+'</span>':'?'};

const filterIds=["sourcePlatform","targetPlatform","cpu","language","type","tag","status","activity","compilable","playable","exact","ai"];

function unique(field){
  return [...new Set(projects.flatMap(r=>arr(r[field])).filter(Boolean))]
    .sort((a,b)=>String(a).localeCompare(String(b),undefined,{numeric:true,sensitivity:"base"}));
}
function fillSelect(id,field){
  const select=$(id);
  for(const value of unique(field)){
    const option=document.createElement("option");
    option.value=option.textContent=value;
    select.append(option);
  }
}

function sortValue(r,key){
  const b=r.build||{},a=r.ai||{};
  return {
    title:r.title, source:text(r.source_platforms), target:text(r.target_platforms),
    language:text(r.reconstructed_languages), type:text(r.types),
    started:r.re_started??r.github?.created_at, updated:r.last_activity,
    compilable:tri(b.compilable), playable:tri(b.playable),
    exact:tri(b.byte_exact), ai:tri(a.usage)
  }[key];
}
function compare(a,b){
  const av=sortValue(a,sort.key),bv=sortValue(b,sort.key);
  const aMissing=av===null||av===undefined||av===""||av==="Unknown";
  const bMissing=bv===null||bv===undefined||bv===""||bv==="Unknown";
  if(aMissing!==bMissing)return aMissing?1:-1;
  return String(av??"").localeCompare(String(bv??""),undefined,{numeric:true,sensitivity:"base"})*sort.dir;
}

function matches(r){
  const q=$("q").value.trim().toLowerCase();
  const b=r.build||{},a=r.ai||{};
  const hay=[
    r.title,r.notes,r.repo,r.status,
    ...arr(r.tags),...arr(r.techniques),...arr(r.types),
    ...arr(r.source_platforms),...arr(r.target_platforms),
    ...arr(r.source_cpu),...arr(r.reconstructed_languages)
  ].join(" ").toLowerCase();

  return (!q||hay.includes(q))
    && (!$("sourcePlatform").value||arr(r.source_platforms).includes($("sourcePlatform").value))
    && (!$("targetPlatform").value||arr(r.target_platforms).includes($("targetPlatform").value))
    && (!$("cpu").value||arr(r.source_cpu).includes($("cpu").value))
    && (!$("language").value||arr(r.reconstructed_languages).includes($("language").value))
    && (!$("type").value||arr(r.types).includes($("type").value))
    && (!$("tag").value||arr(r.tags).includes($("tag").value))
    && (!$("status").value||r.status===$("status").value)\n    && (!$("activity").value||r.github?.activity_state===$("activity").value)
    && (!$("compilable").value||tri(b.compilable)===$("compilable").value)
    && (!$("playable").value||tri(b.playable)===$("playable").value)
    && (!$("exact").value||tri(b.byte_exact)===$("exact").value)
    && (!$("ai").value||tri(a.usage)===$("ai").value);
}

function projectCell(r){
  const title=esc(r.title||r.id||"?");
  if(!r.repo)return '<strong>'+title+'</strong>';
  return '<a class="project-link" href="'+esc(r.repo)+'" target="_blank" rel="noopener">'+title+'</a>';
}

function render(){
  const rows=projects.filter(matches).sort(compare);
  $("count").textContent=rows.length;
  $("total").textContent=projects.length;
  $("sortnote").textContent="Sorted by "+sort.key+(sort.dir<0?" ↓":" ↑");
  document.querySelectorAll("th[data-key]").forEach(th=>{
    th.removeAttribute("data-sort");
    if(th.dataset.key===sort.key)th.dataset.sort=sort.dir>0?"asc":"desc";
  });

  if(!rows.length){
    $("rows").innerHTML='<tr><td colspan="11" class="empty">No projects match the current filters.</td></tr>';
    return;
  }

  $("rows").innerHTML=rows.map(r=>{
    const b=r.build||{},a=r.ai||{};
    return '<tr class="project-row" data-id="'+esc(r.id)+'">'
      +'<td>'+projectCell(r)+'</td>'
      +'<td>'+tags(r.source_platforms)+'</td>'
      +'<td>'+tags(r.target_platforms)+'</td>'
      +'<td>'+tags(r.reconstructed_languages)+'</td>'
      +'<td>'+tags(r.types)+'</td>'
      +'<td>'+esc(r.re_started??(r.github?.created_at?r.github.created_at.slice(0,4)+"*":"?"))+'</td>'
      +'<td>'+esc(r.last_activity??"?")+'</td>'
      +'<td>'+flag(b.compilable)+'</td>'
      +'<td>'+flag(b.playable)+'</td>'
      +'<td>'+flag(b.byte_exact)+'</td>'
      +'<td>'+flag(a.usage)+'</td></tr>';
  }).join("");

  document.querySelectorAll("#rows tr.project-row").forEach(tr=>{
    tr.addEventListener("click",e=>{
      if(e.target.closest("a"))return;
      showDetails(projects.find(r=>r.id===tr.dataset.id));
    });
  });
}

function showDetails(r){
  const b=r.build||{},a=r.ai||{};
  const line=(label,value)=>'<dt>'+label+'</dt><dd>'+value+'</dd>';
  const repo=r.repo?'<a href="'+esc(r.repo)+'" target="_blank" rel="noopener">'+esc(r.repo)+'</a>':'?';
  $("detailbody").innerHTML='<h2>'+esc(r.title)+'</h2><dl class="details-grid">'
    +line("Repository",repo)
    +line("Source platform",tags(r.source_platforms))
    +line("Target platform",tags(r.target_platforms))
    +line("CPU",tags(r.source_cpu))
    +line("Original/source language",tags(r.source_language))
    +line("Reconstructed language",tags(r.reconstructed_languages))
    +line("RE type",tags(r.types))
    +line("Started",esc(r.re_started??"?"))
    +line("Last activity",esc(r.last_activity??"?"))
    +line("Last checked",esc(r.last_checked??"?"))\n    +line("Repository created",esc(r.github?.created_at??"?"))\n    +line("GitHub activity",esc(r.github?.activity_state??"?"))\n    +line("Default branch",esc(r.github?.default_branch??"?"))\n    +line("GitHub languages",tags(r.github?.languages))\n    +line("Latest commit",r.github?.latest_commit?.url?'<a href="'+esc(r.github.latest_commit.url)+'" target="_blank" rel="noopener">'+esc(r.github.latest_commit.date+" — "+r.github.latest_commit.message)+'</a>':"?")
    +line("Status",esc(r.status??"?"))
    +line("Compilable",tri(b.compilable))
    +line("Runnable",tri(b.runnable))
    +line("Playable",tri(b.playable))
    +line("Byte exact",tri(b.byte_exact))
    +line("AI usage",tri(a.usage))
    +line("AI tools",tags(a.tools))
    +line("Techniques",tags(r.techniques))
    +line("Tags",tags(r.tags))
    +line("Notes",esc(r.notes||""))
    +'</dl>';
  $("details").showModal();
}

function init(){
  fillSelect("sourcePlatform","source_platforms");
  fillSelect("targetPlatform","target_platforms");
  fillSelect("cpu","source_cpu");
  fillSelect("language","reconstructed_languages");
  fillSelect("type","types");
  fillSelect("tag","tags");
  fillSelect("status","status");\n  const activities=[...new Set(projects.map(r=>r.github?.activity_state).filter(Boolean))].sort(); for(const value of activities){const o=document.createElement("option");o.value=o.textContent=value;$("activity").append(o);}
  $("total").textContent=projects.length;
  render();
}

fetch("data/projects.json",{cache:"no-cache"})
  .then(r=>{if(!r.ok)throw new Error("HTTP "+r.status);return r.json()})
  .then(data=>{projects=data;init()})
  .catch(error=>{
    $("rows").innerHTML='<tr><td colspan="11" class="empty">Could not load project data: '+esc(error.message)+'</td></tr>';
  });

$("q").addEventListener("input",render);
filterIds.forEach(id=>$(id).addEventListener("change",render));
$("clear").addEventListener("click",()=>{
  $("q").value="";
  filterIds.forEach(id=>$(id).value="");
  render();
});
document.querySelectorAll("th[data-key]").forEach(th=>th.addEventListener("click",()=>{
  sort=sort.key===th.dataset.key?{key:sort.key,dir:-sort.dir}:{key:th.dataset.key,dir:1};
  render();
}));
document.querySelector("#details .close").addEventListener("click",()=>$("details").close());
$("details").addEventListener("click",e=>{if(e.target===$("details"))$("details").close()});
