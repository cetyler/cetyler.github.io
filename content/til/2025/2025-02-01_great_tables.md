+++
title = 'Great Tables and StreamLit'
date = 2025-02-01T16:02:22-06:00
draft = false
tags = ['python','great_tables','streamlit']
summary = 'The Great Tables package is all about making it simple to produce nice-looking display tables.'
comments = true
+++

[Great Tables](https://posit-dev.github.io/great-tables/) is a Python package
that can help display tables in a visually appealing way.
It does appear to work in StreamLit according to this
[post](https://discuss.streamlit.io/t/great-tables-using-streamlit-how-to/68163).
According to edsaac, it can be done by 
[exporting the GT object as html](https://posit-dev.github.io/great-tables/reference/GT.html#great_tables.GT.as_raw_html)
and passing it to [st.html](https://docs.streamlit.io/develop/api-reference/utilities/st.html)
works OK.
Below is the example edsaac provided:

```python
from great_tables import GT, html
from great_tables.data import sza
import polars as pl
import streamlit as st

st.title(
    ":balloon: Displaying a Great Table",
    help="Check `great_tables` [documentation](https://posit-dev.github.io/great-tables/reference/GT.html#great_tables.GT.as_raw_html)",
)

with st.echo(code_location="below"):
    ## Example from https://posit-dev.github.io/great-tables/examples/
    sza_pivot = (
        pl.from_pandas(sza)
        .filter((pl.col("latitude") == "20") & (pl.col("tst") <= "1200"))
        .select(pl.col("*").exclude("latitude"))
        .drop_nulls()
        .pivot(values="sza", index="month", on="tst", sort_columns=True)
    )

    table = (
        GT(sza_pivot, rowname_col="month")
        .data_color(
            domain=[90, 0],
            palette=["rebeccapurple", "white", "orange"],
            na_color="white",
        )
        .tab_header(
            title="Solar Zenith Angles from 05:30 to 12:00",
            subtitle=html("Average monthly values at latitude of 20&deg;N."),
        )
        .sub_missing(missing_text="")
        .as_raw_html()
    )

    st.html(table)
```
