+++
title = 'Using Assert Never in Python'
date = 2025-04-01T18:29:06-05:00
draft = false
tags = ['assert_never','error','python']
summary = 'Similar to how to do it in SQL you can do in Python.'
comments = true
+++

This is from [this article](https://hakibenita.com/future-proof-sql).

## Assert Never in Python

This will work in Python 3.11:

```python
from typing import assert_never, Literal

def calculate_commission(
    method: Literal['cash', 'credit_card', 'bank_transfer'],
    amount: int,
) -> float:
    if method == 'cash':
        return 100
    elif method == 'credit_card':
        return 30 + 0.02 * amount
    else:
        assert_never(method)
```

Running this code in [Mypy](http://mypy-lang.org/) will produce the following
error:

```python
error: Argument 1 to "assert_never" has incompatible type "Literal['bank_transfer']";
expected "NoReturn"
```
This will only generate an error during static analysis and won't error during
run-time.
