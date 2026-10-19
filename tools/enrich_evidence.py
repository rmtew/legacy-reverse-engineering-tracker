#!/usr/bin/env python3
from __future__ import annotations
import re
import routine_metadata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"projects.json"
RAW="https://raw.githubusercontent.com"
API="https://api.github.com"
TODAY=datetime.now(timezone.utc).date().isoformat()
COLLECTOR="github-docs-v4"
MAX=700_000
DOCS=["README.md","README","readme.md","STATUS.md","status.md","BUILD.md","build.md","BUILDING.md","building.md","NOTES.md","notes.md"]
ROOT_EXTRA=["docs/README.md","docs/STATUS.md","docs/status.md","docs/BUILD.md","docs/build.md"]

POS_COMPILE=[
 re.compile(r"\b(?:game|source|code|disassembly|listing|rom|firmware|project)\s+(?:now\s+)?(?:compiles|assembles|reassembles|builds)\b",re.I),
 re.compile(r"\b(?:game|project|program|source|code|disassembly|listing|rom|firmware)\s+(?:can|may)\s+(?:be\s+)?(?:compiled|built|assembled|reassembled)\b",re.I),
 re.compile(r"\byou can (?:compile|build|assemble|reassemble)(?:\s+and\s+run)?\b",re.I),
 re.compile(r"\b(?:compile|build|assemble|reassemble) and run\b",re.I),
 re.compile(r"\bassemble the game back to a binary\b",re.I),
 re.compile(r"\bre-assemble this code\b",re.I),
]
NEG_COMPILE=[re.compile(r"\b(?:does not|doesn't|cannot|can't)\s+(?:compile|build|assemble|reassemble)\b",re.I),re.compile(r"\bnot compilable\b",re.I)]
POS_PLAY=[
 re.compile(r"\b(?:build|reconstruction|reconstructed version|prg|binary|game)\s+(?:is\s+)?playable\b",re.I),
 re.compile(r"\b(?:build|reconstruction|reconstructed version|prg|binary|game)\s+(?:now\s+)?plays(?:\s+well)?\b",re.I),
 re.compile(r"\b(?:game|source|code)\s+compiles and plays\b",re.I),
 re.compile(r"\bplayable\s+(?:prg|binary|build|version|game)\b",re.I),
 re.compile(r"\bboots? and plays\b",re.I),
]
NEG_PLAY=[re.compile(r"\bnot playable\b",re.I),re.compile(r"\b(?:game|build|reconstruction|version)\s+(?:does not|doesn't) play\b",re.I)]
POS_BYTE=[
 re.compile(r"\b(?:source|disassembly|listing|file|image)\b[^.\n]{0,120}\b(?:byte[- ]for[- ]byte identical|byte[- ]identical|byte[- ]exact|bit[- ]for[- ]bit identical)\b",re.I),
 re.compile(r"\b(?:rebuilt|reassembled|compiled|generated|reconstructed|output)\s+(?:binary|rom|snapshot|executable|cartridge|image)\b[^.\n]{0,120}\b(?:byte[- ]identical|byte[- ]exact|bit[- ]for[- ]bit identical|exactly the same|identical to)\b",re.I),
 re.compile(r"\b(?:reproduce|reproduces|reproduced|reproducing)\b[^.\n]{0,100}\b(?:every byte|byte[- ]for[- ]byte|exactly|identical)\b",re.I),
 re.compile(r"\bgenerates? (?:the )?(?:exactly |exact )?same binary as (?:the )?original\b",re.I),
 re.compile(r"\bbyte[- ]exact round[- ]trip\b",re.I),
]
NEG_BYTE=[re.compile(r"\bnot byte[- ](?:exact|identical)\b",re.I),re.compile(r"\bnot bit[- ]for[- ]bit\b",re.I)]
GOAL=re.compile(r"\b(?:goal|aim|target|intended|intention|trying|attempt|want|planned|plans?|eventually|hope)\b",re.I)
# build.byte_exact is specifically about a rebuilt original-program binary.  Do
# not promote asset/data conversions merely because they reproduce their source
# bytes exactly; those are useful verification signals but a different claim.
BYTE_REJECT=re.compile(r"\b(?:goal|aim|target|intended|intention|trying|attempt|want|planned|plans?|eventually|hope|asset|assets|art|artwork|resource|resources|data file|data files|converter|conversion|texture|textures|sprite|sprites|sound|music)\b",re.I)
START=[
 re.compile(r"\b(?:project|work|reverse[- ]engineering|disassembly)\s+(?:was\s+)?(?:started|began|commenced)\s+(?:in\s+)?((?:19|20)\d{2})\b",re.I),
 re.compile(r"\bi started (?:this|the) (?:project|work|reverse[- ]engineering|disassembly)[^0-9\n]{0,50}((?:19|20)\d{2})\b",re.I),
]
CI_NAME=re.compile(r"\b(?:build|test|tests|ci|compile|assemble|verify|verification)\b",re.I)
CI_EXCLUDE=re.compile(r"\b(?:pages?|deploy|deployment|docs?|documentation|website|site|lint|format)\b",re.I)

def repo_name(url):
 m=re.fullmatch(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?",url or "")
 return f"{m.group(1)}/{m.group(2)}" if m else None

def raw(repo,branch,path): return f"{RAW}/{repo}/{quote(branch,safe='')}/{quote(path,safe='/')}"
def blob(repo,branch,path): return f"https://github.com/{repo}/blob/{quote(branch,safe='')}/{quote(path,safe='/')}"

def clean(s):
 s=re.sub(r"<[^>]+>"," ",s);s=re.sub(r"\[([^\]]+)\]\([^\)]+\)",r"\1",s)
 return re.sub(r"\s+"," ",re.sub(r"[#*_\x60>|]"," ",s)).strip()[:280]

def ev(value,repo,branch,path,line,match):
 a=max(0,match.start()-120);b=min(len(line),match.end()+140)
 return {"value":value,"strength":"strong","source":path,"url":blob(repo,branch,path),"excerpt":clean(("…" if a else "")+line[a:b]+("…" if b<len(line) else "")),"checked_at":TODAY,"collector":COLLECTOR}

def uniq(xs):
 out=[];seen=set()
 for x in xs:
  k=(x["value"],x["source"],x["excerpt"])
  if k not in seen:seen.add(k);out.append(x)
 return out[:10]

def scan_bool(text,repo,branch,path,pos,neg,reject=None):
 out=[]
 for line in text.splitlines():
  line=line.strip()
  if not line or len(line)>1800:continue
  hit=False
  for p in neg:
   m=p.search(line)
   if m:out.append(ev(False,repo,branch,path,line,m));hit=True;break
  if hit:continue
  for p in pos:
   m=p.search(line)
   if m and not (reject and reject.search(line)):out.append(ev(True,repo,branch,path,line,m));break
 return uniq(out)

def scan_start(text,repo,branch,path):
 out=[];year=datetime.now(timezone.utc).year
 for line in text.splitlines():
  line=line.strip()
  if not line or len(line)>1800:continue
  for p in START:
   m=p.search(line)
   if m:
    y=int(m.group(1))
    if 1980<=y<=year:out.append(ev(y,repo,branch,path,line,m))
    break
 return uniq(out)

def one_value(xs):
 vals={x["value"] for x in xs if x.get("strength")=="strong"}
 return next(iter(vals)) if len(vals)==1 else None

def apply(record,auto):
 prev=((record.get("evidence") or {}).get("automated") or {}).get("applied") or {}
 build=record.setdefault("build",{})
 for field,val in prev.items():
  if field=="re_started":
   if record.get(field)==val:record[field]=None
  elif field.startswith("ai.") or field in ("source_cpu", "target_cpu", "source_platforms", "target_platforms"):
   pass  # Explicit source observations are historical facts, not volatile build status.
  elif build.get(field)==val:build[field]=None
 applied={}
 for field in ("compilable","playable","byte_exact"):
  val=one_value(auto[field])
  if val is not None and build.get(field) is None:build[field]=val;applied[field]=val
 val=one_value(auto["re_started"])
 if val is not None and record.get("re_started") is None:record["re_started"]=val;applied["re_started"]=val
 if build.get("playable") is True and build.get("runnable") is None:build["runnable"]=True;applied["runnable"]=True
 applied.update(routine_metadata.apply(record, auto))
 if applied:auto["applied"]=applied
 evidence=record.setdefault("evidence",{})
 if any(auto.get(k) for k in ("compilable","playable","byte_exact","re_started","ci","ai_use","ai_config","source_cpu","target_cpu","source_platforms","target_platforms")):evidence["automated"]=auto
 else:
  evidence.pop("automated",None)
  if not evidence:record.pop("evidence",None)
 return applied

def main():
 from enrichment_pipeline import main as bounded_main
 bounded_main()

if __name__=="__main__":main()
