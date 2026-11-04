"""Catalogue change snapshots include authored provider selectors, not probes."""

import unittest

from record_project_activity import MOVE_FIELDS, changed_fields, snapshot


class ProjectActivitySnapshotTest(unittest.TestCase):
    def test_gitlab_selectors_are_material_location_changes(self):
        before = {"id": "p", "repo": "https://gitlab.com/group/subgroup/project",
                  "gitlab_branch": "main", "gitlab_path": "game"}
        for field, value in (("gitlab_branch", "port"), ("gitlab_path", "engine")):
            with self.subTest(field=field):
                after = {**before, field: value}
                fields = changed_fields(snapshot(before), snapshot(after))
                self.assertEqual(fields, [field])
                self.assertIn(field, MOVE_FIELDS)

    def test_gitlab_refresh_metadata_does_not_become_a_catalogue_change(self):
        before = {"id": "p", "repo": "https://gitlab.com/a/b"}
        after = {**before, "last_activity": "2026-10-01", "gitlab": {
            "repository": "gitlab.com/a/b", "checked_at": "2026-10-01",
            "latest_release": {"tag": "v1", "published_at": "2026-10-01"}}}
        self.assertEqual(snapshot(before), snapshot(after))

    def test_new_absent_selectors_do_not_change_existing_catalogue_snapshots(self):
        project = {"id": "p", "repo": "https://github.com/a/b"}
        before = snapshot(project)
        before.pop("gitlab_branch")
        before.pop("gitlab_path")
        self.assertEqual(changed_fields(before, snapshot(project)), [])


if __name__ == "__main__":
    unittest.main()
