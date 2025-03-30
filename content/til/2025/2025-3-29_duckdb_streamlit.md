+++
title = 'Using DuckDB in Streamlit'
date = 2025-03-29T20:37:32-05:00
draft = false
tags = ['Petrica Leuca','duckdb','streamlit']
summary = 'There were a handful of useful things from this article.'
comments = true
+++

[Petrica's article](https://duckdb.org/2025/03/28/using-duckdb-in-streamlit.html)
covering a few things I didn't know you can do with either DuckDB and StreamLit.

## In-Memory Connection
Connecting to an in-memory database involves loading the data into memory,
whenever a DuckDB connection is established.
Depending on the resources of the application server and the amount of data,
creating a new in-memory DuckDB connection and loading the required data on
every request will slow down the application. 
In Streamlit this behavior is addressed by 
[caching the resource](https://docs.streamlit.io/develop/concepts/architecture/caching#stcache_resource),
which can be done as:

* caching the DuckDB connection as a global shared connection in the application;
* caching the DuckDB connection for the user session.

```python
@st.cache_resource(ttl=datetime.timedelta(hours=1), max_entries=2)
def get_duckdb_memory(session_id):
    """
    Set a caching resource which will be refreshed
     - either at each hour
     - either at each third call
     - either when the connection is established for a new session_id
    """

    duckdb_conn = duckdb.connect()
    prepare_duckdb(duckdb_conn=duckdb_conn)

    return duckdb_conn  
```

I didn't realize that you could cache for a given time and also I didn't know
that you could cache per user session.
