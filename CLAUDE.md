# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal articles site - a clean, minimalist article publishing platform built with vanilla JavaScript and served via GitHub Pages. It functions as a single-page application that dynamically loads Markdown articles with client-side rendering.

## Development Commands

### Local Development
```bash
# Run local server (Python 3)
python3 -m http.server 8000

# Visit http://localhost:8000
```

### Deployment
- **Automatic**: Push to main branch triggers GitHub Pages deployment
- **Site URL**: https://wryan14.github.io/

## Architecture

### Core System
The site operates as a client-side rendered single-page application with three main components:

1. **index.html** - Single-page application shell with all JavaScript inline. Contains:
   - Article listing/search/filtering logic
   - Markdown rendering via Marked.js (CDN-loaded)
   - Theme management (light/dark mode)
   - URL routing for direct article links

2. **articles.json** - Central configuration file that defines all articles:
   ```json
   {
     "title": "Article Title",
     "date": "YYYY-MM-DD",
     "file": "filename.md",
     "excerpt": "Brief description",
     "tags": ["tag1", "tag2"]
   }
   ```

3. **Markdown Files** - Individual article content files in repository root

### Article Flow
1. User visits site → Load articles.json
2. Parse metadata → Display article cards
3. User clicks article → Fetch .md file
4. Render with Marked.js → Display in article view
5. URL updates to #article/[slug] for direct linking

### Key Features Implementation
- **Search**: Client-side filtering of title, excerpt, content, and tags
- **Tag Filtering**: Dynamic tag extraction and filtering system
- **Reading Progress**: Scroll-based progress bar for articles
- **Dark Mode**: localStorage-persisted theme preference
- **Reading Time**: Automatic calculation based on word count (200 WPM)

## Adding New Articles

1. Create `.md` file in repository root following naming convention:
   - Use kebab-case: `article-name.md`
   - Avoid underscores

2. Add entry to `articles.json`:
   - Maintain chronological order (newest first)
   - Include all required fields
   - Follow existing tag conventions (lowercase, space-separated)

3. Commit and push to main branch for automatic deployment

## Style Guidelines

### Article Naming (from style/article_guide.md)
- **Files**: kebab-case, e.g., `grace-works-synthesis.md`
- **Titles**: Title Case with descriptive subtitles
- **Dates**: YYYY-MM-DD format
- **Tags**: lowercase, space-separated, 3-7 per article
- **Excerpts**: 1-2 sentences, 150-250 characters, present tense

### Writing Style (from style/style_guide.md)
- Minimize cognitive load while maintaining natural flow
- Active voice, concrete specifics
- Get to the point without being robotic
- Never fabricate details

## File Structure
```
/
├── index.html           # Single-page application
├── articles.json        # Article metadata configuration
├── favicon.ico         # Site favicon
├── *.md                # Article content files
├── style/              # Style documentation
│   ├── article_guide.md  # Article formatting rules
│   └── style_guide.md    # Writing style guidelines
└── archived/           # Archived articles directory
```

## Important Notes

- **No Build Process**: This is a static site with no build tools
- **Client-Side Only**: All rendering happens in the browser
- **CDN Dependencies**: Marked.js loaded from CDN for Markdown parsing
- **GitHub Pages**: Automatic deployment from main branch
- **SEO Limitation**: Client-side rendering means limited SEO (acceptable for personal site)
- **Archive System**: Moving articles to `/archived/` removes them from main listing while preserving content