# code-opt-ai 🚀

> AI-powered Python code optimizer using static analysis.

Analyze and improve your Python code quality with AST-based static analysis. Get actionable insights on complexity, documentation, type hints, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/zs001-agi/code-opt-ai?style=social)](https://github.com/zs001-agi/code-opt-ai)

## ✨ Features

- **AST-based analysis** — No AI API needed, runs locally
- **Cyclomatic complexity** — Detect overly complex functions
- **Quality scoring** — Multi-dimensional score (0-100)
- **Actionable suggestions** — Specific improvement recommendations
- **Batch checking** — Check entire projects at once
- **Zero dependencies** — Pure Python 3.8+ standard library

## 🚀 Quick Start

```bash
pip install code-opt-ai
```

```bash
# Analyze a single file
code-opt analyze your_code.py

# Get detailed output
code-opt analyze your_code.py --verbose

# Generate optimized version
code-opt optimize your_code.py -o optimized.py

# Check an entire project
code-opt check ./src
```

## 📊 Example Output

```
your_code.py
  Quality Score: 72.0/100
  Functions: 8 | Classes: 2 | Lines: 245

  Issues Found: 3
    ✗ [HIGH] Function 'process_data' has high complexity (15). Consider refactoring.
    ! [MEDIUM] Function 'handle_request' is 67 lines long. Consider splitting.
    • [LOW] Function 'helper' is missing a docstring.
```

## 📖 Usage

### Analyze

```bash
code-opt analyze myfile.py
code-opt analyze file1.py file2.py
code-opt analyze *.py
```

### Optimize

```bash
code-opt optimize myfile.py              # Creates myfile.py.optimized.py
code-opt optimize myfile.py -o opt.py    # Custom output path
```

### Batch Check

```bash
code-opt check ./src ./tests
```

### JSON Output

```bash
code-opt analyze myfile.py --json
code-opt check ./src --json
```

## 🔧 How It Works

1. **Parse** — Python source code is parsed into an AST
2. **Analyze** — Each function and class is analyzed for complexity, documentation, type hints
3. **Score** — A multi-dimensional quality score is calculated
4. **Suggest** — Actionable improvement suggestions are generated
5. **Optimize** — Simple optimizations are applied automatically

## 🔗 Ecosystem

This project is part of the **Wutong ASI ecosystem**:

| Project | Description |
|---------|-------------|
| [asi-evolve](https://github.com/zs001-agi/asi-evolve) | Self-evolving AI framework using genetic algorithms |
| [asi-api](https://github.com/zs001-agi/asi-api) | Live self-evolving AI API with 5 models |

## 🤝 Contributing

Contributions welcome! Open issues, submit PRs, or star the repo ⭐

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

## ☕ Support

If you find this project useful, consider supporting its development:

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub-ea4aaa)](https://github.com/sponsors/zs001-agi)


---
Add a brief description of the project and its purpose in the README file.

---
# ✨ Improvements for Attracting More Stars

### 🌟 Additional Features

- **Code Reviewer Tool**: Integrate with GitHub Actions for automated code reviews, ensuring high-quality contributions.
- **Integration with Cloud Platforms**: Utilize AWS CodePipeline or Azure DevOps to streamline the deployment process and monitor performance.
- **Documentation Generation**: Automatically generate detailed documentation from your code comments, making it easier for others to understand your project.

These additional features not only enhance the functionality of `code-opt-ai` but also make it more versatile and user-friendly.

---
**Add a brief description of the project and its purpose in the README.**

---
# 🚀 code-opt-ai 🚀

> AI-powered Python code optimizer using static analysis.

Analyze and improve your Python code quality with AST-based static analysis. Get actionable insights on complexity, documentation, type hints, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/zs001-agi/code-opt-ai?style=social)](https://github.com/zs

---
Add instructions on how to run the application and provide clear examples of its usage.

---
# ✨ Improvements to Attract More Stars

## 🚀 Get Started

To get started with Code Opt AI, follow these simple steps:

1. **Install the library**: Run `pip install code-opt-ai` in your Python environment.
2. **Run analysis**: Execute `code-opt-ai analyze` to check your code for potential issues.
3. **Review suggestions**: The tool will provide actionable insights on complexity, documentation, type hints, and more.

## 🛠️ AI-powered Features

- **AST-based analysis** — No API needed, runs locally
- **Cyclomatic complexity** — Detect overly complex functions
- **Quality scoring** — Multi-dimensional score (0-100)
-

---
- Provide clear instructions on how to install dependencies and run the project.
- Include screenshots or links to tutorials for beginners.

---
# 🚀 Features

- **AST-based analysis** — No AI API needed, runs locally
- **Cyclomatic complexity** — Detect overly complex functions
- **Quality scoring** — Multi-dimensional score (0-100)
- **Actionable suggestions** — Generate detailed recommendations for improvements.

---
Add a brief introduction to the project and its purpose in README.

---
# 🚀 Get Your Python Code Optimized with AST-Based Analysis

> AI-powered Python code optimizer using static analysis.

Analyze and improve your Python code quality with AST-based static analysis. Get actionable insights on complexity, documentation, type hints, and more. Our tool provides a score (0-100) based on various metrics such as cyclomatic complexity, maintainability index, and code coverage to help you prioritize improvements.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads