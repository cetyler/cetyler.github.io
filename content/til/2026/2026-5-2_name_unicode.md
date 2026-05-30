+++
title = 'Python tip: name your unicode characters'
date = 2026-05-02T16:01:12-05:00
draft = false
tags = ['Trey Hunner','python','unicode']
summary = 'Another helpful tip from Trey.'
comments = true
+++

I got this tip from [Trey Hunner's newsletter](https://treyhunner.com).
I would highly suggest signing up to his newsletter and looking at
[Python Morsels](https://www.pythonmorsels.com).
If you use unicode in your code, create a variable instead of trying to use
numerical codes:

```python
>>> dashes = "-–﹘—"
>>> print(*dashes)
- – ﹘ —
```

Instead of this:

```python
>>> flair = "\u2728"
```

## Explicitly name Unicode characters

That's why I prefer to use `\N{...}` to reference Unicode characters by their name:

```python
>>> flair = "\N{sparkles}"
```

That makes it much easier for me to guess what that character actually represents:

```python
>>> print(flair)
✨
```

It works for all Unicode characters, including multi-word names:

```python
>>> print("\N{waving hand sign}")
👋
```


## How to find a character's name

Don't know the name of a Unicode character? Use `unicodedata.name` to look it up:

```python
>>> import unicodedata
>>> for c in dashes:
...     print(f"{unicodedata.name(c)}: {c}")
...
HYPHEN-MINUS: -
EN DASH: –
SMALL EM DASH: ﹘
EM DASH: —
```

You can also do a visual search on [utf8.xyz](https://t.dripemail2.com/c/eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZXRvdXIiLCJpc3MiOiJtb25vbGl0aCIsInN1YiI6ImRldG91cl9saW5rIiwiaWF0IjoxNzc2MjU2MTU2LCJuYmYiOjE3NzYyNTYxNTYsImFjY291bnRfaWQiOiIzOTQ1ODYwIiwiZGVsaXZlcnlfaWQiOiJpczNxeGkxZndidjVndThzZXEzcyIsInRva2VuIjoiaXMzcXhpMWZ3YnY1Z3U4c2VxM3MiLCJzZW5kX2F0IjoxNzc2MjU3MjIwLCJlbWFpbF9pZCI6MTE2NjQ3NTQsImVtYWlsYWJsZV90eXBlIjoiQnJvYWRjYXN0IiwiZW1haWxhYmxlX2lkIjo0NjgxMDY4LCJ1cmwiOiJodHRwczovL3V0ZjgueHl6P19fcz04Y3N0c2Fldmt2NWc2dnJhcmJkcyZ1dG1fc291cmNlPWRyaXAmdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249d2Vla2x5K2VtYWlsKy0rMjAyNi0wNC0xNSZ1dG1fY29udGVudD1XZWVrbHkrUHl0aG9uK3RpcCUzQStuYW1lK3lvdXIrdW5pY29kZStjaGFyYWN0ZXJzIn0.GWh8YwLAAPFSkab8XMi286VHRWkKgqtmnKzndDOGUPg "https://t.dripemail2.com/c/eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZXRvdXIiLCJpc3MiOiJtb25vbGl0aCIsInN1YiI6ImRldG91cl9saW5rIiwiaWF0IjoxNzc2MjU2MTU2LCJuYmYiOjE3NzYyNTYxNTYsImFjY291bnRfaWQiOiIzOTQ1ODYwIiwiZGVsaXZlcnlfaWQiOiJpczNxeGkxZndidjVndThzZXEzcyIsInRva2VuIjoiaXMzcXhpMWZ3YnY1Z3U4c2VxM3MiLCJzZW5kX2F0IjoxNzc2MjU3MjIwLCJlbWFpbF9pZCI6MTE2NjQ3NTQsImVtYWlsYWJsZV90eXBlIjoiQnJvYWRjYXN0IiwiZW1haWxhYmxlX2lkIjo0NjgxMDY4LCJ1cmwiOiJodHRwczovL3V0ZjgueHl6P19fcz04Y3N0c2Fldmt2NWc2dnJhcmJkcyZ1dG1fc291cmNlPWRyaXAmdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249d2Vla2x5K2VtYWlsKy0rMjAyNi0wNC0xNSZ1dG1fY29udGVudD1XZWVrbHkrUHl0aG9uK3RpcCUzQStuYW1lK3lvdXIrdW5pY29kZStjaGFyYWN0ZXJzIn0.GWh8YwLAAPFSkab8XMi286VHRWkKgqtmnKzndDOGUPg") (which Seth Larson started and I now own).
Both searching by name (e.g. utf8.xyz/sparkles) or by the character itself (e.g. https://utf8.xyz/—) works.

