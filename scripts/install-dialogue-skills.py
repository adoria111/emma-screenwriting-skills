#!/usr/bin/env python3
"""Install the two dialogue entries, preserving links and backing up changed files."""
import argparse
import hashlib
import os
from pathlib import Path
import shutil
import tempfile
from datetime import datetime, timezone

FILES = (
    'em-dialogue/SKILL.md',
    'em-dialogue/agents/openai.yaml',
    'em-dialogue/references/course-0930.md',
    'em-dialogue/references/dialogue-framework.md',
    'em-dialogue/references/format-and-performance.md',
    'em-dialogue/references/dialogue-principles.md',
    'em-dialogue-efficiency/SKILL.md',
    'em-dialogue-efficiency/agents/openai.yaml',
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix='.dialogue-', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'wb') as out:
            out.write(data)
        os.chmod(tmp, path.stat().st_mode & 0o777 if path.exists() else 0o644)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skills-dir', type=Path)
    parser.add_argument('--check', action='store_true', help='Inspect only; do not write')
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / 'skills'
    codex_root = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))).expanduser()
    dest = (args.skills_dir or codex_root / 'skills').expanduser().resolve()
    changes = []
    destinations = set()
    for rel in FILES:
        src = source / rel
        if src.is_symlink() or not src.is_file() or source.resolve() not in src.resolve().parents:
            raise RuntimeError('Missing or unsupported source: ' + str(src))
        name, tail = rel.split('/', 1)
        # Resolve an existing skill directory link and keep that link in place.
        target = ((dest / name).resolve() / tail).resolve()
        if target in destinations:
            raise RuntimeError('Two source files resolve to the same destination')
        destinations.add(target)
        data = src.read_bytes()
        old = target.read_bytes() if target.exists() else None
        print(('UNCHANGED ' if old == data else 'UPDATE ') + str(target))
        if old != data:
            changes.append((rel, target, data, old))
    if args.check:
        print('CHECK ONLY: {} file(s) would change; write permission was not tested.'.format(len(changes)))
        return
    if not changes:
        print('All managed files already match. Host loading has not been checked.')
        return
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup = dest / '_backups' / ('dialogue-two-step-' + stamp)
    backup.mkdir(parents=True, exist_ok=False)
    # Complete all backups before changing any installed file.
    for rel, target, data, old in changes:
        if old is not None:
            copy = backup / rel
            copy.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, copy)
    written = []
    try:
        for rel, target, data, old in changes:
            current = target.read_bytes() if target.exists() else None
            if current != old:
                raise RuntimeError('Destination changed during installation: ' + str(target))
            atomic_write(target, data)
            written.append((target, old, data))
            if digest(target.read_bytes()) != digest(data):
                raise RuntimeError('Verification failed: ' + str(target))
    except Exception:
        for target, old, data in reversed(written):
            if target.read_bytes() != data:
                print('ROLLBACK SKIPPED: concurrently modified file ' + str(target))
                continue
            if old is None:
                target.unlink()
            else:
                atomic_write(target, old)
        print('Installation failed. Original backups: ' + str(backup))
        raise
    print('Installed and verified {} file(s). Backup: {}'.format(len(changes), backup))
    print('Open a new Codex conversation and verify the two-step skill can be read. Host loading has not been checked.')


if __name__ == '__main__':
    main()
