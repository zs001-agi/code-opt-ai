"""Code analyzer - AST-based code quality analysis"""
import ast, os, re, json
from typing import Dict, Any, List, Set, Optional, Tuple, Callable
from dataclasses import dataclass, field
from collections import defaultdict, deque
from pathlib import Path

@dataclass
class FunctionInfo:
    """函数信息"""
    name: str
    lineno: int
    end_lineno: int
    n_args: int
    n_returns: int
    n_locals: int
    complexity: int          # 圈复杂度
    has_docstring: bool
    has_type_hints: bool
    is_async: bool
    docstring: str = ""
    args_with_types: int = 0
    nested_depth: int = 0

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "lineno": self.lineno,
            "end_lineno": self.end_lineno,
            "n_args": self.n_args,
            "n_returns": self.n_returns,
            "n_locals": self.n_locals,
            "complexity": self.complexity,
            "has_docstring": self.has_docstring,
            "has_type_hints": self.has_type_hints,
            "is_async": self.is_async,
            "nested_depth": self.nested_depth,
            "docstring": self.docstring[:100] if self.docstring else ""
        }

@dataclass
class ClassInfo:
    """类信息"""
    name: str
    lineno: int
    end_lineno: int
    n_methods: int
    n_base_classes: int
    has_docstring: bool
    docstring: str = ""
    methods: List[FunctionInfo] = field(default_factory=list)
    attributes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "lineno": self.lineno,
            "n_methods": self.n_methods,
            "n_base_classes": self.n_base_classes,
            "has_docstring": self.has_docstring,
            "methods": [m.name for m in self.methods],
            "attributes": self.attributes
        }

class ComplexityVisitor(ast.NodeVisitor):
    """圈复杂度计算"""
    def __init__(self):
        self.complexity = 1
        self.nesting_level = 0
        self._in_function = False
        self._in_async_function = False

    def visit_If(self, node):
        self.complexity += 1
        self.nesting_level = max(self.nesting_level, self._count_ifs(node))
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_With(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.complexity += len(node.values) - 1
        self.generic_visit(node)

    def visit_Compare(self, node):
        self.complexity += len(node.ops) - 1
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def _count_ifs(self, node):
        """递归计算嵌套if"""
        count = 0
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.If, ast.For, ast.While)):
                count += 1 + self._count_ifs(child)
        return count

class CodeAnalyzer:
    """
    基于AST的代码分析器
    提取函数、类、复杂度、代码味道
    """

    def __init__(self):
        self.functions: List[FunctionInfo] = []
        self.classes: List[ClassInfo] = []
        self.imports: List[str] = []
        self.import_froms: List[Tuple[str, str]] = []
        self.top_level_code_lines: int = 0
        self.comments: int = 0
        self.blank_lines: int = 0
        self.total_lines: int = 0
        self.file_path: str = ""
        self.parse_error: Optional[str] = None

    def analyze_file(self, filepath: str) -> Dict[str, Any]:
        """分析文件"""
        self.file_path = filepath
        try:
            with open(filepath, encoding="utf-8", errors="ignore") as f:
                source = f.read()
            return self.analyze_source(source)
        except Exception as e:
            return {"error": str(e), "functions": [], "classes": []}

    def analyze_source(self, source: str) -> Dict[str, Any]:
        """分析源代码"""
        self.functions = []
        self.classes = []
        self.imports = []
        self.import_froms = []

        lines = source.split("\n")
        self.total_lines = len(lines)
        self.blank_lines = sum(1 for l in lines if not l.strip())
        self.comments = sum(1 for l in lines if l.strip().startswith("#"))
        self.top_level_code_lines = self.total_lines - self.blank_lines - self.comments

        try:
            tree = ast.parse(source)
        except SyntaxError as e:
            self.parse_error = str(e)
            return self._build_result()

        # 收集import
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    self.import_froms.append((module, alias.name))

        # 分析顶层
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                self._visit_function(node, False)
            elif isinstance(node, ast.AsyncFunctionDef):
                self._visit_function(node, True)
            elif isinstance(node, ast.ClassDef):
                self._visit_class(node)

        return self._build_result()

def _visit_function(self, node, is_async: bool):
    visitor = ComplexityVisitor()
    self._visit_node(visitor, node, is_async)
    complexity = visitor.complexity

    depth = self._calculate_nesting_depth(node)
    n_returns = self._count_returns(node)
    n_locals = self._count_local_variables(node)

    return complexity, depth, n_returns, n_locals

def _visit_node(self, visitor, node, is_async):
    visitor._in_function = True
    visitor._in_async_function = is_async
    visitor.visit(node)

def _calculate_nesting_depth(self, node):
    depth = 0
    for child in ast.walk(node):
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
            depth = max(depth, self._get_nesting_depth(child))
    return depth

def _count_returns(self, node):
    return sum(1 for _ in ast.walk(node) if isinstance(_, ast.Return))

def _count_local_variables(self, node):
    return len([n for n in ast.walk(node) if isinstance(n, ast.Name)])


# Update the method to use these new methods

    def _visit_class(self, node, depth=0):
        methods = []
        attributes = []

        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                self._visit_function(item, False)
                m_doc = ast.get_docstring(item) or ""
                methods.append(FunctionInfo(
                    name=item.name,
                    lineno=item.lineno,
                    end_lineno=item.end_lineno or item.lineno,
                    n_args=len(item.args.args),
                    n_returns=0,
                    n_locals=0,
                    complexity=1,
                    has_docstring=bool(m_doc),
                    has_type_hints=False,
                    is_async=False,
                    docstring=m_doc,
                    args_with_types=0,
                    nested_depth=depth+1
                ))
            elif isinstance(item, ast.AsyncFunctionDef):
                self._visit_function(item, True)
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        attributes.append(target.id)

        self.classes.append(ClassInfo(
            name=node.name,
            lineno=node.lineno,
            end_lineno=node.end_lineno or node.lineno,
            n_methods=len(methods),
            n_base_classes=len(node.bases),
            has_docstring=bool(ast.get_docstring(node)),
            docstring=ast.get_docstring(node) or "",
            methods=methods,
            attributes=attributes
        ))

    def _get_nesting_depth(self, node) -> int:
        depth = 0
        for child in ast.walk(node):
            if isinstance(child, (ast.For, ast.While, ast.If)):
                depth += 1
        return depth

    def _build_result(self) -> Dict[str, Any]:
        return {
            "filepath": self.file_path,
            "parse_error": self.parse_error,
            "total_lines": self.total_lines,
            "code_lines": self.top_level_code_lines,
            "blank_lines": self.blank_lines,
            "comments": self.comments,
            "n_functions": len(self.functions),
            "n_classes": len(self.classes),
            "n_imports": len(self.imports),
            "n_import_froms": len(self.import_froms),
            "imports": self.imports[:20],
            "import_froms": [(m, n) for m, n in self.import_froms[:20]],
            "functions": [f.to_dict() for f in self.functions],
            "classes": [c.to_dict() for c in self.classes],
        }