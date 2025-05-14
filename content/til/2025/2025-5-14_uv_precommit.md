+++
title = 'pre-commit: install with uv'
date = 2025-05-14T07:50:59-05:00
draft = false
tags = ['python','pre-commit','uv','Adam Johnson']
summary = 'Conscise explanation of using uv and pre-commit.'
comments = true
+++

Nice short [article](https://adamj.eu/tech/2025/05/07/pre-commit-install-uv/)
from Adam.
A good reminder that using `uv` to install tools is a great way to keep the tool up to
date as opposed to installing the tool in each virtual environment.
Below is an excerpt from Adam's article.

```bash
$ uv tool install pre-commit --with pre-commit-uv
```

The install command also adds [pre-commit-uv](https://pypi.org/project/pre-commit-uv/),
a plugin that patches pre-commit to use uv to install Python-based tools.
This drastically speeds up using Python-based hooks, a common use case. 
(Unfortunately, it seems pre-commit itself won’t be adding uv support.)

With pre-commit installed globally, you can now install its Git hook in relevant repositories per usual:

```bash
$ cd myrepo
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```
