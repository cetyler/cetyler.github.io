+++
title = 'How to List Active Connections on PostgreSQL'
date = 2025-04-06T11:36:10-05:00
draft = false
tags = ['pg_stat_activity', 'postgresql']
summary = 'How to return the active connections.'
comments = true
+++

From
https://stackoverflow.com/questions/27435839/how-to-list-active-connections-on-postgresql

```sql
SELECT 
    pid
    ,datname
    ,usename
    ,application_name
    ,client_hostname
    ,client_port
    ,backend_start
    ,query_start
    ,query
    ,state
FROM pg_stat_activity
WHERE state = 'active';
```

If you want to know the idle ones, use `idle`.
