+++
title = 'Include Schema in psycopg2 Connection String'
date = 2025-04-06T10:45:49-05:00
draft = false
tags = ['postgresql', 'psycopg2', 'sqlalchemy']
summary = 'A method to connect to a specific schema.'
comments = true
+++

Info from
https://stackoverflow.com/questions/59298580/how-to-specify-schema-in-psycopg2-connection-method


If you are using the string form you need to URL escape the options argument:

```sql
postgresql://user:password@localhost:5432/database_name?options=-csearch_path%3Ddbo,public
```

This will connect to `localhost` to database `database_name` with `public`
schema.
