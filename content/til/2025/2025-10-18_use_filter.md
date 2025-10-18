+++
title = 'Use filter() instead of for loop'
date = 2025-10-18T16:54:59-05:00
draft = false
tags = ['python']
summary = "A helpful tip to use Python's built-ins."
comments = true
+++

From https://dev.to/0x3d_site/python-shortcuts-that-save-you-hours-5dfp.
While the overall tip was to try and use Python's built-ins more, below was
a very useful tip for me.
Instead of this:

```python
filtered = []
for item in my_list:
    if condition(item):
        filtered.append(item)
```

Do this instead:

```
filtered = list(filter(condition, my_list))
```

