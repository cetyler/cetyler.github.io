+++
title = "VS Code to Copy and Paste to Terminal"
date = 2025-03-10T11:18:37-05:00
draft = false
tags = ['Mehdi','vs code','duckdb','python','postgresql']
summary = 'Very useful tip from Mehdi without leaving your IDE'
comments = true
+++

From [Mehdi's video](https://www.youtube.com/watch?v=vgdXxgbiFqc). While he shows how to do it with VS Code, you can do the same thing with other IDEs.

```
 { 
"key": "shift+alt+k", 
"command": "workbench.action.terminal.runSelectedText" 
},
```

Use this with VS Code to copy and paste the selected text into the terminal. This is good for SQL (ex. duckdb/postgres) though I can see this with other applications like Python's REPL.
