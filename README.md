# scitex-context

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-context.svg)](https://pypi.org/project/scitex-context/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-context.svg)](https://pypi.org/project/scitex-context/)
[![Tests](https://github.com/ywatanabe1989/scitex-context/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-context/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-context/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-context/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-context/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-context)
[![Docs](https://readthedocs.org/projects/scitex-context/badge/?version=latest)](https://scitex-context.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Execution-context detection (script vs Jupyter vs IPython) and output suppression helpers.</b></p>

<p align="center">
  <a href="https://scitex-context.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-context</code>
</p>

---

## Installation

```bash
pip install scitex-context
```

## Quick Start

```python
import scitex_context as ctx

if ctx.is_notebook():
    print("Running inside Jupyter")

with ctx.suppress_output():
    noisy_function()
```

## 1 Interfaces

<details>
<summary><strong>Python API</strong></summary>

<br>

```python
import scitex_context as ctx

# Environment detection
ctx.detect_environment()       # "script" | "notebook" | "ipython"
ctx.is_script()                # True if running under `python foo.py`
ctx.is_notebook()              # True under Jupyter
ctx.is_ipython()               # True under bare IPython
ctx.get_output_directory()     # Conventional output dir for current context

# Notebook helpers (no-op outside a notebook)
ctx.get_notebook_path()
ctx.get_notebook_directory()
ctx.get_notebook_name()
ctx.get_notebook_info_simple()

# Output suppression
with ctx.suppress_output():
    noisy_function()

with ctx.quiet():               # alias
    chatty_lib_call()
```

</details>

## Status

Standalone fork of `scitex.context`. Pure stdlib — zero deps. The umbrella
package's `scitex.context` import path is preserved via a `sys.modules`-alias
bridge.

## Part of SciTeX

`scitex-context` is part of [**SciTeX**](https://scitex.ai).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
