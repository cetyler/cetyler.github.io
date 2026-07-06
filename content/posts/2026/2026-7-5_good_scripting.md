+++
title = 'Scripting Good Practices in Python'
date = 2026-07-05T19:33:10-05:00
draft = false
tags = ['python','uv', 'Bite Code']
summary = 'A good article from Bite Code.'
comments = true
+++

I saw a couple of ideas from
[this Bite Code article](https://www.bitecode.dev/p/scripting-good-practices-in-python)
on how to make your scripts a little nicer.
It is a good article, so I would suggest reading the whole article as I will
only have the items that are new/important to me.

## Dealing with secrets

I am aware of using
[an environment variable](https://www.bitecode.dev/p/environment-variables-for-beginners)
and I typically use a `toml` file or put into a database.
In the article, the suggestion is to use `os.getenv` and if this is not 
provided, prompt for it with getpass.
The added measure is to use the OS's keyring.
The example given below:

```python
# /// script
# dependencies = [
#   "requests",
#   "keyring",
# ]
# ///

import os
import getpass
import keyring

SCRIPT_NAME = "your_script"
USERNAME = "your_username"


def get_api_token():
    # Environment variable takes precedence so that the user can always override it
    # if needed (e.g: for tests)
    token = os.getenv("YOUR_SCRIPT_API_TOKEN")
    if token:
        return token

    # Try the OS keyring, in case the token has been saved in there by a previous run
    token = keyring.get_password(SCRIPT_NAME, USERNAME)
    if token:
        return token

    # Fallback to asking the user
    print('API_TOKEN not found in env vars, please provide it manually.')
    token = getpass.getpass("API token: ")

    # 4. Save it for next time
    # ... put whatever code that checks that the token works to not save a bad one
    # then save it in the keyring
    keyring.set_password(SCRIPT_NAME, USERNAME, token)

    return token


token = get_api_token()
```

If the secret is very big, like an entire file, you can even encrypt it with
[cryptography.fernet](https://cryptography.io/en/latest/fernet/), and just save
the encryption key in the keyring.

## Pipe or to not Pipe

I don't normally think about this but it is useful to think that if the script
will be able to pipe data like a large file.
You should make sure that you don't read `stdin` if it is coming from the user
then do the following:

```python
import sys

def read_piped_stdin():
    # isatty() is True for an interactive terminal => nothing was piped
    # We check for None for windows .pyw files
    if sys.stdin is None or sys.stdin.isatty():
        return None
    return sys.stdin.read()

data = read_piped_stdin()
if not data:
    # read() returns "" if nothing is piped
    print("no input piped")
else:
    print(f"got {len(data)} chars from stdin")
```

This will let the user do:

```
> cat /etc/fstab | python your_script.py
got 640 chars from stdin
```

## Make a Good Exit

I typically add an exit (0 for success) but I tend to forget that error codes
need to be positive and the limit is 255.
I do sometimes add negative values to have as a warning but since I almost 
always log, that practice has gone away.
Also make sure that you capture **all** exceptions.
If there is an unexpected exception, make it as such with the error code and
logging.

## Documentation

It wasn't mentioned in the article but documentation should be first before you
worry about adding anything else form the article.
I have learned the hard way creating a quick and dirty script to solve a problem
and came back to the script months later initially unsure what I was doing.
Adding a simple comment block at the top (after any dependencies):

```python
# /// script
# dependencies = [
#   "requests",
#   "keyring",
# ]
# ///

"""Example Script

OVERVIEW
Brief overview what the script does.

QUICKSTART
Describe how to run the program with examples if needed.

CHANGELOG
- 2026-07-05: Added some documentation.
- 2026-07-04: Initial release.
"""

import os
import getpass
import keyring
```

The format is similar to basic README files.

## Conclusion

[Good article](https://www.bitecode.dev/p/scripting-good-practices-in-python)
which I did learn some new tricks.
Remember not to punish your future self as you will most likely be the person
that will go back in your code the most.
My future self in my sense is almost like a different person in that I barely
remember what I did 6 months ago so I write documentation as if I am writing
for someone else.
