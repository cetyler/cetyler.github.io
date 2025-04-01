+++
title = 'Stub Code'
date = 2025-03-31T20:41:19-05:00
draft = false
tags = ['stub','beyond the basic stuff with python','python','Al Sweigart']
summary = 'A better way to have a new function that is not ready.'
comments = true
+++

*Stubs* are exception to these code smell rules.
These are placeholders for future code, such as functions or classes that have
yet to be implemented.

Instead of using a `pass` statement such as:

```python
>>> def exampleFunction():
...     pass
...
```

Which when run will do nothing, instead use `raise NotImplementedError`
statement.

```python
>>> def exampleFunction():
...     raise NotImplementedError
...
>>> exampleFunction()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in exampleFunction
  NotImplementedError
```

This will warn you whenever your program calls a stub function or method
accident.
