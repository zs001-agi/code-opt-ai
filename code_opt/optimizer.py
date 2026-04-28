"""Code optimizer - Analyzes and suggests improvements for Python code"""
import ast
import os
import re
from typing import Dict, Any, List, Optional
from pathlib import Path

from code_opt.analyzer import CodeAnalyzer, FunctionInfo, ClassInfo


class CodeOptimizer:
    """AI-powered code optimizer using static analysis."""

    def __init__(self):
        self.analyzer = CodeAnalyzer()

    def analyze(self, filepath: str) -> dict:
        """Analyze code file and return quality report."""
        filepath = str(filepath)
        report = self.analyzer.analyze_file(filepath)
        report["quality_score"] = self._calculate_quality_score(report)
        report["issues"] = self._find_issues(report)
        return report

    def analyze_source(self, source: str, filename: str = "<string>") -> dict:
        """Analyze source code string and return quality report."""
        report = self.analyzer.analyze_source(source)
        report["filename"] = filename
        report["quality_score"] = self._calculate_quality_score(report)
        report["issues"] = self._find_issues(report)
        return report

    def suggest_optimizations(self, filepath: str) -> list:
        """Get optimization suggestions for a file."""
        report = self.analyze(filepath)
        suggestions = []

        for issue in report.get("issues", []):
            suggestions.append({
                "type": issue["type"],
                "location": issue["location"],
                "severity": issue["severity"],
                "current": issue.get("current", ""),
                "suggestion": self._get_suggestion_text(issue),
                "message": issue.get("message", ""),
            })

        return suggestions

    def optimize_file(self, filepath: str, output_path: str = None) -> dict:
        """Analyze and generate optimized version of a file."""
        filepath = str(filepath)
        with open(filepath, encoding="utf-8", errors="ignore") as f:
            source = f.read()

        original_report = self.analyze(filepath)
        optimized_source = self._apply_optimizations(source, original_report.get("issues", []))

        if output_path:
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(optimized_source)

        # Re-analyze optimized version
        if output_path:
            optimized_report = self.analyze(output_path)
        else:
            optimized_report = self.analyze_source(optimized_source, filepath)

        return {
            "file": filepath,
            "original_score": original_report.get("quality_score", 0),
            "optimized_score": optimized_report.get("quality_score", 0),
            "issues_found": original_report.get("issues", []),
            "optimizations_applied": self._get_optimizations_applied(source, optimized_source),
            "original_length": len(source),
            "optimized_length": len(optimized_source),
        }

def _calculate_complexity_penalty(self, functions: list) -> float:
    """Calculate complexity penalty based on function complexity."""
    penalty = 0.0
    for func in functions:
        complexity = func.get("complexity", 0)
        if complexity > 10:
            penalty += 5
        if complexity > 20:
            penalty += 5
    return penalty

def _calculate_docstring_penalty(self, functions: list) -> float:
    """Calculate docstring penalty based on function documentation."""
    penalty = 0.0
    for func in functions:
        if not func.get("has_docstring", False):
            penalty += 3
    return penalty

def _calculate_quality_score(self, report: dict) -> float:
    """Calculate a quality score (0-100) from analysis report."""
    score = 100.0
    
    functions = report.get("functions", [])
    
    complexity_penalty = self._calculate_complexity_penalty(functions)
    docstring_penalty = self._calculate_docstring_penalty(functions)
    
    score -= complexity_penalty
    score -= docstring_penalty

    return score


def _calculate_complexity_penalty(self, functions: list) -> float:
    """Calculate penalty based on function complexity."""
    # Placeholder for complexity calculation logic
    return 0.0


def _calculate_docstring_penalty(self, functions: list) -> float:
    """Calculate penalty based on presence of docstrings."""
    # Placeholder for docstring calculation logic
    return 0.0


def check_directory(directory: str) -> dict:
    """Batch check all Python files in a directory."""
    directory = str(directory)
    optimizer = CodeOptimizer()
    results = {}

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith(('.', '__pycache__', 'venv', '.venv', 'env', 'node_modules'))]
        for f in sorted(files):
            if f.endswith('.py'):
                filepath = os.path.join(root, f)
                results[filepath] = optimizer.analyze(filepath)

    return results

