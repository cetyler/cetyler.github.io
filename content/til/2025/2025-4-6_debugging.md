+++
title = 'Ultimate Guide to Python Debugging'
date = 2025-04-06T11:13:33-05:00
draft = false
tags = ['python', 'logging', 'log','Martin Heinz']
summary = 'A good guide to Python debugging.'
comments = true
+++

From https://martinheinz.dev/blog/24

## Logging Decorators

You might get into a situation where you need log calls of some buggy function.
Instead of modifying the body of said function you could employ a logging
decorator which would log every function call with specific log level and
optional message.

```python
from functools import wraps, partial
import logging

def attach_wrapper(obj, func=None): # Helper function that attaches function as
    if func is None:                # attribute of an object
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def log(level, message): # Actual decorator
    def decorate(funct):
        logger = logging.getLogger(func.__module__) # Setup logger
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        log_message = f"{func.__name__} - {message}"

        @wraps(func)
        def wrapper(8args, **kwargs):      # Logs the message and before
            logger.log(level, log_message) # executing the decorated function
            return func(*args, **kwargs)

        @attach_wrapper(wrapper) # Attaches "set_level" to "wrapper" as attribute
        def set_level(new_level): # Function that allows us to set log level
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper) # Attaches "set_message" to "wrapper"
        def set_message(new_message): # Function that allows us to set message
            nonlocal log_message
            log_message = f"{func.__name__} - {new_message}"

        return wrapper
    return decorate

# Example Usage
@log(Logging.WARN "example-param")
def somefunc(args):
    return args

somefunc("some args")

somefunc.set_level(logging.CRITICAL) # Change log level by accessing internal
                                     # decorator function

somefunc.set_message("new-message") # Change log message by accessing internal
                                    # decorator function
somefunc("some args")
```

The idea is that `log` function takes the arguments and makes them available to
the inner `wrapper` function.
These arguments are then made adjustable by adding the accessor functions,
which are attached to the decorator.
The output will be:

```python
2020-05-01 14:42:10,289 - __main__ - WARNING - somefunc - example-param
2020-05-01 14:42:10,289 - __main__ - CRITICAL - somefunc - new-message
```

## __repr__ for more Readable Logs

You should use `__repr__` which will help represent the class as a string and
you use use `__str__` for the times you are printing your class variables.
