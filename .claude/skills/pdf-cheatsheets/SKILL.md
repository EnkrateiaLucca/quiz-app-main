---
name: cheatsheet-creator
description: Create PDF cheatsheets from web articles, transcripts, notes, or presentations. Use when the user asks to summarize content into a cheatsheet, quick reference, or one-pager PDF. Triggers on requests like "make a cheatsheet from this article", "create a quick reference PDF", or "summarize this into a one-page PDF".
---

# Cheatsheet Creator

Create concise, well-formatted PDF cheatsheets from source content.

## Workflow

1. **Analyze source** - Identify key concepts, commands, tips, or facts
2. **Structure content** - Group into logical sections (3-5 sections ideal)
3. **Generate PDF** - Use the bundled script with extracted content

## Content Guidelines

Extract only the essential information:
- Key definitions and concepts
- Important commands or syntax
- Critical tips and warnings
- Quick reference tables

Keep sections short. Each bullet should be scannable in seconds.

## Usage

Run the script with a title, sections, and optional filename:

```bash
python scripts/create_cheatsheet.py \
  --title "Python Basics" \
  --sections sections.json \
  --output cheatsheet.pdf
```

The sections.json format:

```json
[
  {
    "heading": "Variables",
    "items": ["x = 5 assigns value", "Use snake_case for names"]
  },
  {
    "heading": "Functions", 
    "items": ["def name(): to define", "return sends value back"]
  }
]
```

## Quick Inline Usage

For simple cheatsheets, pass content directly:

```python
from scripts.create_cheatsheet import create_cheatsheet

sections = [
    {"heading": "Section 1", "items": ["Point A", "Point B"]},
    {"heading": "Section 2", "items": ["Point C", "Point D"]}
]

create_cheatsheet("My Cheatsheet", sections, "output.pdf")
```