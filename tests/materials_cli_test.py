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
        command = ['ruby', str(root / 'scripts/add_material.rb'), '--file', str(source / 'assets/CV.pdf'), '--slug', name, '--title', 'Lecture & notes: test', '--kind', 'Lecture notes', '--year', '2026', *extra]
        subprocess.run(command, capture_output=True, text=True, check=True)
        assert (root / '_materials' / f'{name}.md').exists()
        assert (root / 'assets/thumbnails' / f'{name}.jpg').stat().st_size > 0
        assert (root / 'assets/materials' / f'{name}.pdf').exists() == (name == 'local-note')
        duplicate = subprocess.run(command, capture_output=True, text=True)
        assert duplicate.returncode != 0 and 'Already exists' in duplicate.stderr
print('PASS: local/external material authoring, thumbnails, PDF omission, duplicate protection')
