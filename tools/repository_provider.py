"""Provider identities shared by collection and offline readers (no I/O)."""
import re
from urllib.parse import urlsplit


def repository(project):
    url = project.get('repo') or ''
    match = re.fullmatch(r'https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?', url)
    if match:
        return f'{match[1]}/{match[2]}'
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or parsed.netloc != 'gitlab.com' or parsed.query or parsed.fragment:
        return None
    path = parsed.path.strip('/').removesuffix('.git')
    parts = path.split('/')
    if len(parts) < 2 or any(not re.fullmatch(r'[\w.-]+', part) or part in ('.', '..', '-') for part in parts):
        return None
    return 'gitlab.com/' + path


def provider(project_or_key):
    key = repository(project_or_key) if isinstance(project_or_key, dict) else project_or_key
    return ('gitlab' if key.startswith('gitlab.com/') else 'github') if key else None


def metadata(project):
    kind = provider(project)
    if not kind and not project.get('repo'):
        kind = 'gitlab' if project.get('gitlab') else 'github'
    return project.get(kind or '', {}) or {}


def selectors(project):
    kind = provider(project) or 'github'
    return project.get(kind + '_branch'), project.get(kind + '_path')


def matches_branch(project, branch):
    selected, _ = selectors(project)
    return not selected or selected == branch
