---
description: |
  [TOPIC] Python API
  [DETAILS] Public Python API of scitex-context — exported functions, signatures,
  return types, and minimal usage examples per function.
tags: [scitex-context-python-api]
---

# Python API

```python
import scitex_context as ctx
```

## Environment detection

```python
ctx.detect_environment()
# -> "script" | "jupyter" | "ipython" | "interactive" | "unknown"

ctx.is_script()    # -> bool — True when running `python foo.py`
ctx.is_notebook()  # -> bool — True under Jupyter
ctx.is_ipython()   # -> bool — True under IPython (console or notebook)

ctx.get_output_directory(path, env_type=None)
# -> (str, bool) — canonical output dir for the current context
```

## Notebook path helpers

```python
ctx.get_notebook_path()       # -> str | None — full path of current notebook
ctx.get_notebook_name()       # -> str | None — filename only
ctx.get_notebook_directory()  # -> str | None — parent directory
ctx.get_notebook_info_simple()
# -> tuple[str | None, str | None] — (name, dir) fallback using CWD
```

## Output suppression

```python
with ctx.suppress_output():
    noisy_function()     # stdout/stderr silenced inside this block

with ctx.quiet():        # alias of suppress_output
    chatty_lib_call()    # same behaviour
```
