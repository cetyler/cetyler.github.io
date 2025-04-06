+++
title = 'How to use Variables in a psql Script'
date = 2025-04-06T11:19:37-05:00
draft = false
tags = ['postgresql', 'psql', 'variables']
summary = 'How to use variables.'
comments = true
+++

I found this at
[Stack
Overflow](https://stackoverflow.com/questions/18673208/how-to-use-variables-in-a-psql-script#:~:text=The%20COPY%20command%20expect%20a%20literal%20string%20for,concatenate%20the%20strings%20into%20a%20psql%20%27s%20variable.).

This shows that I could use variables to use for the file location.

```sql
postgres=# \set var1 AAAA
postgres=# \set var2 BBBB
postgres=# \echo :var1:var2
AAAABBBB
postgres=# \echo :var1 :var2
AAAA BBBB
postgres-# \echo :var1'\\':var2
AAAA\BBBB

postgres=# \set mypath '/tmp'
postgres=# \set mypathx :mypath/x.csv
postgres=# \echo :mypathx
/tmp/x.csv
postgres=# copy fo from :'mypathx';
COPY 1
postgres=# \set mypathy :mypath/y.csv
postgres=# copy fo from :'mypathy';
COPY 1
```

Another example with Windows using `$$` quoting:

```sql
\set path 'c:\\server\\data\\'
\set paymentMethodsPath :path 'paymentMethods.csv'
\set priceLevelsPath :path 'priceLevels.csv'
COPY paymentMethods (name,regexString) FROM $$:paymentMethodsPath$$ WITH (FORMAT csv, HEADER true);
COPY priceLevels (name) FROM $$:priceLevels$$ WITH (FORMAT csv, HEADER false);
```

or with `'` quotes:

```sql
\set path 'c:\\server\\data\\'
\set paymentMethodsPath 'E''':path'paymentMethods.csv'''
\set priceLevelsPath 'E''':path'priceLevels.csv'''
COPY paymentMethods (name,regexString) FROM :paymentMethodsPath WITH (FORMAT csv, HEADER true);
COPY priceLevels (name) FROM :priceLevels WITH (FORMAT csv, HEADER false);
```
