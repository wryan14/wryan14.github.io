# Sermon RAG System: Simple Design & Cost

## What We're Building

A simple, searchable system for Pastor Mann's 499 YouTube sermons that will:

- Transcribe all sermons with AI
- Let people search and ask questions about the content
- Improve YouTube SEO with better titles, descriptions, and tags
- Automatically process new sermon uploads

## System Architecture

![Sermon RAG System Architecture](https://mermaid.ink/img/pako:eNqNVMtu2zAQ_BWCJwcwZMdOmrhAeuhRSIE2CBo0EC8HWqRsBNpQJOXWMPTvXVJyHAdtT-JqZ4czs7O73BLFElEiN1eKc0Wp4Mh-kCplFANvsCUl0rJghJY1p6gohfUEvTmCLz8ufl5-j5RqkaB3V4zQaY8Kh3--JNrC_Xxzfd3UcrvjQSk3lzNFPrIEz3g9Y-HVZwgpBzl48M_b8RuExE-FveBxJE4Rl_Mcp33hKMh4Yp_aRbSZo2YOXOW1pMT0xQ2NaQkJSfQ_lCLFFKnltV5YWs3C6g69UGnCiSHkJCx9Oet27AwsB14ZCq9D7ZKp_L80h8VMOI2nfJaswk6FSpxyyK4vchZqw5IFhxDDjM_XkxKzj6ZoRfHkP66xbHFbqOQ-RZ3Vh4tB04c9mxMEGsKoNjWtDNuv7VQ4x7TrTtnkwbhM13Xtk9tnXXG9bnuJIzSqaOHJcIE85hV1vGKpf-iEP0Iui92e8fO_yfI_QSvUxlIWOCJHyMF3LgotGz1AXx9JDj7xrJakk7g7-PCqQU8Whi1BDm6nZBL3aQ6gy04FoNM1nBXVnfOCDEVPD5tQCNsU-_qwuS64dAdbrVCh5fXWI0wK89sEE2eZIyVVuQm3vfM7KPLQJMhx7doSX5Q1ZzZ4oOuMPqTM4Gb2FHlQVhZRKqW7zy_fstfuPLVY8aqh_Jtf02tpLMfxGrfH-Z-Vdoc-fgCVcPa6SrOytgYp6jWNV4lSV2N-xjuKrfUG1YxHZm0tjm1kqxhbpQvF1iYS-2ZtGZtzr7_Wc2zpOJK96fXMcfWP4-of-Gj3iw?type=png)

*System diagram showing the flow from YouTube videos through transcription, storage, and query processing to user interface.*

## Tech Stack

**Core Components:**
- **Audio Download**: yt-dlp (Python library to grab YouTube audio)
- **Transcription**: OpenAI Whisper API
- **Vector Database**: Pinecone (free tier)
- **Question Answering**: OpenAI GPT-4o
- **Frontend**: Jekyll site on GitHub Pages
- **Backend**: Python with FastAPI on a simple host

## How It Works

**Step 1: Getting the Sermons**
- Download audio from YouTube with yt-dlp
- Transcribe with Whisper API ($0.006/minute)
- Split text into chunks and create embeddings

**Step 2: Building the Database**
- Store embeddings in Pinecone (free tier handles our needs)
- Save transcripts in simple storage (S3 or even GitHub)
- Track metadata like dates, titles, URLs

**Step 3: User Interface**
- Simple search box on a Jekyll site (GitHub Pages)
- User asks a question
- System finds relevant sermon sections
- GPT-4o generates an answer with timestamps/links

**Step 4: Automation**
- Script checks for new uploads weekly
- Automatically processes new sermons
- Optionally generates SEO suggestions

## Cost Breakdown

**One-time Costs:**
- Transcribe 499 videos (~45 min each): ~$135
- Generate embeddings: ~$2
- Domain name (optional): $12/year

**Monthly Costs:**
- Transcribe new videos (12/month): ~$3.24
- Server hosting: ~$7 (or less with free tiers)
- GPT-4o usage: ~$10 (Depends on usage)
- Storage: ~$1

**Total Estimates:**
- Initial setup: ~$150
- Monthly ongoing: ~$25
- First year total: ~$450

## Quick Start Approach

1. **Test with a small batch first** (5-10 sermons)
2. **Start simple** - get basic transcription and search working
3. **Build incrementally** - add features as we go
4. **Use free tiers** wherever possible

## Technical Notes

- Whisper API provides the best balance of cost ($0.006/min) and accuracy
- Pinecone's free tier (100k vectors) is plenty for our needs
- GPT-4o offers superior understanding of religious context at $0.01/1K input tokens and $0.03/1K output tokens
- Consider trying local embedding models if you want to cut API costs

This project is meant to be fun and educational while creating something useful. The design prioritizes simplicity and low maintenance over enterprise-grade features.
