#!/usr/bin/env python3
"""Build and validate one pinned, complete public site snapshot."""

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil

from generate_recent_activity import recent_activity
from generate_rss import DEFAULT_LIMIT, generate
from validate_site_data import validate


def build(root, destination):
    if destination.exists():
        raise ValueError("Use a new site destination")
    destination.mkdir(parents=True)
    shutil.copy2(root / "index.html", destination / "index.html")
    for name in ("web", "data"):
        shutil.copytree(root / name, destination / name)
    index = destination / "index.html"
    html = index.read_text()
    for asset in ("tracker.css", "tracker.js"):
        path = "web/" + asset
        digest = sha256((destination / path).read_bytes()).hexdigest()[:12]
        html, count = re.subn(re.escape(path) + r'(?:\?v=[^"\s]*)?', path + "?v=" + digest, html)
        if count != 1:
            raise ValueError(f"Expected one reference to {path}, found {count}")
    index.write_text(html)
    (destination / ".nojekyll").touch()
    generate(
        root / "data/activity.json", root / "data/projects.json", destination / "activity.xml", DEFAULT_LIMIT
    )
    activity = json.loads((root / "data/activity.json").read_bytes())
    for days in (30, 180):
        (destination / f"data/activity-{days}d.json").write_text(
            json.dumps(recent_activity(activity, days), ensure_ascii=False, separators=(",", ":")) + "\n"
        )
    validate(
        destination / "data/projects.json", destination / "data/activity.json", destination / "activity.xml"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--destination", type=Path, default=Path("_site"))
    args = parser.parse_args()
    build(args.root, args.destination)
