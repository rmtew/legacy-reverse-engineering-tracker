"""Canonical execution methods. No architecture is inferred from names or prose."""
from copy import deepcopy

METHODS = frozenset({'baked-emulation', 'native-translation'})


def check_methods(project):
    for path in project.get('execution_paths') or []:
        if isinstance(path, dict) and path.get('method') not in METHODS:
            raise ValueError('Invalid canonical execution method: ' + str(path.get('method')))


def research_v1_project(project):
    """Decode the historical research-records/v1 spelling AFTER seal verification.

    Never mutate signed input, evidence text, expected hashes or receipts. Native
    translation is not reclassified here: that requires reviewed architecture.
    """
    project = deepcopy(project)
    for path in project.get('execution_paths') or []:
        if isinstance(path, dict) and path.get('method') == 'game-specific-emulation':
            path['method'] = 'baked-emulation'
    return project


def activity_v1_event(event):
    """Read legacy activity snapshots/details into a PUBLIC projection only.

    The retained event and its historical before/after evidence stay unchanged.
    The browser needs no old machine-key/search alias.
    """
    event = deepcopy(event)
    if isinstance(event.get('project'), dict):
        event['project'] = research_v1_project(event['project'])
    for detail in event.get('change_details') or []:
        if detail.get('field') == 'execution_paths':
            for key in ('before', 'after'):
                if key in detail:
                    detail[key] = research_v1_project({'execution_paths': detail[key]})['execution_paths']
    return event
