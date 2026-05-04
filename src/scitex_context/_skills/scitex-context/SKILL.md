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

## Sub-skills

### Core (01–09)
- [01_installation.md](01_installation.md) — install + import sanity check
- [02_quick-start.md](02_quick-start.md) — 30-second tour
- [03_python-api.md](03_python-api.md) — Python API surface
