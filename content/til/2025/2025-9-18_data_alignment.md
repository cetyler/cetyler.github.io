+++
title = 'Data Alignment to Save Space'
date = 2025-09-18T16:46:50-05:00
draft = false
tags = ['postgresql','database','Sehrope Sarkuni']
summary = 'While it was an excellent talk, this was my biggest takeaway.'
comments = true
+++

I saw [Sehrope's talk](https://www.youtube.com/watch?v=lkWiyEe2RUQ) at PGconf
New York 2021 recently.
His slides are located
[here](https://sehrope.github.io/pgconf-nyc-2021-advanced-schema-design/).

Very good talk that I plan on watching again in a year or so in time since I
believe there are some items that will click with me in the future when I
learn more about PostgreSQL.
The main thing that click with me today was arranging your columns by data
type.
I feel like I should have known this but if the data is stored in 8 byte
increments, PostgreSQL will give for example `bigint` takes up 8 bytes while
`boolean` takes only 2 bytes.
Sehrope describes that if you have `bigint` column, then `boolean` then
`bigint` then `boolean`, the total space would be 32 bytes.
Whereas if the two `bigint` columns are together and then `boolean` then the
total space would be only be 24 bytes.
If you add more boolean columns, it will still be 24 bytes until you fill the
8 bytes.

His example below:

```sql
CREATE TABLE bad_alignment (
	a  boolean,
	b  bigint,
	c  boolean,
	d  bigint,
	e  boolean,
	f  bigint,
	g  boolean,
	h  bigint
);

CREATE TABLE good_alignment (
	b  bigint,
	d  bigint,
	f  bigint,
	h  bigint,
	a  boolean,
	c  boolean,
	e  boolean,
	g  boolean
);

INSERT INTO bad_alignment
SELECT true, 1, true, 2, true, 3, true, 4
  FROM generate_series(1, 1000000) x;
 
INSERT INTO good_alignment
SELECT 1, 2, 3, 4, true, true, true, true
  FROM generate_series(1, 1000000) x;
 
table_name      | table_size 
----------------+------------
bad_alignment   | 89 MB
good_alignment  | 65 MB
```

His suggestion is to go from the largest columns to the smallest.

```sql
 [12345678 12345678 12345678 12345678 12345678 12345678]
    [B        DDDDDDDD B        DDDDDDDD B        DDDDDDDD]
    [DDDDDDDD DDDDDDDD DDDDDDDD BBB-----]

"B" = Boolean        "DDDDDDDD" = Double        "-" = Unused
```
