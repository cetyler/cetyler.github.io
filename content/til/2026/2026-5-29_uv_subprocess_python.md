+++
title = 'Using uv and subprocess module'
date = 2026-05-29T20:34:06-05:00
draft = false
tags = ['uv','python','subprocess']
summary = 'Need to be careful when using uv to call a Python program with subprocesses'
comments = true
+++

While replacing a PowerShell script that was calling various programs to a
Python script, I ran into an issue using `uv`.
When using `subprocess` module, if you are trying to run a Python script using
`uv` in the `subprocess.run()`, it needs to match the same version of Python
the Python script.
If there is a different version, it will fail.
However, this doesn't seem to apply if `subprocess.run()` is running something
that was installed using `uv tool install`.
