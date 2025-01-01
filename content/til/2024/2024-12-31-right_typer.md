+++
title = 'RightTyper to Generate Types'
date = 2024-12-31T21:37:26-05:00
draft = false
author = 'Christopher Tyler'
tags = ['python','types','til']
summary = 'Get a helper with typing.'
comments = true
+++

I heard about this on
[Python Bytes](https://pythonbytes.fm/episodes/show/415/just-put-the-fries-in-the-bag-bro).
[RightTyper](https://github.com/RightTyper/RightTyper) is a tool that can
generate types for your function arguments and return values.
You can use it with `pytest` according to the documentation:

```bash
python3 -m righttyper -m pytest --continue-on-collection-errors /your/test/dir
```

I can see using this for the projects where I started typing but not completely
and use RightTyper to provide some hints on what I should use to fill in the
types.
