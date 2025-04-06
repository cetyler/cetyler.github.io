+++
title = 'Practical Decorators'
date = 2025-04-06T10:36:56-05:00
draft = false
tags = ['python', 'decorators', 'training', 'Reuven Lerner', 'pycon']
summary = "Reuven's talk from PyCon 2019."
comments = true
+++

From [Reuven Lerner at PyCon 2019](https://www.youtube.com/watch?v=MjHpMCIvwsY).

When you see this:

```python
@once_per_minute
def add(a, b):
    return a + b
```

We should think this:

```python
def add(a, b):
    return a + b

add = once_per_minute(add)
```


## Example 1: Timing

How long does it take for a function to run?

```python
def logtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = runc(*args, **kwargs)
        total_time = time.time() - start_time
        with open('timelog.txt', 'a') as outfile:
            outfile.write(f'{time.time{}}\t{func.__name__}\t{total_time}\n')
        return result
    return wrapper
```

To apply the decorator:

```python
@logtime
def slow_add(a, b):
    time.sleep(2)
    return a + b

@logtime
def slow_mul(am b):
    time.sleep(3)
    return a * b
```

## Example 2: Once per Minute

Raise an exception if we try to run a function more than once in 60 seconds.

```python
def once_per_minue(func):
    last_invoked = 0

    def wrapper(*args, **kwargs):
        nonlocal last_invoked
        elapsed_time = time.time() - last_invoked

        if elasped_time < 60:
            raise CalledTooOftenError(f"Only {elapsed_time has passed")

        last_invoked = time.time()

        return func(*args, **kwargs)

    return wrapper
```

A `nonlocal` will make a variable non local and refer to the one in the outer
function.

## Example 3: Once per n

Raise an exception if we try to run a function more than once in n seconds.

When we see this:

```python
@once_per_n(5)
def add(a, b):
    return a + b
```

We should think this:

```python
def add(a, b):
    return a + b

add = once_per_n(5)(add)
```

There will be 4 callables.

```python
def once_per_n(n):

    def middle(func):
        last_invoked = 0

        def wrapper(*args, **kwargs):
            nonlocal last_invoked
            elapsed_time = time.time() - last_invoked

            if elasped_time < 60:
                raise CalledTooOftenError(f"Only {elapsed_time has passed")

            last_invoked = time.time()

            return func(*args, **kwargs)

        return wrapper

    return middle
```

## Example 4: Memoization

Cache the results of function calls, so we don't need to call them again.

```python
def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args not in cache:
            print(f"Caching NEW value for {func.__name__}{args}")
            cache[args] = func(*args, **kwargs)
        else:
            print(f"Using OLD value for {func.__name__}{args}")
        return cache[args]
    return wrapper
```

But this won't work if it is non hash able.
Instead, using pickle it will become hashable.

```python
def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        t = (pickle.dumps(args), pickle.dumps(kwargs))
        if t not in cache:
            print(f"Caching NEW value for {func.__name__}{args}")
            cache[t] = func(*args, **kwargs)
        else:
            print(f"Using OLD value for {func.__name__}{args}")
        return cache[t]
    return wrapper
```

## Conclusions

* Decorators let you DRY (Don't Repeat Yourself) up your callables.
* Understanding how many callables are involved makes it easier to see what
  problems can be solved and how.
* Decorators make it dramatically easier to do many things.
* Of course, much of this depends on the fact that in Python, callables
  (functions and classes) are objects like any other -- and can be passed and
  returned easily.
