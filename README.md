# scitex-context

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Execution-context detection (script vs Jupyter vs IPython) and output suppression helpers.</b></p>

<p align="center">
  <a href="https://scitex-context.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-context</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-context/"><img src="https://img.shields.io/pypi/v/scitex-context.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/scitex-context/"><img src="https://img.shields.io/pypi/pyversions/scitex-context.svg" alt="Python"></a>
  <a href="https://github.com/ywatanabe1989/scitex-context/actions/workflows/test.yml"><img src="https://github.com/ywatanabe1989/scitex-context/actions/workflows/test.yml/badge.svg" alt="Tests"></a>
  <a href="https://github.com/ywatanabe1989/scitex-context/actions/workflows/install-test.yml"><img src="https://github.com/ywatanabe1989/scitex-context/actions/workflows/install-test.yml/badge.svg" alt="Install Test"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-context"><img src="https://codecov.io/gh/ywatanabe1989/scitex-context/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scitex-context.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/scitex-context/badge/?version=latest" alt="Docs"></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/license-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>
<!-- scitex-badges:end -->

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

<details open>
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

`scitex-context` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[context]` to use as
`scitex.context` (Python) or `scitex context ...` (CLI).

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
