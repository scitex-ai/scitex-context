# scitex-context

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
