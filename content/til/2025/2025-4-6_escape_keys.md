+++
title = 'Escape Keys using psycopg2'
date = 2025-04-06T11:29:10-05:00
draft = false
tags = ['python','psycopg2','postgresql']
summary = 'A mistake I seem to make repeatedly.'
comments = true
+++

Found the information at
https://www.psycopg.org/docs/usage.html#query-parameters.

Since `%` is used in both Python and in PostgreSQL I need to use `%%` instead:

```python
>>> cur.execute("SELECT (%s % 2) = 0 AS even", (10,))       # WRONG
>>> cur.execute("SELECT (%s %% 2) = 0 AS even", (10,))      # correct
```

or this:

```python
f""" AND '{findings}' %%> ANY(STRING_TO_ARRAY(
      CONCAT("Finding1","Finding2","Finding3","Finding4","Finding5","Finding6")
      ,' '
      )
     )
"""
```

instead of this:

```python
f""" AND '{findings}' %> ANY(STRING_TO_ARRAY(
      CONCAT("Finding1","Finding2","Finding3","Finding4","Finding5","Finding6")
      ,' '
      )
     )
"""
```
