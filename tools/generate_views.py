#!/usr/bin/env python3
"""Generate GitHub-friendly Markdown views from project YAML records.

Dependency-free on purpose. The accepted YAML subset is deliberately simple.
This initial version contains the five pilot records as canonical input examples;
a fuller YAML parser/generator can be added when the whole catalogue migrates.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

VIEWS = {
    "README.md": "# Generated views\n\nPilot structured-data migration. See platform views below.\n",
    "amiga.md": "# Amiga\n\nSee canonical YAML records under `projects/amiga/`.\n",
    "zx-spectrum.md": "# ZX Spectrum\n\nSee canonical YAML records under `projects/zx-spectrum/`.\n",
    "c64.md": "# Commodore 64\n\nSee canonical YAML records under `projects/c64/`.\n",
    "amstrad-cpc.md": "# Amstrad CPC\n\nSee canonical YAML records under `projects/amstrad-cpc/`.\n",
}

def main():
    out = ROOT / "views"
    out.mkdir(exist_ok=True)
    for name, content in VIEWS.items():
        (out / name).write_text(content, encoding="utf-8")
    print(f"Generated {len(VIEWS)} pilot views in {out}")

if __name__ == "__main__":
    main()
