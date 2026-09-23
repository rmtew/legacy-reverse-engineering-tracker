// Supplement generated activity with each project's latest known commit/release.
// This keeps the feed useful when data/activity.json has not yet collected a
// repository's recent commit history (for example, a newly added project).
function combinedActivityEvents() {
  const events = [...activityData.events];
  const seen = new Set(events.map(event =>
    event.type + ":" + event.project_id + ":" + (event.sha || event.tag || event.url || event.date)
  ));

  for (const project of projects) {
    const commit = project.github?.latest_commit;
    if (commit?.date) {
      const identity = commit.sha || commit.url || commit.date;
      const key = "commit:" + project.id + ":" + identity;
      if (!seen.has(key)) {
        seen.add(key);
        events.push({
          type: "commit",
          date: commit.date.length === 10 ? commit.date + "T12:00:00Z" : commit.date,
          project_id: project.id,
          repository: project.github?.repository || "",
          sha: commit.sha || "",
          title: commit.message || (commit.sha ? "Commit " + commit.sha.slice(0, 8) : "Latest commit"),
          message: commit.message || "",
          url: commit.url || project.repo || project.project_url,
          author: "",
          branches: [project.github?.tracking_branch || project.github?.default_branch].filter(Boolean)
        });
      }
    }

    const release = project.github?.latest_release;
    if (!release?.published_at) continue;
    const tag = release.tag || release.name || "release";
    const key = "release:" + project.id + ":" + tag;
    if (seen.has(key)) continue;
    seen.add(key);
    events.push({
      type: "release",
      date: release.published_at.length === 10 ? release.published_at + "T12:00:00Z" : release.published_at,
      project_id: project.id,
      repository: project.github?.repository || "",
      tag,
      title: "Release " + tag,
      message: release.name && release.name !== tag ? release.name : "",
      url: release.url || project.project_url || project.repo,
      author: "",
      branches: []
    });
  }

  return events;
}

// If the main data load happened unusually quickly, redraw with the fallback.
if (projects.length) renderActivity();
