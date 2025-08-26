+++
title = 'Remove Characters from a String'
date = 2025-08-26T14:41:40-05:00
draft = false
tags = ['postgresql','replace()']
summary = 'Needed to remove an email from a string of emails.'
comments = true
+++

I needed to remove an email from a string of emails in PostgreSQL.
Below is what I came up with:

```sql
data> begin;
data> update progarm.emails set emails = replace(emails,' Marvin@mars.com;',''), comment = 'Remove Marvin from the group.' where name = 'looney';
data> commit;
```

Using [replace()](https://www.postgresql.org/docs/17/functions-string.html) , I was able to remove *Marvin*.
If I wanted to update his email, then I would have done `'TheMartian@mars.com'` instead of `''`.
