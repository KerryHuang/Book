"""依 TSV（路徑\tkind\tsource\tauthor）在每篇 md 檔頭加入 front matter；已有 front matter 的略過。
用法：python scripts/apply-frontmatter.py a.tsv [b.tsv ...]
"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
done = skipped = missing = 0
for tsv in sys.argv[1:]:
    for line in open(tsv, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        cols = (line.split("\t") + ["", "", ""])[:4]
        rel, kind, source, author = [c.strip() for c in cols]
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            missing += 1; print("找不到:", rel); continue
        txt = open(p, encoding="utf-8", errors="ignore").read()
        if txt.startswith("---"):
            skipped += 1; continue
        fm = ["---", f"kind: {kind or 'unknown'}"]
        if source: fm.append(f"source: {source}")
        if author: fm.append(f"author: {author}")
        fm.append("---")
        open(p, "w", encoding="utf-8", newline="\n").write("\n".join(fm) + "\n\n" + txt.lstrip("﻿"))
        done += 1
print(f"寫入 {done}、已有略過 {skipped}、找不到 {missing}")
