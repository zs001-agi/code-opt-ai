from setuptools import setup, find_packages

setup(
    name="code-opt-ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "code-opt=code_opt.cli:main",
        ],
    },
    author="Wutong ASI",
    description="AI-powered Python code optimizer using static analysis",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zs001-agi/code-opt-ai",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
    ],
    keywords="code-quality ast static-analysis python optimizer developer-tools",
)
