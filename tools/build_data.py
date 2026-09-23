#!/usr/bin/env python3
"""Build web/projects.json from canonical project YAML records.

The repository intentionally uses a small YAML subset so this tool has no
third-party dependencies: scalars, inline lists, and one-level nested mappings.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def scalar(value):
    value=value.strip()
    if value in ("yes","true"): return True
    if value in ("no","false"): return False
    if value in ("null","unknown",""): return None
    if value.startswith("[") and value.endswith("]"):
        body=value[1:-1].strip()
        return [] if not body else [item.strip().strip("'\"") for item in body.split(",")]
    return value.strip("'\"")

def load_record(path):
    record={}
    parent=None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent=len(raw)-len(raw.lstrip())
        key,sep,value=raw.strip().partition(":")
        if not sep:
            raise ValueError(f"{path}: malformed line: {raw!r}")
        if indent==0:
            if value.strip():
                record[key]=scalar(value)
                parent=None
            else:
                record[key]={}
                parent=key
        elif parent:
            record[parent][key]=scalar(value)
        else:
            raise ValueError(f"{path}: unexpected indentation: {raw!r}")
    record["_record_path"]=path.relative_to(ROOT).as_posix()
    return record

def validate(record,path):
    required=("id","title","source_platforms","target_platforms","reconstructed_languages","types")
    missing=[key for key in required if key not in record]
    if missing:
        raise ValueError(f"{path}: missing required fields: {', '.join(missing)}")

paths=sorted((ROOT/"projects").rglob("*.yml"))
records=[]
ids=set()
for path in paths:
    record=load_record(path)
    validate(record,path)
    if record["id"] in ids:
        raise ValueError(f"duplicate project id: {record['id']}")
    ids.add(record["id"])
    records.append(record)

records.sort(key=lambda r:(str(r.get("title") or "").casefold(),r["id"]))
output=ROOT/"web"/"projects.json"
output.parent.mkdir(exist_ok=True)
output.write_text(json.dumps(records,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(f"Wrote {len(records)} project records to {output.relative_to(ROOT)}")
