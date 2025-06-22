import pathlib, re, json, csv, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = re.compile(r'\b(TODO|FIXME|PLACEHOLDER)\b|pass\s+#\s*stub')
ignore_dirs = {'docs', '.git', '.github', 'venv', '__pycache__', 'build'}
matches = []
for p in ROOT.rglob('*'):
    if p.is_dir() and p.name in ignore_dirs: continue
    if p.suffix in {'.py', '.sh', '.ipynb', '.md'}:
        for i, line in enumerate(p.read_text(errors='ignore').splitlines(), 1):
            if tokens.search(line):
                matches.append([str(p.relative_to(ROOT)), i, line.strip()])
# write tsv
out_tsv = ROOT/'audit'/'open_placeholders.tsv'
out_tsv.parent.mkdir(exist_ok=True)
with out_tsv.open('w', newline='') as f:
    csv.writer(f, delimiter='\t').writerows(matches)
# update task_list.json
tl = json.loads((ROOT/'task_list.json').read_text())
for file, ln, snippet in matches:
    desc = f"Resolve placeholder: {file}:{ln} – {snippet[:60]}"
    if not any(desc.startswith(t['description'][:40]) for t in tl):
        tl.append({"description": desc, "priority": "low", "owner": "GenghisDarb"})
(ROOT/'task_list.json').write_text(json.dumps(tl, indent=2))
# exit non-zero if code-todo remains
code_todo = [m for m in matches if m[0].endswith(('.py','.sh'))]
sys.exit(1 if code_todo else 0)
