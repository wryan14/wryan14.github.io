# wryan14.github.io

Personal site at https://wryan14.github.io/. It has a few long-form articles written in Markdown. There is no build step. `index.html` loads `articles.json`, then fetches and renders each article in the browser with [marked](https://marked.js.org/).

## Run locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000. You need a local server because opening `index.html` directly from disk blocks the `fetch` calls.

## Add an article

1. Write the article as a Markdown file in the repo root, named in kebab-case (`my-article.md`). Leave out frontmatter and a top-level `# Title`, because the page adds the title and date.
2. Put any images in `images/` and link them with relative paths: `![Alt text](images/photo.jpg)`. An italic line right after an image is styled as its caption.
3. Add an entry to `articles.json`:

   ```json
   {
     "title": "My Article",
     "date": "2026-01-31",
     "file": "my-article.md",
     "excerpt": "One or two sentences shown on the home page."
   }
   ```

4. Push to `main`. GitHub Pages deploys automatically.

The page sorts articles by date, so the order in `articles.json` doesn't matter. An article's URL (`#article/my-article`) comes from its title, so changing a title breaks old links to it.

## Files

```
index.html       Page, styles, and script
articles.json    Article list: title, date, file, excerpt
*.md             Articles
images/          Article images
favicon.ico
.nojekyll        Tells GitHub Pages to serve files as-is
```
