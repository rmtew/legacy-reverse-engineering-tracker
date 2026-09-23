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

const filterIds = [
  "sourcePlatform", "targetPlatform", "cpu", "language", "type", "tag",
  "status", "activity", "compilable", "playable", "exact", "ai"
];

function unique(field) {
  return [...new Set(projects.flatMap(record => arr(record[field])).filter(Boolean))]
    .sort((a, b) => String(a).localeCompare(String(b), undefined, { numeric: true, sensitivity: "base" }));
}

function fillSelect(id, field) {
  const select = $(id);
  for (const value of unique(field)) {
    const option = document.createElement("option");
    option.value = option.textContent = value;
    select.append(option);
  }
}

function fillActivitySelect() {
  const values = [...new Set(projects.map(record => record.github?.activity_state).filter(Boolean))].sort();
  for (const value of values) {
    const option = document.createElement("option");
    option.value = option.textContent = value;
    $("activity").append(option);
  }
}

function sortValue(record, key) {
  const build = record.build || {};
  const ai = record.ai || {};
  return {
    title: record.title,
    source: text(record.source_platforms),
    target: text(record.target_platforms),
    language: text(record.reconstructed_languages),
    type: text(record.types),
    started: record.re_started ?? record.github?.created_at,
    updated: record.last_activity,
    compilable: tri(build.compilable),
    playable: tri(build.playable),
    exact: tri(build.byte_exact),
    ai: tri(ai.usage)
  }[key];
}

function compare(a, b) {
  const av = sortValue(a, sort.key);
  const bv = sortValue(b, sort.key);
  const aMissing = av === null || av === undefined || av === "" || av === "Unknown";
  const bMissing = bv === null || bv === undefined || bv === "" || bv === "Unknown";
  if (aMissing !== bMissing) return aMissing ? 1 : -1;
  return String(av ?? "").localeCompare(
    String(bv ?? ""),
    undefined,
    { numeric: true, sensitivity: "base" }
  ) * sort.dir;
}

function matches(record) {
  const query = $("q").value.trim().toLowerCase();
  const build = record.build || {};
  const ai = record.ai || {};
  const haystack = [
    record.title, record.notes, record.repo, record.project_url, record.status,
    ...arr(record.tags), ...arr(record.techniques), ...arr(record.types),
    ...arr(record.source_platforms), ...arr(record.target_platforms),
    ...arr(record.source_cpu), ...arr(record.reconstructed_languages)
  ].join(" ").toLowerCase();

  return (!query || haystack.includes(query))
    && (!$("sourcePlatform").value || arr(record.source_platforms).includes($("sourcePlatform").value))
    && (!$("targetPlatform").value || arr(record.target_platforms).includes($("targetPlatform").value))
    && (!$("cpu").value || arr(record.source_cpu).includes($("cpu").value))
    && (!$("language").value || arr(record.reconstructed_languages).includes($("language").value))
    && (!$("type").value || arr(record.types).includes($("type").value))
    && (!$("tag").value || arr(record.tags).includes($("tag").value))
    && (!$("status").value || record.status === $("status").value)
    && (!$("activity").value || record.github?.activity_state === $("activity").value)
    && (!$("compilable").value || tri(build.compilable) === $("compilable").value)
    && (!$("playable").value || tri(build.playable) === $("playable").value)
    && (!$("exact").value || tri(build.byte_exact) === $("exact").value)
    && (!$("ai").value || tri(ai.usage) === $("ai").value);
}

function projectCell(record) {
  const title = esc(record.title || record.id || "?");
  const url = record.project_url || record.repo;
  if (!url) return "<strong>" + title + "</strong>";
  return '<a class="project-link" href="' + esc(url) + '" target="_blank" rel="noopener">' + title + "</a>";
}

function render() {
  const rows = projects.filter(matches).sort(compare);
  $("count").textContent = rows.length;
  $("total").textContent = projects.length;
  $("sortnote").textContent = "Sorted by " + sort.key + (sort.dir < 0 ? " ↓" : " ↑");

  document.querySelectorAll("th[data-key]").forEach(th => {
    th.removeAttribute("data-sort");
    if (th.dataset.key === sort.key) th.dataset.sort = sort.dir > 0 ? "asc" : "desc";
  });

  if (!rows.length) {
    $("rows").innerHTML = '<tr><td colspan="11" class="empty">No projects match the current filters.</td></tr>';
    return;
  }

  $("rows").innerHTML = rows.map(record => {
    const build = record.build || {};
    const ai = record.ai || {};
    const started = record.re_started ?? (record.github?.created_at ? record.github.created_at.slice(0, 4) + "*" : "?");

    return '<tr class="project-row" data-id="' + esc(record.id) + '">'
      + "<td>" + projectCell(record) + "</td>"
      + "<td>" + tags(record.source_platforms) + "</td>"
      + "<td>" + tags(record.target_platforms) + "</td>"
      + "<td>" + tags(record.reconstructed_languages) + "</td>"
      + "<td>" + tags(record.types) + "</td>"
      + "<td>" + esc(started) + "</td>"
      + "<td>" + esc(record.last_activity ?? "?") + "</td>"
      + "<td>" + flag(build.compilable) + "</td>"
      + "<td>" + flag(build.playable) + "</td>"
      + "<td>" + flag(build.byte_exact) + "</td>"
      + "<td>" + flag(ai.usage) + "</td>"
      + "</tr>";
  }).join("");

  document.querySelectorAll("#rows tr.project-row").forEach(row => {
    row.addEventListener("click", event => {
      if (event.target.closest("a")) return;
      showDetails(projects.find(record => record.id === row.dataset.id));
    });
  });
}

function showDetails(record) {
  const build = record.build || {};
  const ai = record.ai || {};
  const line = (label, value) => "<dt>" + label + "</dt><dd>" + value + "</dd>";
  const repo = record.repo
    ? '<a href="' + esc(record.repo) + '" target="_blank" rel="noopener">' + esc(record.repo) + "</a>"
    : "?";
  const project = record.project_url
    ? '<a href="' + esc(record.project_url) + '" target="_blank" rel="noopener">' + esc(record.project_url) + "</a>"
    : null;
  const latestCommit = record.github?.latest_commit?.url
    ? '<a href="' + esc(record.github.latest_commit.url) + '" target="_blank" rel="noopener">'
      + esc((record.github.latest_commit.date || "?") + " — " + (record.github.latest_commit.message || ""))
      + "</a>"
    : "?";
  const latestRelease = record.github?.latest_release?.url
    ? '<a href="' + esc(record.github.latest_release.url) + '" target="_blank" rel="noopener">'
      + esc((record.github.latest_release.tag || record.github.latest_release.name || "release")
        + (record.github.latest_release.published_at ? " — " + record.github.latest_release.published_at : ""))
      + "</a>"
    : "?";

  $("detailbody").innerHTML = "<h2>" + esc(record.title) + '</h2><dl class="details-grid">'
    + (project ? line("Project page", project) : "")
    + line("Repository", repo)
    + line("Source platform", tags(record.source_platforms))
    + line("Target platform", tags(record.target_platforms))
    + line("CPU", tags(record.source_cpu))
    + line("Original/source language", tags(record.source_language))
    + line("Reconstructed language", tags(record.reconstructed_languages))
    + line("RE type", tags(record.types))
    + line("Started", esc(record.re_started ?? "?"))
    + line("Last activity", esc(record.last_activity ?? "?"))
    + line("Last checked", esc(record.last_checked ?? "?"))
    + line("Repository created", esc(record.github?.created_at ?? "?"))
    + line("GitHub activity", esc(record.github?.activity_state ?? "?"))
    + line("Default branch", esc(record.github?.default_branch ?? "?"))
    + line("Tracked branch", esc(record.github?.tracking_branch ?? "?"))
    + line("Tracked path", esc(record.github?.tracking_path ?? "?"))
    + line("GitHub languages", tags(record.github?.languages))
    + line("Latest commit", latestCommit)
    + line("Latest release", latestRelease)
    + line("Status", esc(record.status ?? "?"))
    + line("Compilable", tri(build.compilable))
    + line("Runnable", tri(build.runnable))
    + line("Playable", tri(build.playable))
    + line("Byte exact", tri(build.byte_exact))
    + line("AI usage", tri(ai.usage))
    + line("AI tools", tags(ai.tools))
    + line("AI evidence", tags(ai.evidence))
    + line("Techniques", tags(record.techniques))
    + line("Tags", tags(record.tags))
    + line("Notes", esc(record.notes || ""))
    + "</dl>";

  $("details").showModal();
}

function init() {
  fillSelect("sourcePlatform", "source_platforms");
  fillSelect("targetPlatform", "target_platforms");
  fillSelect("cpu", "source_cpu");
  fillSelect("language", "reconstructed_languages");
  fillSelect("type", "types");
  fillSelect("tag", "tags");
  fillSelect("status", "status");
  fillActivitySelect();
  $("total").textContent = projects.length;
  render();
}

fetch("data/projects.json", { cache: "no-cache" })
  .then(response => {
    if (!response.ok) throw new Error("HTTP " + response.status);
    return response.json();
  })
  .then(data => {
    projects = data;
    init();
  })
  .catch(error => {
    $("rows").innerHTML = '<tr><td colspan="11" class="empty">Could not load project data: ' + esc(error.message) + "</td></tr>";
  });

$("q").addEventListener("input", render);
filterIds.forEach(id => $(id).addEventListener("change", render));
$("clear").addEventListener("click", () => {
  $("q").value = "";
  filterIds.forEach(id => { $(id).value = ""; });
  render();
});

document.querySelectorAll("th[data-key]").forEach(th => th.addEventListener("click", () => {
  sort = sort.key === th.dataset.key
    ? { key: sort.key, dir: -sort.dir }
    : { key: th.dataset.key, dir: 1 };
  render();
}));

document.querySelector("#details .close").addEventListener("click", () => $("details").close());
$("details").addEventListener("click", event => {
  if (event.target === $("details")) $("details").close();
});


let activityData = { generated_at: null, window_days: 180, events: [] };
const projectById = () => new Map(projects.map(project => [project.id, project]));
const activityFilterIds = ["activityDays","activityPlatform","activityProject","activityLanguage","activityBranch","activityAi"];

function addOptions(selectId, values) {
  const select = $(selectId);
  for (const value of [...new Set(values.filter(Boolean))].sort((a,b)=>String(a).localeCompare(String(b),undefined,{numeric:true,sensitivity:"base"}))) {
    const option=document.createElement("option");
    option.value=option.textContent=value;
    select.append(option);
  }
}

function initActivityFilters() {
  addOptions("activityPlatform", projects.flatMap(p=>arr(p.source_platforms)));
  const projectSelect=$("activityProject");
  for (const project of [...projects].sort((a,b)=>a.title.localeCompare(b.title))) {
    const option=document.createElement("option");
    option.value=project.id; option.textContent=project.title; projectSelect.append(option);
  }
  addOptions("activityLanguage", projects.flatMap(p=>arr(p.reconstructed_languages)));
  addOptions("activityBranch", activityData.events.flatMap(e=>arr(e.branches)));
}

function activityMatches(event) {
  const map=projectById(), project=map.get(event.project_id);
  if(!project) return false;
  const days=Number($("activityDays").value||30);
  const cutoff=Date.now()-days*86400000;
  if(new Date(event.date).getTime()<cutoff) return false;
  const q=$("activityQ").value.trim().toLowerCase();
  const hay=[event.title,event.message,event.author,event.repository,project.title,...arr(event.branches),...arr(project.tags)].join(" ").toLowerCase();
  return (!q||hay.includes(q))
    && (!$("activityPlatform").value||arr(project.source_platforms).includes($("activityPlatform").value))
    && (!$("activityProject").value||project.id===$("activityProject").value)
    && (!$("activityLanguage").value||arr(project.reconstructed_languages).includes($("activityLanguage").value))
    && (!$("activityBranch").value||arr(event.branches).includes($("activityBranch").value))
    && (!$("activityAi").value||tri(project.ai?.usage)===$("activityAi").value);
}

function activityProjectHeader(project) {
  const url=project.project_url||project.repo;
  const title=url?'<a href="'+esc(url)+'" target="_blank" rel="noopener">'+esc(project.title)+'</a>':esc(project.title);
  return '<strong>'+title+'</strong><div class="activity-project-meta">'+esc(text(project.source_platforms))+'</div>';
}

function renderActivity() {
  const map=projectById();
  const events=activityData.events.filter(activityMatches).sort((a,b)=>new Date(b.date)-new Date(a.date));
  $("activityCount").textContent=events.length;
  $("activityProjectCount").textContent=new Set(events.map(e=>e.project_id)).size;
  $("activityGenerated").textContent=activityData.generated_at?"Collected "+activityData.generated_at.slice(0,10):"";

  if(!events.length){
    $("activityFeed").innerHTML='<div class="activity-empty">No commits match the current filters.</div>';
    return;
  }

  const days=new Map();
  for(const event of events){
    const day=event.date.slice(0,10);
    if(!days.has(day)) days.set(day,new Map());
    const byProject=days.get(day);
    if(!byProject.has(event.project_id)) byProject.set(event.project_id,[]);
    byProject.get(event.project_id).push(event);
  }

  $("activityFeed").innerHTML=[...days.entries()].map(([day,byProject])=>{
    const dateLabel=new Date(day+"T12:00:00Z").toLocaleDateString(undefined,{weekday:"long",year:"numeric",month:"long",day:"numeric",timeZone:"UTC"});
    const projectsHtml=[...byProject.entries()].sort((a,b)=>{
      const ad=Math.max(...a[1].map(e=>new Date(e.date).getTime()));
      const bd=Math.max(...b[1].map(e=>new Date(e.date).getTime()));
      return bd-ad;
    }).map(([projectId,commits])=>{
      const project=map.get(projectId);
      const commitHtml=commits.sort((a,b)=>new Date(b.date)-new Date(a.date)).map(event=>{
        const time=new Date(event.date).toLocaleTimeString(undefined,{hour:"2-digit",minute:"2-digit",hour12:false});
        const title=event.url?'<a href="'+esc(event.url)+'" target="_blank" rel="noopener">'+esc(event.title)+'</a>':esc(event.title);
        const details=[event.author?esc(event.author):"",esc(event.sha.slice(0,8))].filter(Boolean).join(" · ");
        return '<div class="commit"><div class="commit-time">'+time+'</div><div class="commit-main"><div class="commit-title">'+title+'</div><div class="commit-detail">'+details+'</div></div><div class="commit-branches">'+arr(event.branches).map(b=>'<span class="branch">'+esc(b)+'</span>').join("")+'</div></div>';
      }).join("");
      return '<div class="activity-project"><div class="activity-project-head">'+activityProjectHeader(project)+'</div><div class="commit-list">'+commitHtml+'</div></div>';
    }).join("");
    return '<section class="activity-day"><h2>'+esc(dateLabel)+'</h2>'+projectsHtml+'</section>';
  }).join("");
}

document.querySelectorAll(".view-tab").forEach(button=>button.addEventListener("click",()=>{
  document.querySelectorAll(".view-tab").forEach(x=>x.classList.toggle("active",x===button));
  document.querySelectorAll(".view-panel").forEach(panel=>panel.classList.toggle("active",panel.id===button.dataset.view));
  if(button.dataset.view==="activityView") renderActivity();
}));

$("activityQ").addEventListener("input",renderActivity);
activityFilterIds.forEach(id=>$(id).addEventListener("change",renderActivity));
$("activityClear").addEventListener("click",()=>{
  $("activityQ").value="";
  $("activityDays").value="30";
  ["activityPlatform","activityProject","activityLanguage","activityBranch","activityAi"].forEach(id=>$(id).value="");
  renderActivity();
});

Promise.all([
  fetch("data/projects.json",{cache:"no-cache"}).then(r=>{if(!r.ok)throw new Error("projects HTTP "+r.status);return r.json()}),
  fetch("data/activity.json",{cache:"no-cache"}).then(r=>{if(!r.ok)throw new Error("activity HTTP "+r.status);return r.json()})
]).then(([projectData,activity])=>{
  activityData=activity;
  if(projects.length===0){projects=projectData;init();}
  initActivityFilters();
  renderActivity();
}).catch(error=>{
  $("activityFeed").innerHTML='<div class="activity-empty">Could not load activity: '+esc(error.message)+'</div>';
});
