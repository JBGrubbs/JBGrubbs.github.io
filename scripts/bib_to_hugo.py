"""Convert a cleaned BibTeX file into HugoBlox publication page bundles.

Usage: python3 bib_to_hugo.py publications.bib content/publications/

Each entry becomes content/publications/<citekey>/index.md plus cite.bib.
The site owner (Grubbs, J.) is written as `me` so the theme highlights him
and links his profile. Topic tags are assigned from title/abstract/venue so
publications can be filtered by research area.
"""
import os
import re
import sys

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.latexenc import latex_to_unicode

src, outdir = sys.argv[1], sys.argv[2]

MONTHS = {m: i for i, m in enumerate(
    "jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}

# DOIs highlighted on the home page (carried over from the old site's featured list).
FEATURED = {
    "10.1556/2006.2025.00540",       # Bőthe et al. 2026, global moral incongruence
    "10.1001/jamanetworkopen.2024.5473",  # Binge drinking among sports gamblers
    "10.1007/s40429-025-00675-2",    # Moral incongruence after 10 years
    "10.1037/adb0000876",            # Moral incongruence and addiction (RR)
    "10.1007/s10508-018-1248-x",     # Pornography problems due to MI
    "10.1177/0963721420979594",      # Pornography use and psych science
    "10.1016/j.cpr.2020.101925",     # Sexual addiction 25 years on
    "10.1001/jamapsychiatry.2025.0024",  # Sports gambling and drinking over time
    "10.1001/jamanetworkopen.2022.39670",  # Problem gambling among sports bettors
}

TOPICS = [
    ("Gambling", r"gambl|betting|bettor|wager|casino|lotter|prediction market|sportsbook"),
    ("Compulsive Sexual Behavior", r"pornograph|hypersexual|sexual behavio|csbd|sex addiction|sexual addiction|compulsive sexual"),
    ("Moral Incongruence", r"moral incongruence|moral disapproval|transgression as addiction"),
    ("Religion & Spirituality", r"relig|spiritual|\bgod\b|divine|christian|faith|theis"),
    ("Veterans & Military", r"veteran|military|armed forces|service member"),
    ("Alcohol & Substance Use", r"alcohol|drink|substance use|cannabis|binge"),
    ("Personality & Morality", r"narciss|entitle|grandstand|personality|moral"),
]

PROJECTS = {
    "Gambling": "sports-betting",
    "Moral Incongruence": "moral-incongruence",
    "Compulsive Sexual Behavior": "moral-incongruence",
    "Veterans & Military": "veterans-gambling",
}


def clean(s):
    s = latex_to_unicode(s or "")
    s = s.replace("{", "").replace("}", "").replace("\\&", "&")
    return re.sub(r"\s+", " ", s).strip()


def person(name):
    name = clean(name)
    if "," in name:
        last, first = [p.strip() for p in name.split(",", 1)]
    else:
        parts = name.rsplit(" ", 1)
        first, last = (parts[0], parts[1]) if len(parts) == 2 else ("", name)
    if last.lower() == "grubbs" and first[:1].upper() == "J":
        return "me"
    return f"{first} {last}".strip()


def yq(s):
    """Quote a string for YAML using single quotes."""
    return "'" + s.replace("'", "''") + "'"


def venue(e):
    t = e["ENTRYTYPE"]
    if t == "article":
        v = f"*{clean(e.get('journal'))}"
        vol, num = clean(e.get("volume")), clean(e.get("number"))
        if not re.fullmatch(r"[1-9][0-9]*[A-Za-z]?", vol or ""):
            e.pop("volume", None)
        if not re.fullmatch(r"S?[1-9][0-9]*(-[0-9]+)?", num or ""):
            e.pop("number", None)
        if e.get("volume"):
            v += f", {clean(e['volume'])}*"
            if e.get("number"):
                v += f"({clean(e['number'])})"
        else:
            v += "*"
        return v
    if t == "incollection":
        return f"*{clean(e.get('booktitle'))}*"
    if t == "techreport":
        return clean(e.get("institution"))
    return clean(e.get("publisher") or e.get("howpublished") or "")


def pubtype(e):
    return {"article": "article-journal", "incollection": "chapter",
            "techreport": "report", "misc": "manuscript"}.get(e["ENTRYTYPE"], "article-journal")


with open(src, encoding="utf-8") as f:
    db = bibtexparser.load(f)

os.makedirs(outdir, exist_ok=True)
w = BibTexWriter()
w.indent = "  "
counts = {}
for e in db.entries:
    key = re.sub(r"[^a-z0-9-]", "-", e["ID"].lower().replace("_", "-"))
    title = clean(e["title"])
    authors = [person(a) for a in re.split(r"\s+and\s+", e["author"])]
    year = e.get("year", "1900")
    mon = MONTHS.get(e.get("month", "").strip().lower()[:3], 1)
    date = f"{year}-{mon:02d}-01"
    abstract = clean(e.get("abstract"))
    abstract = re.sub(r"\s*\(PsycInfo Database Record.*?\)\s*$", "", abstract)
    doi = (e.get("doi") or "").strip()
    url = (e.get("url") or "").strip()
    hay = " ".join([title, abstract, clean(e.get("journal"))]).lower()
    tags = [name for name, rx in TOPICS if re.search(rx, hay)]
    if "Moral Incongruence" in tags and "Personality & Morality" in tags:
        tags.remove("Personality & Morality")
    projects = sorted({PROJECTS[t] for t in tags if t in PROJECTS})
    for t in tags:
        counts[t] = counts.get(t, 0) + 1

    lines = ["---", f"title: {yq(title)}", "authors:"]
    lines += [f"  - {yq(a)}" for a in authors]
    lines += [f"date: '{date}'", f"publishDate: '{date}'",
              f"publication_types: ['{pubtype(e)}']",
              f"publication: {yq(venue(e))}"]
    if doi:
        lines += ["hugoblox:", "  ids:", f"    doi: {yq(doi)}"]
    if abstract:
        lines.append(f"abstract: {yq(abstract)}")
    if tags:
        lines.append("tags:")
        lines += [f"  - {yq(t)}" for t in tags]
    lines.append(f"featured: {'true' if doi.lower() in FEATURED else 'false'}")
    if projects:
        lines.append("projects:")
        lines += [f"  - {p}" for p in projects]
    if not doi and url.startswith("http"):
        lines += ["links:", "  - type: source", f"    url: {yq(url)}"]
    lines.append("---")

    d = os.path.join(outdir, key)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    one = BibDatabase()
    one.entries = [{k: v for k, v in e.items() if k != "abstract"}]
    with open(os.path.join(d, "cite.bib"), "w", encoding="utf-8") as f:
        f.write(w.write(one))

print("wrote", len(db.entries), "publications")
print("tag counts:", counts)
print("featured:", sum(1 for e in db.entries if (e.get("doi") or "").lower() in FEATURED))
