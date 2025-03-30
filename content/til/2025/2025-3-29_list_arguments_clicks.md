+++
title = 'Passing a List of Arguments with Click'
date = 2025-03-29T21:04:57-05:00
draft = false
tags = ['click','python']
summary = 'This can be useful when an option can take multiples at the same time.'
comments = true
+++

You can use the `multiple` option.

```sql
@click.command()
@click.option('--message', '-m', multiple=True)
def commit(message):
click.echo('\n'.join(message))

$ commit -m foo -m bar
foo
bar
```

More info, see
https://click.palletsprojects.com/en/8.1.x/options/#multiple-options
