---
name: scitex-context
description: Execution-context detection — `is_notebook()`, `is_ipython()`, `is_script()`, `detect_environment()`. `get_output_directory()` returns the canonical place to write artefacts based on context (notebook directory vs script directory vs cwd). Drop-in replacement for the universal `try: get_ipython() except NameError: ...` dance.
primary_interface: python
interfaces:
  python: 2
  cli: 0
  mcp: 0
  skills: 2
  hook: 0
  http: 0
canonical-location: scitex-context/src/scitex_context/_skills/scitex-context/SKILL.md
tags: [scitex-context, scitex-package]
---

> **Interfaces:** Python ⭐⭐ · CLI — · MCP — · Skills ⭐⭐ · Hook — · HTTP —

# scitex-context

Execution-context detection — `is_notebook()`, `is_ipython()`, `is_script()`, `detect_environment()`. `get_output_directory()` returns the canonical place to write artefacts based on context (notebook directory vs script directory vs cwd). Drop-in replacement for the universal `try: get_ipython() except NameError: ...` dance.

See README.md and the package's public `__init__.py` for the full
function list. This skill leaf exists so agents discover the package
exists and roughly what shape it has — refer to the source for
signatures.
