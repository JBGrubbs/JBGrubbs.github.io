"""Clean a Zotero BibTeX export for public website import.

Drops private/noisy fields (local file paths, library notes, database keyword
dumps), normalizes DOIs, and reports duplicates and missing metadata.
"""
import re
import sys
from collections import Counter

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter

src, dst = sys.argv[1], sys.argv[2]

DROP = {"file", "annote", "keywords", "copyright", "urldate", "issn",
        "language", "shorttitle", "note"}

parser = BibTexParser(common_strings=True)
parser.ignore_nonstandard_types = False
with open(src, encoding="utf-8") as f:
    db = bibtexparser.load(f, parser=parser)

seen_doi = Counter()
seen_title = Counter()
for e in db.entries:
    for k in list(e):
        if k in DROP:
            del e[k]
    if "doi" in e:
        d = e["doi"].strip()
        d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d, flags=re.I)
        e["doi"] = d
        seen_doi[d.lower()] += 1
    t = re.sub(r"[^a-z0-9]", "", e.get("title", "").lower())
    seen_title[t] += 1

print("entries:", len(db.entries))
print("dup DOIs:", [d for d, c in seen_doi.items() if c > 1])
print("dup titles:", [t[:60] for t, c in seen_title.items() if c > 1])
print("no DOI:", sum(1 for e in db.entries if not e.get("doi")))
print("years:", sorted(Counter(e.get("year") for e in db.entries).items()))
nogrubbs = [e["ID"] for e in db.entries if "grubbs" not in e.get("author", "").lower()]
print("no Grubbs in author list:", nogrubbs)

w = BibTexWriter()
w.indent = "  "
with open(dst, "w", encoding="utf-8") as f:
    f.write(w.write(db))
