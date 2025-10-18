+++
title = 'How to Version in pyproject'
date = 2025-10-18T16:35:28-05:00
draft = false
tags = ['python','pyproject']
summary = "This is from the packaging project's documentation."
comments = true
+++

From https://packaging.python.org/en/latest/guides/writing-pyproject-toml/.
The main learning I got was how to do a date version instead of 1.0 type versioning.

Put the version of your project.
```
[project]
version = "2020.0.0"
```

Some more complicated version specifiers like `2020.0.0a1` (for an alpha release) are possible; see the [specification](https://packaging.python.org/en/latest/specifications/version-specifiers/#version-specifiers) for full details.

This field is required, although it is often marked as dynamic using
```
[project]
dynamic = ["version"]
```

This allows use cases such as filling the version from a `__version__` attribute or a Git tag. Consult [Single-sourcing the package version](https://packaging.python.org/en/latest/guides/single-sourcing-package-version/#single-sourcing-the-version) for more details.


