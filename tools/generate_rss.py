#!/usr/bin/env python3
"""Generate a low-noise RSS 2.0 feed from tracker activity.

Commit activity is published after its UTC day closes, so daily items do not
repeat earlier commits as the day progresses. Catalogue changes and releases
remain separate items.
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
# Existing catalogue history was never in RSS. Start with future changes so
# the first deployment does not send hundreds of retrospective notifications.
CATALOG_FEED_START = "2026-09-25T21:57:35Z"
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
    """Return settled project/UTC-day items using only post-discovery commits."""
    tracked_since = {}
    for event in activity.get("events", []):
        if event.get("type") in ("project_added", "project_restored"):
            project_id = event.get("project_id")
            if project_id not in tracked_since or event["date"] < tracked_since[project_id]:
                tracked_since[project_id] = event["date"]
    current_day = str(activity.get("generated_at") or "")[:10]
    grouped = defaultdict(list)
    for event in activity.get("events", []):
        if event.get("type") != "commit" or not event.get("sha") or not event.get("date"):
            continue
        if event["date"][:10] >= current_day or event["date"] < tracked_since.get(event.get("project_id"), ""):
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


def change_description(event, project):
    bits = [release_description({"message": ""}, project)]
    context = event.get("activity_context") or {}
    commit = context.get("last_commit") or {}
    last_activity = commit.get("date") or context.get("last_activity")
    if last_activity:
        label = "Last commit" if commit.get("date") else "Last upstream activity"
        bits.append("<p><strong>" + label + ":</strong> " + html.escape(last_activity) + "</p>")
    release = context.get("latest_release") or {}
    if release.get("published_at"):
        tag = release.get("tag") or release.get("name") or "Release"
        bits.append("<p><strong>Latest release:</strong> " + html.escape(tag + " · " + release["published_at"]) + "</p>")
    if "commits_90d" in context:
        bits.append("<p><strong>Last 90 days:</strong> " + str(context["commits_90d"]) +
                    " commits across " + str(context.get("active_days_90d", 0)) + " active days</p>")
    elif event.get("type") in ("project_added", "project_restored"):
        bits.append("<p>Initial activity scan pending.</p>")
    changes = event.get("changes") or []
    if changes:
        bits.append("<p><strong>Changed:</strong> " + html.escape(", ".join(field.replace("_", " ") for field in changes)) + "</p>")
    return "".join(bits)


def generate(activity_path, projects_path, output_path, limit):
    activity = json.loads(activity_path.read_text(encoding="utf-8"))
    projects = json.loads(projects_path.read_text(encoding="utf-8"))
    by_id = {project["id"]: project for project in projects if project.get("id")}

    events = aggregate_commit_days(activity)
    events.extend(release_events(projects))
    events.extend(event for event in activity.get("events", [])
                  if str(event.get("type", "")).startswith("project_")
                  and str(event.get("date") or "") > CATALOG_FEED_START)
    events.sort(key=lambda event: event.get("date") or "", reverse=True)
    events = events[:limit]

    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "Retro Development Project Tracker — Activity"
    ET.SubElement(channel, "link").text = SITE_URL
    ET.SubElement(channel, "description").text = (
        "Daily project activity summaries and releases across tracked reverse engineering, "
        "reconstruction, preservation, homebrew and retro-development tooling projects."
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
        project = by_id.get(event.get("project_id")) or event.get("project") or {}
        display_name = project_title(project, event.get("project_id"))
        item = ET.SubElement(channel, "item")

        if str(event.get("type", "")).startswith("project_"):
            kind = event["type"].replace("project_", "").replace("_", " ")
            ET.SubElement(item, "title").text = display_name + " — " + kind
            ET.SubElement(item, "link").text = event.get("url") or project.get("project_url") or project.get("repo") or SITE_URL
            guid = ET.SubElement(item, "guid", {"isPermaLink": "false"})
            guid.text = "legacy-re:" + str(event.get("project_id")) + ":" + event["type"] + ":" + str(event["date"])
            ET.SubElement(item, "description").text = change_description(event, project)
        elif event.get("type") == "release":
            tag = event.get("tag") or "release"
            ET.SubElement(item, "title").text = display_name + " — released " + tag
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
                display_name + " — " + str(count) + " " + noun + " on " + format_day(day)
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
