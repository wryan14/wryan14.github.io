# CLAUDE.md

Static personal site served by GitHub Pages from `main`. There is no build step, package manager, or test suite. See README.md for the layout and how to add an article.

- Everything (markup, styles, script) lives in `index.html`. Keep it vanilla HTML/CSS/JS, with marked pinned to a specific version on the CDN.
- `articles.json` is the only source of article metadata. Article `.md` files have no frontmatter and no top-level `#` heading.
- URLs are `#article/<slug>`, where the slug comes from the title. Don't rename titles without asking, because that breaks existing links.
- Preview with `python3 -m http.server 8000`.
- Articles are research pieces. Never invent facts, dates, names, or sources. If something isn't in the material provided, ask.
