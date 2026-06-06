---
description: |
  [TOPIC] Quick Start
  [DETAILS] Smallest useful example demonstrating the primary use case in
  under 30 seconds.
tags: [scitex-context-quick-start]
---

# Quick Start

```python
import scitex_context as sc

# Detect the runtime environment
env = sc.detect_environment()
print(f"Running in: {env}")

# Check environment type
if sc.is_script():
    print("This is a script")
elif sc.is_notebook():
    print("This is a Jupyter notebook")
elif sc.is_ipython():
    print("This is an IPython console")

# Suppress noisy library output
with sc.suppress_output():
    print("This will not appear in the console")
```
