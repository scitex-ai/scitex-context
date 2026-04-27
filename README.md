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


Execution-context detection (script vs Jupyter vs IPython) and stdout/stderr suppression helpers, extracted from the [SciTeX](https://github.com/ywatanabe1989/scitex-python) ecosystem as a standalone, zero-dep package.

## Install

```bash
pip install scitex-context
```

## API

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

## Status

Standalone fork of `scitex.context`. Pure stdlib — zero deps. The umbrella
package's `scitex.context` import path is preserved via a `sys.modules`-alias
bridge.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).
