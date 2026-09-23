#!/usr/bin/env python3
"""Generate GitHub-friendly Markdown views from project YAML records.

No external dependencies. The parser accepts the intentionally constrained YAML
used by this repository: scalars, inline lists, and one-level nested mappings.
"""
from pathlib import Path
import ast, re
ROOT=Path(__file__).resolve().parents[1]

def scalar(s):
    s=s.strip()
    if s in ("yes","true"): return True
    if s in ("no","false"): return False
    if s in ("null","unknown",""): return None
    if s.startswith("[") and s.endswith("]"):
        body=s[1:-1].strip()
        return [] if not body else [x.strip().strip("'\"") for x in body.split(",")]
    return s.strip("'\"")

def load(path):
    d={}; parent=None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"): continue
        indent=len(raw)-len(raw.lstrip())
        k,_,v=raw.strip().partition(":")
        if indent==0:
            if v.strip()=="":
                d[k]={}; parent=k
            else:
                d[k]=scalar(v); parent=None
        elif parent:
            d[parent][k]=scalar(v)
    d["_path"]=path.relative_to(ROOT).as_posix()
    return d

def yn(v):
    return "Yes" if v is True else "No" if v is False else "?"

def vals(v):
    if isinstance(v,list): return ", ".join(v)
    return str(v or "?")

records=[load(p) for p in sorted((ROOT/"projects").rglob("*.yml"))]

def table(rs,title):
    lines=[f"# {title}","",f"{len(rs)} project records.","",
    "| Project | Source platform | Target platform | Output | Started | Last activity | Compiles | Playable | Exact | AI |",
    "|---|---|---|---|---:|---:|:---:|:---:|:---:|:---:|"]
    for r in rs:
        b=r.get("build",{}); ai=r.get("ai",{})
        link=f"[{r.get('title','?')}](../{r['_path']})"
        lines.append("| "+" | ".join([link,vals(r.get("source_platforms")),vals(r.get("target_platforms")),
          vals(r.get("reconstructed_languages")),vals(r.get("re_started")),vals(r.get("last_activity")),
          yn(b.get("compilable")),yn(b.get("playable")),yn(b.get("byte_exact")),yn(ai.get("usage"))])+" |")
    return "\n".join(lines)+"\n"

views={
 "all.md":(records,"All projects"),
 "amiga.md":([r for r in records if any("Amiga" in x for x in r.get("source_platforms",[]))],"Amiga"),
 "atari-st.md":([r for r in records if any("Atari ST" in x for x in r.get("source_platforms",[]))],"Atari ST"),
 "zx-spectrum.md":([r for r in records if any("ZX Spectrum" in x for x in r.get("source_platforms",[]))],"ZX Spectrum"),
 "c64.md":([r for r in records if any(x in ("C64","Commodore 64") for x in r.get("source_platforms",[]))],"Commodore 64"),
 "amstrad-cpc.md":([r for r in records if any("Amstrad CPC" in x for x in r.get("source_platforms",[]))],"Amstrad CPC"),
 "compilable.md":([r for r in records if r.get("build",{}).get("compilable") is True],"Compilable"),
 "playable.md":([r for r in records if r.get("build",{}).get("playable") is True],"Playable"),
 "byte-exact.md":([r for r in records if r.get("build",{}).get("byte_exact") is True],"Byte-exact"),
 "ai-assisted.md":([r for r in records if r.get("ai",{}).get("usage") is True],"Confirmed AI-assisted"),
 "assembly.md":([r for r in records if any("assembly" in x.lower() for x in r.get("reconstructed_languages",[]))],"Assembly output"),
}
out=ROOT/"views"; out.mkdir(exist_ok=True)
for name,(rs,title) in views.items():
    (out/name).write_text(table(sorted(rs,key=lambda r:r.get("title","").lower()),title),encoding="utf-8")
index="# Views\n\n"+" · ".join(f"[{title}](./{name})" for name,(_,title) in views.items())+"\n"
(out/"README.md").write_text(index,encoding="utf-8")
print(f"Generated {len(views)} views from {len(records)} records")
