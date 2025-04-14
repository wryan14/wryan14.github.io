# Pastor Mann's Sermon RAG System: Simple Design & Cost

## What We're Building

A simple, searchable system for Pastor Mann's 499 YouTube sermons that will:

- Transcribe all sermons with AI
- Let people search and ask questions about the content
- Improve YouTube SEO with better titles, descriptions, and tags
- Automatically process new sermon uploads

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
- GPT-3.5 generates an answer with timestamps/links

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
- GPT-3.5 usage: ~$3
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
