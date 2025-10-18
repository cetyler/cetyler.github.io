+++
title = 'Use Grep to Find Content and Move'
date = 2025-10-18T15:59:38-05:00
draft = false
tags = ['grep','xargs','stackoverflow']
summary = 'You can grep and move those files at the same time.'
comments = true
+++

From [Stack Overflow](https://stackoverflow.com/questions/91899/use-grep-to-find-content-in-files-and-move-them-if-they-match)

If you want to find and move files that do not match your pattern (move files that don't contain `'Subject \[SPAM\]'` in this example) use:

```bash
grep -L -Z -r 'Subject: \[SPAM\]' . | xargs -0 -I{} mv {} DIR
```

The -Z means output with zeros (\0) after the filenames (so spaces are not used as delimeters).

```bash
xargs -0
```

means interpret \0 to be delimiters.

The -L means find files that do not match the pattern. Replace `-L` with `-l` if you want to move files that match your pattern.

Then

```bash
-I{} mv {} DIR
```

means replace `{}` with the filenames, so you get `mv filenames DIR`.
