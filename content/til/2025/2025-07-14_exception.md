+++
title = 'Python Gotcha: Logging an uncaught exception'
date = 2025-07-17T14:41:40-05:00
draft = false
tags = ['python','exceptions','traceback','Andrew Wegner']
summary = 'A much better method than a huge try/except block.'
comments = true
+++

I would be try/except blocks throughout my code but I would have a large
try/except block to catch any uncaught exception.
Andrew's [article](https://andrewwegner.com/python-gotcha-logging-uncaught-exception.html)
did a good job showing me another way.

The solution is sys.excepthook. This is called when any exception is raised and
uncaught, except for SystemExit.
It's pretty easy to utilize as well.
A few small changes to the above code will allow us to log this completely 
unexpected ZeroDivisionError.

```python
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("app.log")
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def handle_uncaught_exception(exc_type, exc_value, exc_traceback):
    logger.critical(
        "uncaught exception, application will terminate.",
        exc_info=(exc_type, exc_value, exc_traceback),
    )
sys.excepthook = handle_uncaught_exception


def divide(a, b):
    return a/b

def main():
    logger.info("Application start")
    a = 10
    b = 0
    logger.info(divide(a,b))
    logger.info("Application end")

if __name__ == "__main__":
    main()
```
The important bit is the new `handle_uncaught_exception` function and the
`sys.excepthook` line (with appropriate import statement).

What I would do with my code, especially the ones where I log using my
[log_to_db library](https://github.com/cetyler/log_to_db), I will save to a
database:
```python
...
def handle_uncaught_exception(exc_type, exc_value, exc_traceback):
    tb = traceback.extract_tb(exc_traceback)
    error_filename, lineno, funcname, code_error = tb1[-1]
    db_logger.critical(
        message="Uncaught exception, will terminate.",
        details=dict(
            error_type=str(exc_type),
            error_value=str(exc_value),
            error_line_number=str(lineno),
            error_filename=str(error_filename),
            error_function=str(funcname),
            code_error=str(code_error),
            )
sys.excepthook = handle_uncaught_exception

...
```

