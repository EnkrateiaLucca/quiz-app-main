# Quiz App

A single-file quiz application built with vanilla HTML/CSS/JavaScript. No build tools, no dependencies, no package manager - just open `quiz-app.html` in a browser.

## Features

- **Two Question Types**: Multiple-choice (click options) and open-ended (text input with flexible answer matching)
- **JSON-Based Import**: Load quiz questions from simple JSON files
- **Real-Time Feedback**: Visual indicators for correct/incorrect answers with explanations
- **Multiple Export Formats**:
  - CSV for spreadsheet analysis
  - Markdown for LLM review
  - Anki format for flashcard creation
- **Modern Design**: Brutalist aesthetic with Automata Learning Lab brand tokens
- **Zero Dependencies**: Pure vanilla JavaScript - no frameworks, no build process

## Getting Started

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/EnkrateiaLucca/quiz-app-main.git
cd quiz-app-main
```

2. Open the app in your browser:
```bash
# macOS
open quiz-app.html

# Linux
xdg-open quiz-app.html

# Windows
start quiz-app.html
```

3. Click "Choose Quiz File" and select a JSON quiz file (try `example-quiz.json`)
4. Click "Start Quiz" and begin answering questions
5. View results and export in your preferred format

## Quiz JSON Format

Create quiz files using this JSON structure:

```json
[
  {
    "question": "What is the capital of France?",
    "type": "multiple-choice",
    "options": ["London", "Paris", "Berlin", "Madrid"],
    "correctAnswer": 1,
    "explanation": "Paris has been the capital of France since 987 AD."
  },
  {
    "question": "Explain the concept of photosynthesis.",
    "type": "open-ended",
    "acceptedAnswers": [
      "The process by which plants convert sunlight into energy",
      "Plants use sunlight to make food"
    ],
    "explanation": "Photosynthesis uses light energy to convert CO2 and water into glucose."
  }
]
```

### Format Specifications

- **Multiple Choice**:
  - `type`: `"multiple-choice"`
  - `options`: Array of answer choices
  - `correctAnswer`: Zero-based index of the correct option
  - `explanation`: (Optional) Shown after answering

- **Open Ended**:
  - `type`: `"open-ended"`
  - `acceptedAnswers`: Array of acceptable answer strings
  - Matching is case-insensitive and exact
  - `explanation`: (Optional) Shown after answering

## Architecture

### Single-File Design

All code lives in `quiz-app.html`:
- **Styles**: Embedded in `<style>` tag with CSS custom properties for theming
- **Logic**: Pure JavaScript in `<script>` tag
- **Markup**: Three main views toggled via `display: none/block`:
  - `#initialPage`: File upload and format example
  - `#questionContainer`: Quiz interface
  - `#resultContainer`: Score display and export options

### State Management

Simple module-level variables - no framework needed:
- `questions`: Loaded quiz data
- `currentQuestion`: Current question index
- `score`: Running score
- `results`: Array of user answers and correctness

### Design System

Built with Automata Learning Lab brand tokens:

**Colors**:
- Primary: `--ink-black` (#1a1a1a), `--warm-cream` (#f9f7f4)
- Accents: `--coral`, `--golden`, `--sage`, `--sky` (each with `-light` variants)

**Typography**:
- Body: IBM Plex Sans
- Buttons/Code: JetBrains Mono

**Aesthetic**:
- Brutalist design: no border-radius
- 2px solid borders
- Offset box-shadows on hover

## Export Formats

### CSV
Spreadsheet-compatible format with columns:
- Question text
- User's answer
- Correct answer
- Result (Correct/Incorrect)

### Markdown (LLM Export)
Structured for AI review with:
- Summary statistics
- Question-by-question breakdown
- Prompts for improvement suggestions

### Anki
Semicolon-delimited format for flashcard import:
```
question; correct answer
```
Import directly into Anki for spaced repetition learning.

## Examples

The repository includes example quiz files:
- `example-quiz.json`: Sample questions demonstrating both question types
- `test-quiz.json`: Additional test cases

## Browser Compatibility

Requires a modern browser with support for:
- ES6+ JavaScript (arrow functions, const/let, template literals)
- CSS Custom Properties (variables)
- File API for JSON upload

Tested on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Contributing

Contributions are welcome! This project intentionally maintains a zero-dependency approach.

**Guidelines**:
1. Keep everything in the single `quiz-app.html` file
2. Use vanilla JavaScript - no frameworks or libraries
3. Follow the existing design system (see CLAUDE.md for details)
4. Test in multiple browsers before submitting

**Process**:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit with descriptive messages
5. Push and open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Technical Details

For developers working with this codebase, see [CLAUDE.md](CLAUDE.md) for:
- Detailed architecture documentation
- Design system specifications
- Development guidelines
- Code structure overview
