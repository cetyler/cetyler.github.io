+++
title = 'Set Statement Timeout'
date = 2023-07-07T23:34:51-05:00
draft = false
tags = ['postgresql','statement_timeout','idle_in_transaction']
summary = 'Again not sure where I saw this but need to use this more often.'
comments = true
+++


You can set a timeout in case you would want to terminate a long running query
so that you don't cause other problems.

```sql
$ alter database mydatabase set statement_timeout = '60s';
```

Another thing you may want to set is `idle_in_transaction` timeout as well
which will cancel long running transaction that are no longer performing work.
