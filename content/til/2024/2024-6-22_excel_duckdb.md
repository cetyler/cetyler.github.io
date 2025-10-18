+++
title = 'Fastest Way to Read Excel in Python'
date = 2024-06-22T15:20:48-05:00
draft = false
tags = ['python','duckdb','excel','Haki Benita']
summary = 'Hint, use DuckDB.'
comments = true
+++

From https://hakibenita.com/fast-excel-python#results-summary

TLDR use DuckDB.
Not necessarily the fastest but faster than Pandas.
Also LibreOffice can be useful as it is faster than Pandas as well and that
includes converting to CSV prior to loading into Python.

Using duckdb will retain the data type from Excel and be up to 5x faster than
Pandas.

## Reading Excel using DuckDB

```python
import duckdb

def iter_excel_duckdb(file: IO[bytes]) -> Iterator[dict[str,object]]:
    duckdb.install_extension('spatial')
    duckdb.load_extension('spatial')
    rows = duckdb.sql(f"""
        select * from st_read(
            '{file.name}',
            open_options=['HEADERS=FORCE', 'FIELD_TYPES=AUTO'])
    """)
    while row := rows.fetchone():
        yield dict(zip(rows.columns, row))
```

This will retain the data types.
