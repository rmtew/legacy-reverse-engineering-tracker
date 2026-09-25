"""Build compact browser feeds from the canonical 180-day activity history."""

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def timestamp(value):
    date = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return date.replace(tzinfo=timezone.utc) if date.tzinfo is None else date


def recent_activity(activity, days=30):
    cutoff = timestamp(activity["generated_at"]) - timedelta(days=days)
    events = []
    for event in activity["events"]:
        if timestamp(event["date"]) < cutoff:
            continue
        browser_event = dict(event)
        if event["type"] == "commit":
            browser_event.pop("message", None)  # The page displays/searches the subject.
        elif event["type"] == "daily_commits":
            browser_event.pop("shas", None)  # Used by the collector, not the UI.
        events.append(browser_event)
    return {
        "generated_at": activity["generated_at"],
        "window_days": days,
        "events": events,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--days", type=int, default=30)
    args = parser.parse_args()
    activity = json.loads(args.source.read_text(encoding="utf-8"))
    output = recent_activity(activity, args.days)
    args.destination.parent.mkdir(parents=True, exist_ok=True)
    args.destination.write_text(json.dumps(output, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Generated {len(output['events'])} recent events from {len(activity['events'])} retained events")


if __name__ == "__main__":
    main()
