from pathlib import Path
p = Path('/')
files = p.rglob('*.py')
for f in files:
    print(f)