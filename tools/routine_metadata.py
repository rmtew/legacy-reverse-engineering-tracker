"""Conservative, deterministic extraction from scoped immutable source documents."""
import re

# Presence describes configuration, not proof an assistant actually contributed.
INSTRUCTIONS = ('AGENTS.md', 'CLAUDE.md', 'CODEX.md', '.github/copilot-instructions.md',
                '.codex/config.toml', '.claude/settings.json', '.cursorrules', '.aider.conf.yml')
TOOL = re.compile(r'\b(Claude(?: Code)?|ChatGPT|(?:OpenAI )?Codex|(?:GitHub )?Copilot|Gemini|Cursor|Aider)\b', re.I)
USE = re.compile(r'\b(?:written|developed|coded|generated|built|ported|created|assisted|implemented)\b[^.\n]{0,90}\b(?:with|using|by|via)\b|\b(?:I|we)\s+(?:use|used)\b', re.I)
GENERIC_USE = re.compile(r'\bAI[- ](?:assisted (?:coding|development)|generated (?:code|assets|artwork))\b', re.I)
UNASSERTED = re.compile(r"\b(?:not|never|without|no|goal|aim|plan|planned|planning|hope|might|could|can)\b", re.I)
TOOLS = {'claude code': 'Claude', 'openai codex': 'OpenAI Codex', 'codex': 'OpenAI Codex',
         'copilot': 'GitHub Copilot', 'github copilot': 'GitHub Copilot', 'chatgpt': 'ChatGPT',
         'claude': 'Claude', 'gemini': 'Gemini', 'cursor': 'Cursor', 'aider': 'Aider'}
CPU = {v.casefold(): v for v in ('6502', '6510', '65C02', '65816', 'Z80', '68000', '68010', '68020',
                               '68030', '68040', '68060', '8086', '80286', '80386', 'ARM', 'x86', 'x86-64')}
PLATFORMS = {v.casefold(): v for v in ('Amiga', 'Amiga OCS', 'Amiga ECS', 'Amiga AGA', 'Amiga CD32',
                                     'Atari ST', 'Atari STE', 'Commodore 64', 'ZX Spectrum', 'Amstrad CPC',
                                     'Game Boy', 'DOS', 'Windows', 'Linux', 'macOS')}
PLATFORMS.update({'c64': 'Commodore 64', 'sinclair zx spectrum': 'ZX Spectrum'})
DECLARATION = re.compile(r'^\s*(?:[-*]\s*)?(source|original|target|result)\s+(CPU|platform)\s*:\s*([^.;\n]+?)\s*$', re.I)


def instruction_paths(base):
    """Only the tracked subtree and inherited instructions; never sibling/vendor trees."""
    parts = base.split('/') if base else []
    if len(parts) > 32 or any(p in ('', '.', '..') for p in parts) or '\\' in base:
        raise ValueError('Unsafe or excessive project path for scoped metadata')
    local = [f'{base}/{name}' if base else name for name in INSTRUCTIONS]
    inherited = [('/'.join(parts[:n]) + '/' if n else '') + name
                 for n in range(len(parts)) for name in ('AGENTS.md', 'CLAUDE.md')]
    return list(dict.fromkeys(local + inherited))


def scan(text, repo, commit, path, evidence, *, context_only=False):
    fields = {key: [] for key in ('ai_use', 'ai_config', 'source_cpu', 'target_cpu', 'source_platforms', 'target_platforms')}
    if any(path == name or path.endswith('/' + name) for name in INSTRUCTIONS):
        excerpt = f'{path} present; configuration/instructions only, actual AI use is unconfirmed'
        fields['ai_config'].append({'value': path, 'strength': 'supporting', 'source': path,
                                   'url': evidence.blob(repo, commit, path), 'excerpt': excerpt,
                                   'collector': evidence.COLLECTOR, 'checked_at': evidence.TODAY})
    if context_only:
        return fields
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith(('```', '~~~')):
            fenced = not fenced
            continue
        if fenced or line.lstrip().startswith('>') or not line or len(line) > 1800:
            continue
        # Do not interpret a tool name, a question, a plan or a negation as use.
        tool = TOOL.search(line)
        generic = GENERIC_USE.search(line)
        if not UNASSERTED.search(line) and '?' not in line and (generic or (tool and USE.search(line))):
            match = generic or tool
            value = TOOLS[tool.group(1).casefold()] if tool else 'Unspecified AI'
            fields['ai_use'].append(evidence.ev(value, repo, commit, path, line, match))
        # Deliberately narrow: an explicit labelled declaration, one known value.
        # Never infer runtime minima from compiler flags, prose or CI hosts.
        declaration = DECLARATION.fullmatch(re.sub(r'[*`]', '', line))
        if declaration:
            side, kind, value = declaration.groups()
            side = 'source' if side.lower() in ('source', 'original') else 'target'
            key = side + ('_cpu' if kind.lower() == 'cpu' else '_platforms')
            value = (CPU if kind.lower() == 'cpu' else PLATFORMS).get(value.strip().casefold())
            if value:
                fields[key].append(evidence.ev(value, repo, commit, path, line, declaration))
    return fields


def apply(record, auto):
    """Promote unknown explicit facts; authored values and descriptions stay intact."""
    applied = {}
    for key in ('source_cpu', 'target_cpu', 'source_platforms', 'target_platforms'):
        values = {e['value'] for e in auto.get(key, []) if e.get('strength') == 'strong'}
        if not record.get(key) and len(values) == 1:
            record[key] = [next(iter(values))]
            applied[key] = record[key][:]
            record.setdefault('evidence', {}).setdefault('routine', {})[key] = auto[key][:]
    hits = auto.get('ai_use') or []
    if hits:
        ai = record.setdefault('ai', {'usage': None, 'tools': []})
        # A curated No stays visible alongside contrary evidence for review.
        if ai.get('usage') is None:
            ai['usage'] = True
            applied['ai.usage'] = True
        if ai.get('usage') is True:
            tools = set(ai.get('tools') or [])
            tools.update(e['value'] for e in hits if e['value'] != 'Unspecified AI')
            if tools != set(ai.get('tools') or []):
                ai['tools'] = sorted(tools)
        observations = list(ai.get('evidence') or [])
        for hit in hits:
            marker = f"Documented AI use in {hit['source']}: {hit['excerpt']}"
            if not any(str(item).startswith(marker) for item in observations):
                observations.append(marker + ' (' + hit['url'] + ')')
        ai['evidence'] = observations
        # Keep the first immutable disclosure even if a later document removes it.
    return applied
