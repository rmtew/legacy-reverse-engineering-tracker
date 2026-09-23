#!/usr/bin/env python3
"""Generate a low-noise RSS 2.0 feed from tracker activity.

Commit activity is aggregated into one RSS item per project per UTC calendar day.
Releases remain separate RSS items.
"""
from __future__ import annotations

import argparse
import html
import json
from collections import defaultdict
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
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
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


def project_title(project, fallback=None):
    return (
        project.get("display_title")
        or project.get("title")
        or project.get("upstream_name")
        or fallback
        or "Unknown project"
    )


def project_platforms(project):
    source = joined(project.get("source_platforms"))
    target = joined(project.get("target_platforms"))
    if source and target and source != target:
        return source + " → " + target
    return source or target


def format_day(day):
    try:
        return datetime.strptime(day, "%Y-%m-%d").strftime("%-d %B %Y")
    except (ValueError, OSError):
        # %-d is not portable to Windows; Pages builds on Linux, but keep a fallback.
        try:
            return datetime.strptime(day, "%Y-%m-%d").strftime("%d %B %Y").lstrip("0")
        except ValueError:
            return day


def release_events(projects):
    events = []
    for project in projects:
        release = (project.get("github") or {}).get("latest_release") or {}
        published = release.get("published_at")
        if not published:
            continue
        tag = release.get("tag") or release.get("name") or "release"
        events.append({
            "type": "release",
            "date": published + "T12:00:00Z",
            "project_id": project.get("id"),
            "repository": (project.get("github") or {}).get("repository"),
            "tag": tag,
            "title": "Release " + tag,
            "message": release.get("name") if release.get("name") != tag else "",
            "url": release.get("url") or project.get("project_url") or project.get("repo"),
        })
    return events


def aggregate_commit_days(activity):
    """Return one event per project per UTC day."""
    grouped = defaultdict(list)
    for event in activity.get("events", []):
        if event.get("type") != "commit" or not event.get("sha") or not event.get("date"):
            continue
        grouped[(event.get("project_id"), str(event["date"])[:10])].append(event)

    summaries = []
    for (project_id, day), commits in grouped.items():
        commits.sort(key=lambda event: event.get("date") or "", reverse=True)
        latest = commits[0]
        authors = sorted({str(event.get("author")) for event in commits if event.get("author")})
        branches = sorted({
            str(branch)
            for event in commits
            for branch in (event.get("branches") or [])
            if branch
        })
        summaries.append({
            "type": "daily_commits",
            "date": latest.get("date"),
            "day": day,
            "project_id": project_id,
            "repository": latest.get("repository"),
            "commits": commits,
            "authors": authors,
            "branches": branches,
            "count": len(commits),
        })
    return summaries


def daily_description(event, project):
    project_url = project.get("project_url") or project.get("repo") or SITE_URL
    title = project_title(project, event.get("project_id") or "?")
    bits = [
        '<p><strong>Project:</strong> <a href="' +
        html.escape(project_url, quote=True) + '">' +
        html.escape(title) + '</a></p>'
    ]

    platforms = project_platforms(project)
    if platforms:
        bits.append("<p><strong>Platforms:</strong> " + html.escape(platforms) + "</p>")

    if event.get("authors"):
        bits.append("<p><strong>Authors:</strong> " + html.escape(", ".join(event["authors"])) + "</p>")
    if event.get("branches"):
        bits.append("<p><strong>Branches:</strong> " + html.escape(", ".join(event["branches"])) + "</p>")

    bits.append("<ul>")
    for commit in event.get("commits", []):
        commit_url = commit.get("url")
        title_text = commit.get("title") or (commit.get("sha") or "")[:12]
        label = html.escape(title_text)
        if commit_url:
            label = '<a href="' + html.escape(commit_url, quote=True) + '">' + label + '</a>'

        meta = []
        if commit.get("author"):
            meta.append(html.escape(str(commit["author"])))
        if commit.get("sha"):
            meta.append(html.escape(str(commit["sha"])[:8]))
        branches = commit.get("branches") or []
        if branches:
            meta.append(html.escape(", ".join(branches)))

        suffix = " — " + " · ".join(meta) if meta else ""
        bits.append("<li>" + label + suffix + "</li>")
    bits.append("</ul>")
    return "".join(bits)


def release_description(event, project):
    project_url = project.get("project_url") or project.get("repo") or SITE_URL
    title = project_title(project, event.get("project_id") or "?")
    bits = [
        '<p><strong>Project:</strong> <a href="' +
        html.escape(project_url, quote=True) + '">' +
        html.escape(title) + '</a></p>'
    ]
    platforms = project_platforms(project)
    if platforms:
        bits.append("<p><strong>Platforms:</strong> " + html.escape(platforms) + "</p>")
    if event.get("message"):
        bits.append("<p>" + html.escape(str(event["message"])) + "</p>")
    return "".join(bits)


def generate(activity_path, projects_path, output_path, limit):
    activity = json.loads(activity_path.read_text(encoding="utf-8"))
    projects = json.loads(projects_path.read_text(encoding="utf-8"))
    by_id = {project["id"]: project for project in projects if project.get("id")}

    events = aggregate_commit_days(activity)
    events.extend(release_events(projects))
    events.sort(key=lambda event: event.get("date") or "", reverse=True)
    events = events[:limit]

    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "Legacy Reverse Engineering Tracker — Activity"
    ET.SubElement(channel, "link").text = SITE_URL
    ET.SubElement(channel, "description").text = (
        "Daily project activity summaries and releases across tracked legacy software "
        "reverse-engineering projects."
    )
    ET.SubElement(channel, "language").text = "en"
    ET.SubElement(channel, "{" + ATOM_NS + "}link", {
        "href": FEED_URL,
        "rel": "self",
        "type": "application/rss+xml",
    })
    build_date = rfc822(activity.get("generated_at"))
    if build_date:
        ET.SubElement(channel, "lastBuildDate").text = build_date

    for event in events:
        project = by_id.get(event.get("project_id"), {})
        project_title = project_title(project, event.get("project_id"))
        item = ET.SubElement(channel, "item")

        if event.get("type") == "release":
            tag = event.get("tag") or "release"
            ET.SubElement(item, "title").text = project_title + " — released " + tag
            link = event.get("url") or project.get("project_url") or project.get("repo") or SITE_URL
            ET.SubElement(item, "link").text = link
            guid = ET.SubElement(item, "guid", {"isPermaLink": "false"})
            guid.text = "legacy-re:" + str(event.get("project_id")) + ":release:" + str(tag)
            ET.SubElement(item, "description").text = release_description(event, project)
        else:
            count = int(event.get("count") or 0)
            noun = "commit" if count == 1 else "commits"
            day = event.get("day") or str(event.get("date") or "")[:10]
            ET.SubElement(item, "title").text = (
                project_title + " — " + str(count) + " " + noun + " on " + format_day(day)
            )
            link = project.get("project_url") or project.get("repo") or SITE_URL
            ET.SubElement(item, "link").text = link
            guid = ET.SubElement(item, "guid", {"isPermaLink": "false"})
            guid.text = "legacy-re:" + str(event.get("project_id")) + ":day:" + str(day)
            ET.SubElement(item, "description").text = daily_description(event, project)

        pub_date = rfc822(event.get("date"))
        if pub_date:
            ET.SubElement(item, "pubDate").text = pub_date

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
