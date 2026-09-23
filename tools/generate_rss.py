#!/usr/bin/env python3
"""Generate an RSS 2.0 feed from the tracker activity database."""
from __future__ import annotations

import argparse
import html
import json
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
import xml.etree.ElementTree as ET

SITE_URL = "https://rmtew.github.io/legacy-reverse-engineering-tracker/"
FEED_URL = SITE_URL + "activity.xml"
DEFAULT_LIMIT = 200
ATOM_NS = "http://www.w3.org/2005/Atom"
ET.register_namespace("atom", ATOM_NS)


def parse_time(value):
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def rfc822(value):
    dt = parse_time(value)
    return format_datetime(dt.astimezone(timezone.utc)) if dt else None


def joined(value):
    if isinstance(value, list):
        return ", ".join(str(item) for item in value if item)
    return str(value or "")


def description(event, project):
    project_url = project.get("project_url") or project.get("repo") or SITE_URL
    title = project.get("title") or event.get("project_id") or "?"
    bits = [
        '<p><strong>Project:</strong> <a href="' +
        html.escape(project_url, quote=True) + '">' +
        html.escape(title) + '</a></p>'
    ]
    platforms = joined(project.get("source_platforms"))
    if platforms:
        bits.append("<p><strong>Platform:</strong> " + html.escape(platforms) + "</p>")
    branches = joined(event.get("branches"))
    if branches:
        bits.append("<p><strong>Branch:</strong> " + html.escape(branches) + "</p>")
    if event.get("author"):
        bits.append("<p><strong>Author:</strong> " + html.escape(str(event["author"])) + "</p>")
    message = (event.get("message") or event.get("title") or "").strip()
    if message:
        bits.append("<pre>" + html.escape(message[:5000]) + "</pre>")
    return "".join(bits)


def generate(activity_path, projects_path, output_path, limit):
    activity = json.loads(activity_path.read_text(encoding="utf-8"))
    projects = json.loads(projects_path.read_text(encoding="utf-8"))
    by_id = {project["id"]: project for project in projects if project.get("id")}

    events = [
        event for event in activity.get("events", [])
        if event.get("type") == "commit" and event.get("sha") and event.get("date")
    ]
    events.sort(key=lambda event: event.get("date") or "", reverse=True)
    events = events[:limit]

    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "Legacy Reverse Engineering Tracker — Activity"
    ET.SubElement(channel, "link").text = SITE_URL
    ET.SubElement(channel, "description").text = (
        "Recent commits across tracked legacy software reverse-engineering projects."
    )
    ET.SubElement(channel, "language").text = "en"
    ET.SubElement(channel, "atom:link", {
        "xmlns:atom": ATOM_NS,
        "href": FEED_URL,
        "rel": "self",
        "type": "application/rss+xml",
    })
    build_date = rfc822(activity.get("generated_at"))
    if build_date:
        ET.SubElement(channel, "lastBuildDate").text = build_date

    for event in events:
        project = by_id.get(event.get("project_id"), {})
        project_title = project.get("title") or event.get("project_id") or "Unknown project"
        commit_title = event.get("title") or (event.get("sha") or "")[:12]
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = project_title + " — " + commit_title
        link = event.get("url") or project.get("project_url") or project.get("repo") or SITE_URL
        ET.SubElement(item, "link").text = link
        guid = ET.SubElement(item, "guid", {"isPermaLink": "false"})
        guid.text = "legacy-re:" + str(event.get("project_id")) + ":" + str(event.get("sha"))
        pub_date = rfc822(event.get("date"))
        if pub_date:
            ET.SubElement(item, "pubDate").text = pub_date
        ET.SubElement(item, "description").text = description(event, project)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    tree = ET.ElementTree(rss)
    ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("activity", type=Path)
    parser.add_argument("projects", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    args = parser.parse_args()
    generate(args.activity, args.projects, args.output, max(1, args.limit))


if __name__ == "__main__":
    main()
