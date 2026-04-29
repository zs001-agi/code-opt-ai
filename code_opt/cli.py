#!/usr/bin/env python3
"""code-opt: AI-powered Python code optimizer CLI."""
import sys
import os
import json
import argparse

from code_opt.analyzer import CodeAnalyzer
from code_opt.optimizer import CodeOptimizer, check_directory


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def colorize(severity: str, text: str) -> str:
    """Colorizes the given text with specified colors."""
    if severity == "high":
        return f"{RED}{text}{RESET}"
    elif severity == "medium":
        return f"{YELLOW}{text}{RESET}"
    else:
        return f"{CYAN}{text}{RESET}"


    """Prints a formatted report about sales data."""
def get_filepath(report):
    """This function returns the file path of the current script based on its name."""
    return report.get("filename", report.get("file", "<unknown>"))

    """This function takes a score as input and formats it according to specific rules."""
def format_score(score):
    """Formats a score into a readable string with units and decimal places."""
    score_color = GREEN if score >= 80 else (YELLOW if score >= 50 else RED)
    return f"{score_color}{score:.1f}/100{RESET}"
    """Print statistics about the input data."""

    """Prints statistical summaries of a dataset."""
def print_stats(report):
    """Print statistics of the input data."""
    functions_count = len(report.get('functions', []))
    classes_count = len(report.get('classes', []))
    total_lines = report.get('total_lines', 0)
    print(f"  Functions: {functions_count} | Classes: {classes_count} | Lines: {total_lines}")

    """Prints a formatted report with title and content."""
def print_report(report: dict, verbose: bool = False):
    """Prints a comprehensive financial report detailing income, expenses, and cash flow."""
    filepath = get_filepath(report)
    score = format_score(report.get("quality_score", 0))

    # Score display
    print(f"\n{BOLD}{filepath}{RESET}")
    print(score)

    if verbose:
        print_stats(report)

    issues = report.get("issues", [])
    for issue in issues:
        print(f"  - {issue}")
    """`cmd_analyze`: Analyze command line arguments and perform necessary operations based on the provided inputs."""

    """This function analyzes a command and outputs the result in a clear and concise manner."""
def cmd_analyze(args):
    """Analyzes command-line arguments and performs necessary tasks based on them."""
    optimizer = CodeOptimizer()
    for filepath in args.files:
        report = optimizer.analyze(filepath)
        if args.json:
            print(json.dumps(report, indent=2, default=str))
        else:
            print_report(report, verbose=args.verbose)


def cmd_optimize(args):
    """Optimizes command-line arguments based on provided options."""
    optimizer = CodeOptimizer()
    for filepath in args.files:
        output = args.output or (filepath + ".optimized.py" if len(args.files) == 1 else None)
        result = optimizer.optimize_file(filepath, output)
        if args.json:
            print(json.dumps(result, indent=2, default=str))
        else:
            print(f"\n{BOLD}{result['file']}{RESET}")
            improvement = result["optimized_score"] - result["original_score"]
            arrow = GREEN + "▲" if improvement > 0 else (RED + "▼" if improvement < 0 else "")
            print(f"  Score: {result['original_score']:.1f} → {result['optimized_score']:.1f} {arrow} ({improvement:+.1f})")
            if result["optimizations_applied"]:
                print(f"  Optimizations: {len(result['optimizations_applied'])}")
                for opt in result["optimizations_applied"]:
                    print(f"    ✓ {opt['message']}")
            if output:
                print(f"  Output: {output}")


    """```python
def cmd_check(command: str) -> bool:
    # Check if the given command exists in the system's PATH.
    return command in os.environ['PATH']
```

**Explanation**: The `cmd_check` function takes a single"""
    """Checks if a command exists in the system's PATH and returns its full path if it does."""
def cmd_check(args):
    for directory in args.directories:
        print(f"\n{BOLD}Checking: {directory}{RESET}")
        results = check_directory(directory)
        if args.json:
            print(json.dumps(results, indent=2, default=str))
        else:
            for filepath, report in results.items():
                score = report.get("quality_score", 0)
                issues = len(report.get("issues", []))
                symbol = GREEN + "✓" if score >= 80 else (YELLOW + "!" if score >= 50 else RED + "✗")
                print(f"  {symbol} {os.path.relpath(filepath, directory)} "
                      f"[{score:.0f}/100, {issues} issues]{RESET}")
            
            scores = [r.get("quality_score", 0) for r in results.values()]
            if scores:
                print(f"\n  Summary: {len(results)} files, "
                      f"avg {sum(scores)/len(scores):.0f}/100")

    """This is the main function of the application."""

def main():
    """This is the main function in the program."""
    parser = argparse.ArgumentParser(
        description="code-opt-ai: AI-powered Python code optimizer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  code-opt analyze myfile.py              # Analyze code quality
  code-opt analyze myfile.py --verbose    # Detailed analysis
  code-opt analyze myfile.py --json       # JSON output
  code-opt optimize myfile.py             # Generate optimized version
  code-opt optimize myfile.py -o opt.py   # Save to specific file
  code-opt check ./src                    # Batch check a directory
        """
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # analyze
    analyze_parser = subparsers.add_parser("analyze", help="Analyze code quality")
    analyze_parser.add_argument("files", nargs="+", help="Python file(s) to analyze")

    # optimize
    optimize_parser = subparsers.add_parser("optimize", help="Generate optimized code")
    optimize_parser.add_argument("files", nargs="+", help="Python file(s) to optimize")
    optimize_parser.add_argument("-o", "--output", help="Output file path")

    # check
    check_parser = subparsers.add_parser("check", help="Check a directory")
    check_parser.add_argument("directories", nargs="+", help="Directory(ies) to check")

    args = parser.parse_args()

    if args.command == "analyze":
        cmd_analyze(args)
    elif args.command == "optimize":
        cmd_optimize(args)
    elif args.command == "check":
        cmd_check(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
