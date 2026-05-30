+++
title = 'uv Python Upgrade'
date = 2026-05-02T15:41:06-05:00
draft = false
tags = ['python','uv','John Hagen','Brian Okken','Python Bytes']
summary = 'If you use uv, an easy way to update Python.'
comments = true
+++

I heard this on
[Python Bytes episode 473](https://pythonbytes.fm/episodes/show/473/a-clean-room-rewrite).
See [docs.astral.sh](https://docs.astral.sh/uv/concepts/python-versions/#upgrading-python-versions).

After running `uv self update`, you can now run `uv python upgrade` to update
all uv-installed Python versions to their latest patch releases.
You can also target a specific version, e.g. `uv python upgrade 3.12`.
Brian said he is considering setting it up as a cron job.
