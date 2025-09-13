+++
title = 'Find Error in pg_dump'
date = 2025-11-05T23:52:55-05:00
draft = false
tags = ['pg_dump','postgresql','sed']
summary = 'Find this handy tip on Mastodon.'
comments = true
+++

[RustProof Labs](https://mastodon.social/@rustprooflabs/111233934559645783)
posted this handy tip.

Ran into an error on line 2,494,680 of a large pg_dump file?  No problem, sed
can quickly show the troublesome lines. 🤓 

```bash
$ sed -n '2494670,2494690p' < big_600MB_dump_file.sql
```

