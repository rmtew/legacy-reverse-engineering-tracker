#!/usr/bin/env python3
"""Build web/projects.json from the constrained YAML records in projects/.

No third-party packages are required.
"""
from pathlib import Path
import json
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
        indent=len(raw)-len(raw.lstrip()); k,_,v=raw.strip().partition(":")
        if indent==0:
            if not v.strip(): d[k]={}; parent=k
            else: d[k]=scalar(v); parent=None
        elif parent: d[parent][k]=scalar(v)
    return d

records=[load(p) for p in sorted((ROOT/"projects").rglob("*.yml"))]
out=ROOT/"web"/"projects.json"; out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(records,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(f"Wrote {len(records)} records to {out}")
