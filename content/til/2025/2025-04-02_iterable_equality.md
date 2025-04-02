+++
title = 'Check Iterable Equality the Right Way'
date = 2025-04-02T19:09:30-05:00
draft = false
tags = ['python','iterable','Trey Hunner']
summary = 'From his Python Morsels newsletter.'
comments = true
+++

This is a really useful tip from [Trey](https://treyhunner.com/).
Need to check whether two Python lists have equal items?
Just use the `== `operator!
```python
list1 == list2
```
Using `==` on lists will check the contents of each list to make sure they contain equivalent items.
What if you have two iterables that might not be lists?
You could convert them both to lists:
```python
list(iterable1) == list(iterable2)
```
But if performance is an issue (whether CPU time or memory), you might want to do this instead:
```python
all(
    a == b
    for a, b in zip(iterable1, iterable2, strict=True)
)
```
That `strict=True` argument only works on Python 3.10 and above.
If you leave out `strict=True`, zip will stop comparing once it reaches the end of the shortest iterable
(meaning if one iterable is a prefix of the other, they'll be seen as equal).
For more on this topic, watch
[my new screencast on checking the equality of different iterables](https://t.dripemail2.com/c/eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZXRvdXIiLCJpc3MiOiJtb25vbGl0aCIsInN1YiI6ImRldG91cl9saW5rIiwiaWF0IjoxNzQzNTk3MzI2LCJuYmYiOjE3NDM1OTczMjYsImFjY291bnRfaWQiOiIzOTQ1ODYwIiwiZGVsaXZlcnlfaWQiOiJvYzRiZXRrZGpsaXBxbGliM2o2NyIsInRva2VuIjoib2M0YmV0a2RqbGlwcWxpYjNqNjciLCJzZW5kX2F0IjoxNzQzNTk4MDIwLCJlbWFpbF9pZCI6MTA1NDgyNDgsImVtYWlsYWJsZV90eXBlIjoiQnJvYWRjYXN0IiwiZW1haWxhYmxlX2lkIjo0MjEwMjc2LCJ1cmwiOiJodHRwczovL3B5bS5kZXYvaXRlcmFibGUtZXF1YWxpdHkvP19fcz04Y3N0c2Fldmt2NWc2dnJhcmJkcyZ1dG1fc291cmNlPWRyaXAmdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249d2Vla2x5K2VtYWlsKy0rMjAyNS0wNC0wMiZ1dG1fY29udGVudD1XZWVrbHkrUHl0aG9uK3RpcCUzQStjaGVjaytpdGVyYWJsZStlcXVhbGl0eSt0aGUrcmlnaHQrd2F5In0.JDH8OZ_6AYOzpwRR5JvpV5AXkUnd0cQMUDJx682U9MQ).
