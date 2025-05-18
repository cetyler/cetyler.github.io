+++
title = 'Using Open Libary APIs'
date = 2025-05-18T14:54:30-05:00
draft = false
tags = ['duckdb','openlibrary','scanned_isbn','pandas']
summary = 'Using DuckDB to analyze data from Open Library.'
comments = true
+++

## Overview

I have a [personal project](https://github.com/cetyler/scanned_isbn) that I 
want to use my phone to scan ISBN of my books to catalog my physical books.
This article is not about that project, but how to use
[DuckDB](https://duckdb.org) and using [Open Library](https://openlibrary.org).

## Open Library

Open Library is part of the [Internet Archive](https://archive.org/).
The nice part is that they have some documentation for using their
[APIs](https://openlibrary.org/developers/api) and provide the means to do
[bulk downloads](https://openlibrary.org/developers/dumps).
I decided to download the bulk data since for now I don't want to hammer their
website until I figure out how I want to setup my program and run tests.
Also my thinking is that I can have the existing data and only use their API
when I don't have the data.

### APIs

The APIs I plan to make use would be searching by ISBN and by author.
For example, Rogue protocol from the excellent Murderbot Dairies, have a ISBN
of 9781250191786.
This will return a JSON that will provide information of the book.

```JSON
{
  "number_of_pages": 158,
  "description": {
    "type": "/type/text",
    "value": "\"Sci-Fi's favorite antisocial AI is back on a mission.  The case against the too-big-to-fail GrayChris Corporation is floundering, and more importantly, authorities are beginning to ask more questions about where Dr. Mensah's SecUnit is.  And Murderbot would rather those questions went away.  For good.\""
  },
  "isbn_10": [
    "1250191785"
  ],
  "series": [
    "The Murderbot Diaries"
  ],
  "key": "/books/OL26966631M",
  "authors": [
    {
      "key": "/authors/OL221294A"
    }
  "isbn_13": [
    "9781250191786"
  ],
}
```

This is a partial of what will be returned.
Notice that `authors` have an ID instead of the author's name.
Using `OL221294A` and author API will then provide Martha's information.

```JSON
{
    "name": "Martha Wells",
  "bio": "Martha Wells (born September 1, 1964) is an American writer of speculative fiction. She has published a number of fantasy novels, young adult novels, media tie-ins, short stories, and nonfiction essays on fantasy and science fiction subjects. Her novels have been translated into twelve languages. Wells has won a Nebula Award, two Locus Awards, and two Hugo Awards.",
  "alternate_names": [
    "Wells, Martha",
    "Wells, M.",
    "M. Wells"
  ],
  "links": [
    {
      "title": "Official Website",
      "url": "https://marthawells.com",
      "type": {
        "key": "/type/link"
      }
    }
  ],
}
```

This is a partial of what will be returned.
Now I have Martha's information.
For my purposes, this should be enough to catalog my books.
While I don't have a ton of books, I would prefer to have the data locally to
reduce using their APIs and to make it easier to run a bunch of tests.

### Bulk Download

Now that I have an idea of the data I want, I should be able to download the
following:

```bash
> wget https://openlibrary.org/data/ol_dump_authors_latest.txt.gz
> wget https://openlibrary.org/data/ol_dump_editions_latest.txt.gz
> wget https://openlibrary.org/data/ol_dump_works_latest.txt.gz
```

For example, according
[author's documentation](https://openlibrary.org/type/author)
it should have the following properties:

- **name** of type [/type/string](https://openlibrary.org/type/string)
- **eastern_order** of type [/type/boolean](https://openlibrary.org/type/boolean)
- **personal_name** of type [/type/string](https://openlibrary.org/type/string)
- **enumeration** of type [/type/string](https://openlibrary.org/type/string)
- **title** of type [/type/string](https://openlibrary.org/type/string)
- **alternate_names[]** of type [/type/string](https://openlibrary.org/type/string)
- **uris[]** of type [/type/string](https://openlibrary.org/type/string)
- **bio** of type [/type/text](https://openlibrary.org/type/text)
- **location** of type [/type/string](https://openlibrary.org/type/string)
- **birth_date** of type [/type/string](https://openlibrary.org/type/string)
- **death_date** of type [/type/string](https://openlibrary.org/type/string)
- **date** of type [/type/string](https://openlibrary.org/type/string)
- **wikipedia** of type [/type/string](https://openlibrary.org/type/string)
- **links[]** of type [/type/link](https://openlibrary.org/type/link)

This is similar to using the API.
Keep in mind that total compressed size for all the files will be in the ~13GB
range.
Since I plan on using DuckDB, this shouldn't be a problem.

## DuckDB

While in the documentation from Open Library they mention
[openlibrary-search](https://github.com/LibrariesHacked/openlibrary-search) to
aid with using PostgreSQL and Python, I decided to use DuckDB to help me have a
reason to use and learn DuckDB more.
First step is to get an idea of how the data dump looks.
For now I will continue to focus on authors.

```sql
D describe from read_csv('ol_dump_authors_latest.txt.gz');
┌─────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│ column_name │ column_type │  null   │   key   │ default │  extra  │
│   varchar   │   varchar   │ varchar │ varchar │ varchar │ varchar │
├─────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ column0     │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ column1     │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ column2     │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ column3     │ TIMESTAMP   │ YES     │ NULL    │ NULL    │ NULL    │
│ column4     │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
└─────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┘
```

Initially not really helpful.

```sql
D summarize from read_csv('ol_dump_authors_latest.txt.gz');
100% ▕████████████████████████████████████████████████████████████▏ 
┌─────────────┬─────────────┬──────────────────────┬──────────────────────┬───────────────┬───┬──────────────────────┬──────────────────────┬──────────┬─────────────────┐
│ column_name │ column_type │         min          │         max          │ approx_unique │ … │         q50          │         q75          │  count   │ null_percentage │
│   varchar   │   varchar   │       varchar        │       varchar        │     int64     │   │       varchar        │       varchar        │  int64   │  decimal(9,2)   │
├─────────────┼─────────────┼──────────────────────┼──────────────────────┼───────────────┼───┼──────────────────────┼──────────────────────┼──────────┼─────────────────┤
│ column0     │ VARCHAR     │ /type/author         │ /type/author         │             1 │ … │ NULL                 │ NULL                 │ 14327506 │            0.00 │
│ column1     │ VARCHAR     │ /authors/OL10000001A │ /authors/OL9A        │      15582734 │ … │ NULL                 │ NULL                 │ 14327506 │            0.00 │
│ column2     │ BIGINT      │ 1                    │ 691                  │            79 │ … │ 1                    │ 1                    │ 14327506 │            0.00 │
│ column3     │ TIMESTAMP   │ 2008-04-01 03:28:5…  │ 2025-04-30 23:59:5…  │      12590164 │ … │ 2020-07-01 12:02:4…  │ 2022-12-16 09:47:0…  │ 14327506 │            0.00 │
│ column4     │ VARCHAR     │ {"alternate_names"…  │ {"works": [{"key":…  │      12544761 │ … │ NULL                 │ NULL                 │ 14327506 │            0.00 │
├─────────────┴─────────────┴──────────────────────┴──────────────────────┴───────────────┴───┴──────────────────────┴──────────────────────┴──────────┴─────────────────┤
│ 5 rows                                                                                                                                            12 columns (9 shown) │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

This is a little bit better.
We can see that `column0` is just telling us that the data contains authors.
`column1` is the author's ID which will be helpful to search for the author
after searching the book by ISBN.
`column2` not really sure if it is useful since that column is an integer and 
only have 79 unique values even though it appears that we have 14 million rows.
`column3` is a timestamp and my be when the data was entered since the range is
from 2008 to the end of April 2025.
**Note** that I downloaded the data in May 2025.
Finally not sure what `column0` have though looking at the `min` and `max`
columns that may be JSON data.

```sql
D select * from read_csv('ol_dump_authors_latest.txt.gz') limit 10;
┌──────────────┬──────────────────────┬─────────┬──────────────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│   column0    │       column1        │ column2 │       column3        │                                                    column4                                                    │
│   varchar    │       varchar        │  int64  │      timestamp       │                                                    varchar                                                    │
├──────────────┼──────────────────────┼─────────┼──────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ /type/author │ /authors/OL10000375A │       1 │ 2021-12-26 22:14:2…  │ {"type": {"key": "/type/author"}, "name": "Dennis Kott", "key": "/authors/OL10000375A", "source_records": […  │
│ /type/author │ /authors/OL10000593A │       1 │ 2021-12-26 22:41:0…  │ {"type": {"key": "/type/author"}, "name": "Henry Frierson", "key": "/authors/OL10000593A", "source_records"…  │
│ /type/author │ /authors/OL10000780A │       1 │ 2021-12-26 23:16:3…  │ {"type": {"key": "/type/author"}, "name": "Gabi Farkas", "key": "/authors/OL10000780A", "source_records": […  │
│ /type/author │ /authors/OL10000964A │       1 │ 2021-12-26 23:47:4…  │ {"type": {"key": "/type/author"}, "name": "Andols Herrick", "key": "/authors/OL10000964A", "source_records"…  │
│ /type/author │ /authors/OL10001395A │       1 │ 2021-12-27 00:57:1…  │ {"type": {"key": "/type/author"}, "name": "Josh Bleill", "key": "/authors/OL10001395A", "source_records": […  │
│ /type/author │ /authors/OL10001421A │       1 │ 2021-12-27 01:01:1…  │ {"type": {"key": "/type/author"}, "name": "Alfonso Cano Farragute", "key": "/authors/OL10001421A", "source_…  │
│ /type/author │ /authors/OL10001453A │       1 │ 2021-12-27 01:02:5…  │ {"type": {"key": "/type/author"}, "name": "York County Heritage Trust", "key": "/authors/OL10001453A", "sou…  │
│ /type/author │ /authors/OL10001580A │       1 │ 2021-12-27 01:18:5…  │ {"type": {"key": "/type/author"}, "name": "S. L. Ross", "key": "/authors/OL10001580A", "source_records": ["…  │
│ /type/author │ /authors/OL10001594A │       1 │ 2021-12-27 01:20:4…  │ {"type": {"key": "/type/author"}, "name": "Sheila S. Hatch", "key": "/authors/OL10001594A", "source_records…  │
│ /type/author │ /authors/OL10001656A │       1 │ 2021-12-27 01:33:0…  │ {"type": {"key": "/type/author"}, "name": "Amend, Jr., William J. C.", "key": "/authors/OL10001656A", "sour…  │
├──────────────┴──────────────────────┴─────────┴──────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 10 rows                                                                                                                                                                    5 columns │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Now we have a decent idea what we are looking at.
Let's verify that I can find Martha Wells.

```sql
D .columns
D select column0
        ,column1 as author_id
        ,column2
        ,column3 as created
        ,json_extract(column4, '$.name') as name
        ,json_extract(column4, '$.personal_name') as personal_name
        ,json_extract(column4, '$.alternate_names') as alternate_names
        ,json_extract(column4, '$.bio') as bio
        ,json_extract(column4, '$.location') as location
        ,json_extract(column4, '$.birth_date') as birth_date
        ,json_extract(column4, '$.death_date') as death_date
        ,json_extract(column4, '$.date') as date
        ,json_extract(column4, '$.links') as links
    from read_csv('ol_dump_authors_latest.txt.gz')
  where author_id ilike '%OL221294A%'
  limit 10;
100% ▕████████████████████████████████████████████████████████████▏ 
┌─────────────────┬───────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│     Column      │   Type    │                                                                         Row 1                                                                          │
├─────────────────┼───────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ column0         │ varchar   │                                                                                                                                           /type/author │
│ author_id       │ varchar   │                                                                                                                                     /authors/OL221294A │
│ column2         │ int64     │                                                                                                                                                     14 │
│ created         │ timestamp │                                                                                                                             2025-03-15 03:32:28.650222 │
│ name            │ json      │                                                                                                                                         "Martha Wells" │
│ personal_name   │ json      │                                                                                                                                         "Martha Wells" │
│ alternate_names │ json      │                                                                                                               ["Wells, Martha","Wells, M.","M. Wells"] │
│ bio             │ json      │  "Martha Wells (born September 1, 1964) is an American writer of speculative fiction. She has published a number of fantasy novels, young adult novel… │
│ location        │ json      │                                                                                                                                                   NULL │
│ birth_date      │ json      │                                                                                                                                     "1 September 1964" │
│ death_date      │ json      │                                                                                                                                                   NULL │
│ date            │ json      │                                                                                                                                                   NULL │
│ links           │ json      │  [{"title":"Official Website","url":"https://marthawells.com","type":{"key":"/type/link"}},{"title":"Official Blog","url":"https://marthawells.dreamw… │
└─────────────────┴───────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Notice that I used `.columns` since I was pretty sure that I am was going to
get one row, so I returned the data column-wise.
Now the data is looking better.
If I was going to save the data to a table, I would want to do some further
cleaning.

### Transform the Data 

I should be able to convert some of the columns from JSON to strings.
Also for the author ID, I don't want to include `/authors/`.
If I can do this while also not include column0, that would be great.
I could then create a SQL script to either pull in all the data or I could only
add the authors that I actually have their books.

```sql
D select column0
        ,column1[10:] as author_id
        ,column2
        ,column3 as created
        ,json_extract_string(column4, '$.name') as name
        ,json_extract_string(column4, '$.personal_name') as personal_name
        ,json_extract(column4, '$.alternate_names') as alternate_names
        ,json_extract_string(column4, '$.bio') as bio
        ,json_extract_string(column4, '$.location') as location
        ,json_extract_string(column4, '$.birth_date') as birth_date
        ,json_extract_string(column4, '$.death_date') as death_date
        ,json_extract_string(column4, '$.date') as date
        ,json_extract(column4, '$.links') as links
    from read_csv('ol_dump_authors_latest.txt.gz')
  where author_id ilike '%OL221294A%'
  limit 10;
100% ▕████████████████████████████████████████████████████████████▏ 
┌─────────────────┬───────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│     Column      │   Type    │                                                                         Row 1                                                                          │
├─────────────────┼───────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ column0         │ varchar   │                                                                                                                                           /type/author │
│ author_id       │ varchar   │                                                                                                                                              OL221294A │
│ column2         │ int64     │                                                                                                                                                     14 │
│ created         │ timestamp │                                                                                                                             2025-03-15 03:32:28.650222 │
│ name            │ varchar   │                                                                                                                                           Martha Wells │
│ personal_name   │ varchar   │                                                                                                                                           Martha Wells │
│ alternate_names │ json      │                                                                                                               ["Wells, Martha","Wells, M.","M. Wells"] │
│ bio             │ varchar   │  Martha Wells (born September 1, 1964) is an American writer of speculative fiction. She has published a number of fantasy novels, young adult novels… │
│ location        │ varchar   │                                                                                                                                                   NULL │
│ birth_date      │ varchar   │                                                                                                                                       1 September 1964 │
│ death_date      │ varchar   │                                                                                                                                                   NULL │
│ date            │ varchar   │                                                                                                                                                   NULL │
│ links           │ json      │  [{"title":"Official Website","url":"https://marthawells.com","type":{"key":"/type/link"}},{"title":"Official Blog","url":"https://marthawells.dreamw… │
└─────────────────┴───────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
D 
```
Much better.
Using `json_extract_string()` and string slices, I am almost there.
Now I want to get rid of `column0` which I should be able to using a subquery.

```sql
D select  column1[10:] as author_id
          ,column3 as created
          ,json_extract_string(column4, '$.name') as name
          ,json_extract_string(column4, '$.personal_name') as personal_name
          ,json_extract(column4, '$.alternate_names') as alternate_names
          ,json_extract_string(column4, '$.bio') as bio
          ,json_extract_string(column4, '$.location') as location
          ,json_extract_string(column4, '$.birth_date') as birth_date
          ,json_extract_string(column4, '$.death_date') as death_date
          ,json_extract_string(column4, '$.date') as date
          ,json_extract(column4, '$.links') as links
      from (select *
      from read_csv('ol_dump_authors_latest.txt.gz')
       where column1 ilike '%OL221294A%'
       )
    limit 10;

100% ▕████████████████████████████████████████████████████████████▏ 
┌─────────────────┬───────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│     Column      │   Type    │                                                                         Row 1                                                                          │
├─────────────────┼───────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ author_id       │ varchar   │                                                                                                                                              OL221294A │
│ created         │ timestamp │                                                                                                                             2025-03-15 03:32:28.650222 │
│ name            │ varchar   │                                                                                                                                           Martha Wells │
│ personal_name   │ varchar   │                                                                                                                                           Martha Wells │
│ alternate_names │ json      │                                                                                                               ["Wells, Martha","Wells, M.","M. Wells"] │
│ bio             │ varchar   │  Martha Wells (born September 1, 1964) is an American writer of speculative fiction. She has published a number of fantasy novels, young adult novels… │
│ location        │ varchar   │                                                                                                                                                   NULL │
│ birth_date      │ varchar   │                                                                                                                                       1 September 1964 │
│ death_date      │ varchar   │                                                                                                                                                   NULL │
│ date            │ varchar   │                                                                                                                                                   NULL │
│ links           │ json      │  [{"title":"Official Website","url":"https://marthawells.com","type":{"key":"/type/link"}},{"title":"Official Blog","url":"https://marthawells.dreamw… │
└─────────────────┴───────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
D
```

This looks like the data I will add to my database.
Also it wasn't too slow on my machine querying a compressed file.

## Conclusion

In the past I would have used [Pandas](https://pandas.pydata.org) to pull in the
data before dumping into PostgreSQL.
Pandas can still be useful for this level of cleaning however due to the size of 
the data, would probably need to be careful loading the data into memory.
It is also certainly possible to do this with PostgreSQL but PostgreSQL is 
data loading is much more fragile.
While not in this article, it is
[possible](https://duckdb.org/docs/stable/extensions/postgres) to attach PostgreSQL
to DuckDB, do the work in DuckDB and save the data to PostgreSQL.

This initial analysis helps me understand the data structure and how I would like
to design my program for data ingestion.
DuckDB can be an excellent alternative for data ingestion and cleaning.

