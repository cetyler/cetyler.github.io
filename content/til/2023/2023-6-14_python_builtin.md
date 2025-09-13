+++
title = 'Built-in Functions in Python'
date = 2023-06-14T23:27:41-05:00
draft = false
tags = ['python','zip','enumerate','Trey Hunner']
summary = 'A couple of functions that I now know.'
comments = true
+++

[Trey](https://pythonmorsels.com/built-in-functions-in-python) talks about a
number of built-in functions but I only listed a couple that I didn't know.

## enumerate

If you need to count upward, one number at a time while looping over an
iterable at the same time, the `enumerate` function will come in hand.

```python
>>> with open('hello.txt', mode='rt') as my_file:
...     for n, line in enumerate(my_file, start=1):
...         print(f'{n:03}', line)
...
001 This is the first line of the file
002 This is the second line of the file
```

If you are using `range(len(sequence))`, you should use `enumerate` instead.

## zip

The `zip` function is used for looping over multiple iterables at the same
time.

```python
>>> one_iterable = [2, 1, 3, 4, 7, 11]
>>> another_iterable = ['P', 'y', 't', 'h', 'o', 'n']
>>> for n, letter in zip(one_iterable, another_iterable):
...     print(letter, n)
...

P 2
y 1
t 3
h 4
o 7
n 11
```


