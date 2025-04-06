+++
title = 'Find and Replace in Vim'
date = 2025-04-06T11:08:51-05:00
draft = false
tags = ['vim', 'find', 'replace', 'substitute']
summary = 'How to do find and replace in Vim.'
comments = true
+++

From https://linuxize.com/post/vim-find-replace/

## Basic Find and Replace

In Vim you use `:substitue` (`:s`) command.

```
:[range]s/{pattern}/{string}/[flags] [count]
```

If no `[range]` and `[count]` are given, only the pattern found in the current
line is replace.

If you want to replace all occurrences of foo with bar:

```
:%s/foo/bar/g
```

The `%` is for the entire file and `g` would be all occurrences.
The `/` can be replaced with any non-alphanumeric single-byte character as a
delimiter.
This is useful if you are replacing `/`.

## Case Sensitivity

By default the search is case sensitive so include `i` to make it ignore the
case.

```
:s/Foo/bar/gi
```

## Search Range

To search for certain line ranges, include the line numbers:

```
:3,10s/foo/bar/g
```

This will be for lines 3 to 10 (this is inclusive).

To make changes from the current line to the end of the file using `.` and `$`.

```
:.,$/foo/bar/
```

Finally you can use `+` and `-` to denote the number of rows above or below a
certain linIf no `[range]` and `[count]` are given, only the pattern found in
the current line is replace.

If you want to replace all occurrences of foo with bar:

```
:%s/foo/bar/g
```

The `%` is for the entire file and `g` would be all occurrences.
The `/` can be replaced with any non-alphanumeric single-byte character as a
delimiter.
This is useful if you are replacing `/`.

## Case Sensitivity

By default the search is case sensitive so include `i` to make it ignore the
case.

```
:s/Foo/bar/gi
```

## Search Range

To search for certain line ranges, include the line numbers:

```
:3,10s/foo/bar/g
```

This will be for lines 3 to 10 (this is inclusive).

To make changes from the current line to the end of the file using `.` and `$`.

```
:.,$/foo/bar/
```

Finally you can use `+` and `-` to denote the number of rows above or below a
certain line.

```
:.,+4s/foo/bar/g
```

## Substituting Whole Word

To only replace the whole word and not portions, type `\<` to mark the
beginning of a word and `\>` to mark the end of a word.

```
:s/\<foo\>/bar/
```
