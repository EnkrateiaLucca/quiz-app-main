# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A single-file quiz application built with vanilla HTML/CSS/JavaScript. No build tools, no dependencies, no package manager - just open `quiz-app.html` in a browser.

## Running the App

```bash
open quiz-app.html
# or on Linux:
xdg-open quiz-app.html
```

## Architecture

**Single-file SPA**: All code lives in `quiz-app.html` - styles in `<style>`, logic in `<script>`, markup in the body. Three main views are toggled via `display: none/block`:
- `#initialPage` - File upload and JSON format example
- `#questionContainer` - Quiz-taking interface
- `#resultContainer` - Score display and export options

**State management**: Simple module-level variables (`questions`, `currentQuestion`, `score`, `results`) - no framework, no state library.

**Question types**: Multiple-choice (click options) and open-ended (textarea with case-insensitive matching against `acceptedAnswers` array).

## Quiz JSON Format

```json
[
  {
    "question": "Question text",
    "type": "multiple-choice",
    "options": ["A", "B", "C", "D"],
    "correctAnswer": 0,
    "explanation": "Optional explanation"
  },
  {
    "question": "Question text",
    "type": "open-ended",
    "acceptedAnswers": ["answer1", "answer2"],
    "explanation": "Optional explanation"
  }
]
```

- `correctAnswer` is a zero-based index into `options`
- Open-ended matching is case-insensitive exact match

## Design System

Uses Automata Learning Lab brand tokens defined as CSS custom properties:
- Primary: `--ink-black`, `--warm-cream`
- Accents: `--coral`, `--golden`, `--sage`, `--sky` (each with `-light` tint variants)
- Typography: IBM Plex Sans (body), JetBrains Mono (buttons, code)
- Brutalist aesthetic: no border-radius, 2px solid borders, offset box-shadows on hover

## Export Formats

- **CSV**: Question, user answer, correct answer, result status
- **Markdown (LLM Export)**: Structured for AI review with summary prompts
- **Anki**: Semicolon-delimited `question; answer` format for flashcard import