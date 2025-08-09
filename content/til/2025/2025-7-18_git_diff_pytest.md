+++
title = 'git diff with pytest'
date = 2025-07-30T20:04:58-05:00
draft = false
tags = ['pytest','git','Brian Okken','Adam Johnson']
summary = 'An easy way to only run tests that have changed.'
comments = true
+++

I heard this while listening to
[Test and Code](https://testandcode.com/episodes/git-tips-for-testing/transcript).
Brian was talking to Adam Johnson.

```bash
$ pytest $(git diff --name-only *tests*)
```

I can see using this as a good way to only run changed tests.

