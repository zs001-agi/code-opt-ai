"""code-opt-ai: AI-powered Python code optimizer using static analysis."""
from code_opt.analyzer import CodeAnalyzer, FunctionInfo, ClassInfo, ComplexityVisitor
from code_opt.optimizer import CodeOptimizer, check_directory
from code_opt.cli import main

__version__ = "0.1.0"
__all__ = [
    "CodeAnalyzer", "FunctionInfo", "ClassInfo", "ComplexityVisitor",
    "CodeOptimizer", "check_directory",
    "main",
]
