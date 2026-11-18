# joshuagrubbsphd.com

Personal academic website of Joshua B. Grubbs, PhD (University of New Mexico / CASAA), built with [Hugo](https://gohugo.io/) and the [HugoBlox](https://hugoblox.com/) Academic CV template.

## Where things live

| What | File |
| --- | --- |
| Name, bio, links, education, experience | `data/authors/me.yaml` |
| Headshot | `assets/media/authors/me.jpg` |
| Home page sections (about, research areas, featured papers) | `content/_index.md` |
| Lab members | `data/authors/<name>.yaml` (set `user_groups`) |
| Lab page, funding, "Join the Lab" | `content/lab/index.md` |
| Speaking and consultation page | `content/speaking/index.md` |
| Research projects | `content/projects/<project>/index.md` |
| Navigation menu | `config/_default/menus.yaml` |
| Site name, colors, fonts, SEO | `config/_default/params.yaml` |

## Updating publications

Publications are generated from `publications.bib`.

1. Export your publications from Zotero as BibTeX.
2. Replace `publications.bib` with the export and push to `main`.
3. The **Import Publications From Bibtex** GitHub Action strips private Zotero fields (local file paths, notes), regenerates `content/publications/`, and opens a pull request for you to merge.

To run it locally instead:

```bash
pip install "bibtexparser<2"
python scripts/clean_bib.py publications.bib publications.bib
python scripts/bib_to_hugo.py publications.bib content/publications/
```

Papers are tagged by topic automatically from title and abstract (see `TOPICS` in `scripts/bib_to_hugo.py`). To feature a paper on the home page, add its DOI to `FEATURED` in the same script.

## Previewing locally

Requires Hugo extended 0.159+, Go, Node 22, and pnpm.

```bash
pnpm install
hugo server
```

## Deployment

Pushing to `main` builds the site and deploys it to GitHub Pages (`.github/workflows/deploy.yml`).
