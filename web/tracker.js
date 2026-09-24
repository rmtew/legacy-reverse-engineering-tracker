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
  if(cpu.includes("6502")||cpu.includes("6510")||cpu.includes("7501")||cpu.includes("8501")||cpu.includes("2a03")||cpu.includes("huc6280")) return "6502 family";
  if(cpu.includes("m68k")||cpu.includes("68000")||cpu.includes("68010")||cpu.includes("68020")||cpu.includes("68030")||cpu.includes("68040")||cpu.includes("68060")) return "68000 family";
  if(cpu==="8086"||cpu.includes("x86")) return "x86";
  if(cpu.includes("z80")) return "Z80";
  if(cpu.includes("8080")) return "8080";
  if(cpu.includes("6809")) return "6809";
  if(cpu.includes("arm")) return "ARM";
  if(cpu.includes("sh-2")||cpu.includes("sh2")) return "SH-2";
  if(cpu.includes("jaguar")) return "Jaguar GPU/DSP";
  return raw;
};
const platformValues = record => [...new Set([...arr(record?.source_platforms),...arr(record?.target_platforms)].filter(Boolean))];
const runtimeProfiles = record => arr(record?.runtime_profiles).filter(profile=>profile&&profile.platform);
const cpuFamilyValues = record => [...new Set([
  ...arr(record?.source_cpu),...arr(record?.target_cpu),
  ...runtimeProfiles(record).flatMap(profile=>[profile.cpu_family,profile.min_cpu])
].map(cpuFamily).filter(Boolean))];

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
  projectType:new Set(), platform:new Set(), targetKind:new Set(), workKind:new Set(),
  toolKind:new Set(), cpu:new Set(), language:new Set(),
  runsOnCpu:"", runsOnRam:"", runsOnChipset:"",
  ai:"", compilable:"", playable:"", exact:""
};
const activityFilterState = {
  type:new Set(), projectType:new Set(), platform:new Set(), cpu:new Set(), targetKind:new Set(),
  workKind:new Set(), toolKind:new Set(), ai:"", days:"30"
};

const sortedUnique = (values,labeler=value=>value) =>
  [...new Set(values.filter(Boolean))].sort((a,b)=>
    String(labeler(a)).localeCompare(String(labeler(b)),undefined,{numeric:true,sensitivity:"base"})
  );
const facetMatch = (selected,values) => !selected.size || arr(values).some(value=>selected.has(value));

function bindFacet(containerId,values,selected,labeler,onChange){
  const container=$(containerId);
  container.innerHTML=sortedUnique(values,labeler).map(value=>
    '<button type="button" class="facet-chip" data-value="'+esc(value)+'" aria-pressed="false">'+esc(labeler(value))+'</button>'
  ).join("");
  container.querySelectorAll(".facet-chip").forEach(button=>button.addEventListener("click",()=>{
    const value=button.dataset.value;
    if(selected.has(value)) selected.delete(value); else selected.add(value);
    button.classList.toggle("selected",selected.has(value));
    button.setAttribute("aria-pressed",selected.has(value)?"true":"false");
    onChange();
  }));
}

function bindChoiceFacet(containerId,values,state,key,labeler,onChange){
  const container=$(containerId);
  const options=sortedUnique(values,labeler);
  container.innerHTML='<button type="button" class="facet-chip choice-chip selected" data-value="" aria-pressed="true">Any</button>'
    +options.map(value=>'<button type="button" class="facet-chip choice-chip" data-value="'+esc(value)+'" aria-pressed="false">'+esc(labeler(value))+'</button>').join("");
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
  return $("q").value.trim() || ["projectType","platform","targetKind","workKind","toolKind","cpu","language"].some(key=>projectFilterState[key].size)
    || ["runsOnCpu","runsOnRam","runsOnChipset","ai","compilable","playable","exact"].some(key=>projectFilterState[key]);
}
function activityFiltersActive(){
  return $("activityQ").value.trim() || activityFilterState.days!=="30"
    || ["type","projectType","platform","cpu","targetKind","workKind","toolKind"].some(key=>activityFilterState[key].size)
    || activityFilterState.ai;
}
function updateClearButtons(){
  $("clear").hidden=!projectFiltersActive();
  $("activityClear").hidden=!activityFiltersActive();
}

function sortValue(record, key) {
  const build = record.build || {};
  const ai = record.ai || {};
  return {
    title: projectTitle(record),
    source: text(record.source_platforms),
    target: text(record.target_platforms),
    language: text(record.reconstructed_languages),
    classification: classificationSortValue(record),
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
    projectTitle(record), record.title, record.upstream_name, ...arr(record.subjects),
    record.notes, record.repo, record.project_url, record.status,
    ...arr(record.tags), ...arr(record.techniques), ...arr(record.types),
    ...projectTypeValues(record).map(projectTypeLabel),
    ...arr(record.target_kinds), ...arr(record.work_kinds), ...arr(record.tool_kinds),
    ...platformValues(record),...cpuFamilyValues(record),
    ...arr(record.source_cpu),...arr(record.target_cpu),...arr(record.reconstructed_languages),
    ...runtimeProfiles(record).flatMap(profile=>[
      profile.platform,profile.cpu_family,profile.min_cpu,...arr(profile.chipsets),profile.os,profile.notes
    ])
  ].join(" ").toLowerCase();

  const profiles=runtimeProfiles(record);
  const runtimeRequested=projectFilterState.runsOnCpu||projectFilterState.runsOnRam||projectFilterState.runsOnChipset;
  const runtimeMatch=!runtimeRequested || profiles.some(profile=>
    (!projectFilterState.platform.size || projectFilterState.platform.has(profile.platform))
    && (!projectFilterState.runsOnCpu || (profile.min_cpu && cpuCompatible(profile.min_cpu,projectFilterState.runsOnCpu)))
    && (!projectFilterState.runsOnRam || (Number.isFinite(profile.min_ram_kib) && profile.min_ram_kib<=Number(projectFilterState.runsOnRam)))
    && (!projectFilterState.runsOnChipset || arr(profile.chipsets).includes(projectFilterState.runsOnChipset))
  );

  return (!query || haystack.includes(query))
    && facetMatch(projectFilterState.projectType,projectTypeValues(record))
    && facetMatch(projectFilterState.platform,platformValues(record))
    && facetMatch(projectFilterState.cpu,cpuFamilyValues(record))
    && facetMatch(projectFilterState.targetKind,record.target_kinds)
    && facetMatch(projectFilterState.workKind,record.work_kinds)
    && facetMatch(projectFilterState.toolKind,record.tool_kinds)
    && facetMatch(projectFilterState.cpu,record.source_cpu)
    && facetMatch(projectFilterState.language,record.reconstructed_languages)
    && runtimeMatch
    && (!projectFilterState.ai || tri(ai.usage)===projectFilterState.ai)
    && (!projectFilterState.compilable || tri(build.compilable)===projectFilterState.compilable)
    && (!projectFilterState.playable || tri(build.playable)===projectFilterState.playable)
    && (!projectFilterState.exact || tri(build.byte_exact)===projectFilterState.exact);
}

function projectCell(record) {
  const title = esc(projectTitle(record));
  const upstream = upstreamName(record);
  const tooltip = upstream && upstream !== projectTitle(record) ? ' title="Upstream: '+esc(upstream)+'"' : "";
  const url = record.project_url || record.repo;
  if (!url) return "<strong" + tooltip + ">" + title + "</strong>";
  return '<a class="project-link" href="' + esc(url) + '" target="_blank" rel="noopener"' + tooltip + ">" + title + "</a>";
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
      + "<td>" + classificationTags(record) + "</td>"
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

function showDetails(record) {
  const build = record.build || {};
  const ai = record.ai || {};
  const autoEvidence = record.evidence?.automated || {};
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

  const shownTitle=projectTitle(record);
  const upstream=upstreamName(record);
  $("detailbody").innerHTML = "<h2>" + esc(shownTitle) + '</h2><dl class="details-grid">'
    + (upstream && upstream !== shownTitle ? line("Upstream name", esc(upstream)) : "")
    + line("Subjects", tags(record.subjects))
    + (project ? line("Project page", project) : "")
    + line("Repository", repo)
    + line("Source platform", tags(record.source_platforms))
    + line("Target platform", tags(record.target_platforms))
    + line("CPU family", tags(cpuFamilyValues(record)))
    + line("Source CPU", tags(record.source_cpu))
    + (arr(record.target_cpu).length ? line("Target CPU", tags(record.target_cpu)) : "")
    + (runtimeProfiles(record).length ? line("Runs on", runtimeProfilesHtml(record)) : "")
    + line("Original/source language", tags(record.source_language))
    + line("Reconstructed language", tags(record.reconstructed_languages))
    + line("Project type", tags(projectTypeValues(record).map(projectTypeLabel)))
    + line("Software type", classificationValueTags(record.target_kinds))
    + line("Work", classificationValueTags(record.work_kinds))
    + line("Development tool", classificationValueTags(record.tool_kinds))
    + line("Legacy type descriptors", tags(record.types))
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
    + line("Compile evidence", evidenceHtml(autoEvidence.compilable))
    + line("Playable evidence", evidenceHtml(autoEvidence.playable))
    + line("Byte-exact evidence", evidenceHtml(autoEvidence.byte_exact))
    + line("Start-date evidence", evidenceHtml(autoEvidence.re_started))
    + line("CI signals", ciEvidenceHtml(autoEvidence.ci))
    + line("AI usage", tri(ai.usage))
    + line("AI tools", tags(ai.tools))
    + line("AI evidence", tags(ai.evidence))
    + line("Techniques", tags(record.techniques))
    + line("Tags", tags(record.tags))
    + line("Notes", esc(record.notes || ""))
    + "</dl>";

  $("details").showModal();
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
  bindFacet("platformFacet",projects.flatMap(platformValues),projectFilterState.platform,value=>value,()=>{updateClearButtons();render();});
  bindFacet("cpuFacet",projects.flatMap(cpuFamilyValues),projectFilterState.cpu,value=>value,()=>{updateClearButtons();render();});
  bindFacet("targetKindFacet",projects.flatMap(record=>arr(record.target_kinds)),projectFilterState.targetKind,classificationLabel,()=>{updateClearButtons();render();});
  bindFacet("workKindFacet",projects.flatMap(record=>arr(record.work_kinds)),projectFilterState.workKind,classificationLabel,()=>{updateClearButtons();render();});
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

// Project and activity data are loaded together below.

$("q").addEventListener("input",()=>{updateClearButtons();render();});
$("clear").addEventListener("click", () => {
  $("q").value = "";
  for(const key of ["projectType","platform","targetKind","workKind","toolKind","cpu","language"]) clearFacetSet(projectFilterState[key]);
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
let activityDirty = true;
const activityVisible = () => $("activityView").classList.contains("active");
const projectById = () => new Map(projects.map(project => [project.id, project]));
const isProjectActivity = event => String(event.type || "").startsWith("project_");
const activityKind = event => isProjectActivity(event) ? "project" : event.type;
const projectForEvent = (event, map=projectById()) => map.get(event.project_id) || event.project || null;


function combinedActivityEvents() {
  const events=[...activityData.events];
  const seen=new Set(events.map(event=>event.type+":"+event.project_id+":"+(event.sha||event.tag||event.url||event.date)));
  for(const project of projects){
    const release=project.github?.latest_release;
    if(!release?.published_at) continue;
    const tag=release.tag||release.name||"release";
    const key="release:"+project.id+":"+tag;
    if(seen.has(key)) continue;
    seen.add(key);
    events.push({
      type:"release",
      date:release.published_at+"T12:00:00Z",
      project_id:project.id,
      repository:project.github?.repository||"",
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

function initActivityFilters() {
  const eventProjects=activityData.events.map(event=>event.project).filter(Boolean);
  const filterProjects=[...projects,...eventProjects];
  bindFacet("activityTypeFacet",["commit","release","project"],activityFilterState.type,
    value=>({commit:"Commits",release:"Releases",project:"Project changes"}[value]||value),
    ()=>{updateClearButtons();requestActivityRender();});
  bindFacet("activityProjectTypeFacet",["software","tools"],activityFilterState.projectType,projectTypeLabel,()=>{updateClearButtons();requestActivityRender();});
  bindFacet("activityPlatformFacet",filterProjects.flatMap(platformValues),activityFilterState.platform,value=>value,()=>{updateClearButtons();requestActivityRender();});
  bindFacet("activityCpuFacet",filterProjects.flatMap(cpuFamilyValues),activityFilterState.cpu,value=>value,()=>{updateClearButtons();requestActivityRender();});
  bindFacet("activityTargetKindFacet",filterProjects.flatMap(p=>arr(p.target_kinds)),activityFilterState.targetKind,classificationLabel,()=>{updateClearButtons();requestActivityRender();});
  bindFacet("activityWorkKindFacet",filterProjects.flatMap(p=>arr(p.work_kinds)),activityFilterState.workKind,classificationLabel,()=>{updateClearButtons();requestActivityRender();});
  bindFacet("activityToolKindFacet",filterProjects.flatMap(p=>arr(p.tool_kinds)),activityFilterState.toolKind,classificationLabel,()=>{updateClearButtons();requestActivityRender();});
  bindSegment("activityDaysSegment",activityFilterState,"days",()=>{updateClearButtons();requestActivityRender();});
  bindSegment("activityAiSegment",activityFilterState,"ai",()=>{updateClearButtons();requestActivityRender();});
}

function activityMatches(event) {
  const project=projectForEvent(event);
  if(!project) return false;
  const cutoff=Date.now()-Number(activityFilterState.days||30)*86400000;
  if(new Date(event.date).getTime()<cutoff) return false;
  const q=$("activityQ").value.trim().toLowerCase();
  const hay=[
    event.type,event.title,event.message,event.repository,event.tag,
    projectTitle(project),project.title,project.upstream_name,...arr(project.subjects),
    ...projectTypeValues(project).map(projectTypeLabel),...platformValues(project),...cpuFamilyValues(project),
    ...arr(project.target_kinds),...arr(project.work_kinds),...arr(project.tool_kinds),
    ...arr(project.tags),...arr(project.ai?.tools),
    ...arr(event.changes),JSON.stringify(event.change_details||[])
  ].join(" ").toLowerCase();
  return (!q||hay.includes(q))
    && facetMatch(activityFilterState.type,[activityKind(event)])
    && facetMatch(activityFilterState.projectType,projectTypeValues(project))
    && facetMatch(activityFilterState.platform,platformValues(project))
    && facetMatch(activityFilterState.cpu,cpuFamilyValues(project))
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
  const url=project.project_url||project.repo;
  const title=url?'<a href="'+esc(url)+'" target="_blank" rel="noopener">'+esc(projectTitle(project))+'</a>':esc(projectTitle(project));
  return '<strong>'+title+'</strong>'+activityPlatformTags(project)+classificationTags(project,{compact:true});
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
  source_platforms:"Source platform",
  target_platforms:"Target platform",
  source_cpu:"Source CPU",
  source_language:"Source language",
  reconstructed_languages:"Output language",
  target_cpu:"Target CPU",
  runtime_profiles:"Runtime compatibility",
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

function projectChangeHtml(event) {
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
  const date=new Date(value);
  if(Number.isNaN(date.getTime())) return String(value||"").slice(0,10);
  return [
    date.getFullYear(),
    String(date.getMonth()+1).padStart(2,"0"),
    String(date.getDate()).padStart(2,"0")
  ].join("-");
}

function localDayLabel(day) {
  const [year,month,date]=day.split("-").map(Number);
  return new Date(year,month-1,date).toLocaleDateString(
    undefined,
    {weekday:"long",year:"numeric",month:"long",day:"numeric"}
  );
}

function renderActivity() {
  activityDirty=false;
  const map=projectById();
  const events=combinedActivityEvents().filter(activityMatches).sort((a,b)=>new Date(b.date)-new Date(a.date));
  $("activityCount").textContent=events.length;
  $("activityProjectCount").textContent=new Set(events.map(e=>e.project_id)).size;

  if(!events.length){
    $("activityFeed").innerHTML='<div class="activity-empty">No activity matches the current filters.</div>';
    return;
  }

  const days=new Map();
  for(const event of events){
    const day=localDayKey(event.date);
    if(!days.has(day)) days.set(day,new Map());
    const byProject=days.get(day);
    if(!byProject.has(event.project_id)) byProject.set(event.project_id,[]);
    byProject.get(event.project_id).push(event);
  }

  $("activityFeed").innerHTML=[...days.entries()].map(([day,byProject])=>{
    const dateLabel=localDayLabel(day);
    const projectsHtml=[...byProject.entries()].sort((a,b)=>{
      const ad=Math.max(...a[1].map(e=>new Date(e.date).getTime()));
      const bd=Math.max(...b[1].map(e=>new Date(e.date).getTime()));
      return bd-ad;
    }).map(([projectId,commits])=>{
      const project=map.get(projectId) || commits.find(event=>event.project)?.project;
      const commitHtml=commits.sort((a,b)=>new Date(b.date)-new Date(a.date)).map(event=>{
        const time=new Date(event.date).toLocaleTimeString(undefined,{hour:"2-digit",minute:"2-digit",hour12:false});
        const title=event.url?'<a href="'+esc(event.url)+'" target="_blank" rel="noopener">'+esc(event.title)+'</a>':esc(event.title);
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
            +'<div class="activity-change-lines">'+projectChangeHtml(event)+'</div>';
        }else{
          if(event.author) detailParts.push('<span class="activity-author">'+esc(event.author)+'</span>');
          if(identity) detailParts.push('<span class="activity-identity">'+identity+'</span>');
          for(const branch of arr(event.branches)){
            detailParts.push('<span class="branch">'+esc(branch)+'</span>');
          }
          details=detailParts.join('<span class="detail-separator">·</span>');
        }
        const classes=event.type==="release"?"commit release-event":(isProjectActivity(event)?"commit project-event":"commit");
        return '<div class="'+classes+'"><div class="commit-time">'+time+'</div><div class="commit-main"><div class="commit-title">'+title+'</div><div class="commit-detail">'+details+'</div></div></div>';
      }).join("");
      return '<div class="activity-project"><div class="activity-project-head">'+activityProjectHeader(project)+'</div><div class="commit-list">'+commitHtml+'</div></div>';
    }).join("");
    return '<section class="activity-day"><h2>'+esc(dateLabel)+'</h2>'+projectsHtml+'</section>';
  }).join("");
}

function requestActivityRender(){
  activityDirty=true;
  if(activityVisible()) renderActivity();
}

document.querySelectorAll(".view-tab").forEach(button=>button.addEventListener("click",()=>{
  if(button.classList.contains("active")) return;
  document.querySelectorAll(".view-tab").forEach(x=>x.classList.toggle("active",x===button));
  document.querySelectorAll(".view-panel").forEach(panel=>panel.classList.toggle("active",panel.id===button.dataset.view));
  if(button.dataset.view==="activityView" && activityDirty) renderActivity();
}));

$("activityQ").addEventListener("input",()=>{updateClearButtons();requestActivityRender();});
$("activityClear").addEventListener("click",()=>{
  $("activityQ").value="";
  for(const key of ["type","projectType","platform","cpu","targetKind","workKind","toolKind"]) clearFacetSet(activityFilterState[key]);
  activityFilterState.ai="";
  activityFilterState.days="30";
  clearFacetButtons($("activityView"));
  resetSegment("activityDaysSegment","30");
  resetSegment("activityAiSegment","");
  updateClearButtons();
  requestActivityRender();
});

Promise.all([
  fetch("data/projects.json",{cache:"no-cache"}).then(r=>{if(!r.ok)throw new Error("projects HTTP "+r.status);return r.json()}),
  fetch("data/activity.json",{cache:"no-cache"}).then(r=>{if(!r.ok)throw new Error("activity HTTP "+r.status);return r.json()})
]).then(([projectData,activity])=>{
  activityData=activity;
  projects=projectData;
  $("dataFreshness").textContent=formatFreshness(activityData.generated_at);
  init();
  initActivityFilters();
  updateClearButtons();
  renderActivity();
}).catch(error=>{
  $("activityFeed").innerHTML='<div class="activity-empty">Could not load activity: '+esc(error.message)+'</div>';
});
