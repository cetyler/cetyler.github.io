+++
title = 'Use pytest-xdist to Speed Up Testing'
date = 2026-07-18T13:44:04-05:00
draft = false
tags = ['python','pytest']
summary = 'I was able to reduce my tests from ~25 minutes to ~5 minutes.'
comments = true
+++

From [Andros Fenollosa's article](https://en.andros.dev/blog/b6bf68de/testing-in-python-with-pytest-from-the-basics-to-advanced-techniques)
you can run tests in parallel across multiple CPU cores.
For example for one of my projects, I did the following:
```bash
> uv add --dev pytest-xdist
> uv run pytest -n 4
```
This will run on 4 cores.
Use `-n auto` to run on all available cores.
I did not do this due to known memory constraints I have with some of my tests.
See [pytest-xdist documentation]([pytest-xdist — pytest-xdist documentation](https://pytest-xdist.readthedocs.io/en/stable/))
for more information.
