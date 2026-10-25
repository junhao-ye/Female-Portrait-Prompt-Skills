#!/usr/bin/env python3
"""Validate collection packaging and documentation using only the standard library."""

from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {
    'en': 'README.md',
    'zh-CN': 'README.zh-CN.md',
    'zh-TW': 'README.zh-TW.md',
    'ja': 'README.ja.md',
}
SKILLS = ('female-portrait-prompt-generator', 'female-portrait-director')
errors = []
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        errors.append(message)


def text(path):
    try:
        return path.read_text(encoding='utf-8-sig')
    except (OSError, UnicodeError) as exc:
        errors.append(f'{path.relative_to(ROOT)}: {exc}')
        return ''


def without_fences(content):
    lines = []
    marker = None
    for line in content.splitlines():
        fence = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence:
            current = fence.group(1)
            if marker is None:
                marker = current
            elif current[0] == marker[0] and len(current) >= len(marker):
                marker = None
        elif marker is None:
            lines.append(line)
    return '\n'.join(lines), marker


def anchors(content):
    result = set(re.findall(r'<a\s+id=["\']([^"\']+)["\']', content))
    used = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', content, re.M):
        heading = heading.replace('`', '').lower()
        slug = re.sub(r'[^\w\-\s]', '', heading, flags=re.UNICODE).replace(' ', '-')
        duplicate = used.get(slug, 0)
        used[slug] = duplicate + 1
        result.add(f'{slug}-{duplicate}' if duplicate else slug)
    return result


def validate_links(path, content):
    prose, open_fence = without_fences(content)
    check(open_fence is None, f'Unclosed Markdown fence: {path.relative_to(ROOT)}')
    for destination in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', prose):
        destination = destination.strip().strip('<>')
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc:
            continue
        local = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
        try:
            local.relative_to(ROOT)
        except ValueError:
            check(False, f'Link leaves repository: {path.relative_to(ROOT)} -> {destination}')
            continue
        check(local.exists(), f'Missing link: {path.relative_to(ROOT)} -> {destination}')
        if parsed.fragment and local.is_file() and local.suffix == '.md':
            check(unquote(parsed.fragment) in anchors(text(local)),
                  f'Missing anchor: {path.relative_to(ROOT)} -> {destination}')


def main():
    try:
        manifest = json.loads(text(ROOT / 'SOURCE_MANIFEST.json'))
    except json.JSONDecodeError as exc:
        errors.append(f'Invalid source manifest: {exc}')
        return
    expected = manifest.get('files', {})
    check(bool(expected), 'Source manifest is empty')
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'skills').rglob('*') if p.is_file()}
    check(actual == set(expected), 'Skill snapshot file set differs from manifest')
    for relative, digest in expected.items():
        path = ROOT / relative
        check(path.is_file(), f'Missing source: {relative}')
        if path.is_file():
            check(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                  f'Source bytes changed: {relative}')

    for name in SKILLS:
        entry = ROOT / 'skills' / name / 'SKILL.md'
        body = text(entry)
        check(body.startswith('---\n') or body.startswith('---\r\n'), f'Missing frontmatter: {name}')
        check(re.search(r'^name:\s*' + re.escape(name) + r'\s*$', body, re.M), f'Invalid name: {name}')
        check(re.search(r'^description:\s*\S', body, re.M), f'Missing description: {name}')
        validate_links(entry, body)

    base = ROOT / 'skills' / 'female-portrait-director' / 'skill'
    for registry, folder, count in [('style-registry.md', 'routes', 14),
                                     ('overlay-registry.md', 'overlays', 7),
                                     ('tool-registry.md', 'tools', 6)]:
        body = text(base / registry)
        targets = set(re.findall(r'\]\((' + folder + r'/[^)]+\.md)\)', body))
        check(len(targets) == count, f'{registry}: expected {count} modules, got {len(targets)}')
        for target in targets:
            check((base / target).is_file(), f'Missing registered module: {target}')

    for language, readme_name in LANGUAGES.items():
        readme = ROOT / readme_name
        guide = ROOT / 'docs' / f'USAGE.{language}.md'
        for path, min_length in [(readme, 1400), (guide, 6000)]:
            check(path.is_file(), f'Missing localized document: {path.relative_to(ROOT)}')
            body = text(path)
            check(len(body) >= min_length, f'Incomplete localized document: {path.relative_to(ROOT)}')
            check('\ufffd' not in body, f'Unicode replacement character: {path.relative_to(ROOT)}')
            check(not re.search(r'\{(?:nav|guide_nav|install|generator|director|short|optimize|recommend|reverse|reference|direct_image)\}', body),
                  f'Unexpanded build placeholder: {path.relative_to(ROOT)}')
            check('C:\\Users\\' not in body and 'C:/Users/' not in body,
                  f'Private local path in document: {path.relative_to(ROOT)}')
            check('$female-portrait-prompt-generator' in body and '$female-portrait-director' in body,
                  f'Missing invocation example: {path.relative_to(ROOT)}')
            validate_links(path, body)
        guide_body = text(guide)
        check(len(re.findall(r'^## [1-9]\. ', guide_body, re.M)) == 9,
              f'Expected 9 full guide sections: {language}')
        check(len(re.findall(r'^### [A-H]\. ', guide_body, re.M)) == 8,
              f'Expected 8 usage examples: {language}')
        for token in ['identity_reference', 'product_reference', 'style_reference', 'edit_target',
                      '输出模式：标准', '输出模式：简洁', '输出模式：直接生成图片',
                      '输出模式：参考图直接生成', '20–28', '24–28', '22–28']:
            check(token in guide_body, f'Missing required guide detail {token}: {language}')
        for label in ['English', '简体中文', '繁體中文', '日本語']:
            check(label in guide_body, f'Missing language navigation {label}: {language}')

    for name in ['LICENSES.md', 'CONTRIBUTING.md']:
        validate_links(ROOT / name, text(ROOT / name))
    check('Copyright (c) 2026 李岳' in text(ROOT / 'skills/female-portrait-director/LICENSE'),
          'Original Director copyright notice is missing')

    # Report filenames only; never print potential secrets.
    secret_patterns = [r'gh[pousr]_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{40,}',
                       r'sk-proj-[A-Za-z0-9_-]{30,}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.relative_to(ROOT).parts:
            continue
        if path.suffix.lower() in {'.md', '.json', '.yaml', '.yml', '.py', '.txt'}:
            body = text(path)
            check(not any(re.search(pattern, body) for pattern in secret_patterns),
                  f'Potential credential material: {path.relative_to(ROOT)}')

    if not errors:
        print(f'PASS: {checks} checks; {len(expected)} source files unchanged; 4 READMEs and 4 complete usage guides.')
        print('Validated entry points, 14 routes, 7 overlays, 6 task modules, examples, local documentation links, and credential patterns.')
        print('Scope: packaging and documentation only; no image-generation or external-link quality test.')


if __name__ == '__main__':
    main()
    if errors:
        print('\n'.join(f'ERROR: {error}' for error in errors), file=sys.stderr)
        sys.exit(1)
