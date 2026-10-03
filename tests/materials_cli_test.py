"""Exercise authoring in an isolated temporary site; never add fixtures to the real gallery."""
from pathlib import Path
import shutil
import subprocess
import tempfile

source = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='materials-cli-') as temp:
    root = Path(temp)
    shutil.copytree(source / 'scripts', root / 'scripts')
    for name, extra in [('local-note', []), ('external-note', ['--pdf-url', 'https://files.example.org/lecture.pdf'])]:
        command = ['ruby', str(root / 'scripts/add_material.rb'), '--file', str(source / 'assets/CV.pdf'), '--slug', name, '--title', 'Lecture & notes: test', '--kind', 'Lecture notes', '--year', '2026', '--date', '2026-08-19', *extra]
        subprocess.run(command, capture_output=True, text=True, check=True)
        assert (root / '_materials' / f'{name}.md').exists()
        assert "event_date: '2026-08-19'" in (root / '_materials' / f'{name}.md').read_text()
        assert (root / 'assets/thumbnails' / f'{name}.jpg').stat().st_size > 0
        assert (root / 'assets/materials' / f'{name}.pdf').exists() == (name == 'local-note')
        duplicate = subprocess.run(command, capture_output=True, text=True)
        assert duplicate.returncode != 0 and 'Already exists' in duplicate.stderr
    invalid = ['ruby', str(root / 'scripts/add_material.rb'), '--file', str(source / 'assets/CV.pdf'), '--slug', 'invalid-date', '--title', 'Invalid date', '--kind', 'Seminar slides', '--year', '2026', '--date', '2025-08-19']
    assert subprocess.run(invalid, capture_output=True).returncode != 0
    assert not (root / '_materials/invalid-date.md').exists()
    assert not (root / 'assets/materials/invalid-date.pdf').exists()
print('PASS: local/external material authoring, thumbnails, PDF omission, duplicate protection')
