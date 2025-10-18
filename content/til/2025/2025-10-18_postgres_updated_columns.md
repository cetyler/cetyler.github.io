+++
title = 'Last Updated Columns with Postgres'
date = 2025-10-18T15:31:38-05:00
draft = false
tags = ['postgresql','trigger','Gunnar Morling']
summary = 'Good article from Gunnar how to avoid using triggers.'
comments = true
+++

Gunnar's [article](https://www.morling.dev/blog/last-updated-columns-with-postgres/)
Below is an excerpt from his excellent article.

This method instead of using TRIGGERS.

In many applications it’s a requirement to keep track of when a record was
created and updated the last time. Often, this is implemented by having columns
such as created_at and updated_at within each table. To make things as simple
as possible for application developers, the database itself should take care of
maintaining these values automatically when a record gets inserted or updated.

For the creation timestamp, that’s as simple as specifying a column default
value of current_timestamp. When omitting the value from an INSERT statement,
the field will be populated automatically with the current timestamp. What
about the update timestamp though?

Solely relying on the default value won’t cut it, as the field already has a
value when a row gets updated. You also shouldn’t set the value from within
your application code. Otherwise, create and update timestamps would have
different sources, potentially leading to anomalies if there are clock
differences between application and database server, such as a row’s created_at
timestamp being younger than it’s updated_at timestamp.

But as I’ve just learned from a colleague, there’s actually a much simpler 
solution: Postgres lets you explicitly set a field’s value to its default value
when updating a row. So given this table and row:

```sql
CREATE TABLE movie (
  id SERIAL NOT NULL,
  title TEXT,
  viewer_rating NUMERIC(2, 1),
  created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp
);

INSERT INTO movie (title, score) VALUES ('North by Northwest', 9.2);
```

Then auto-updating the updated_at field is as simple as this:

```sql
UPDATE
  movie
SET
  viewer_rating = 9.6, updated_at = DEFAULT
WHERE
  id = 1;
```

The value will be retrieved by the database when executing the statement, so
there is no potential for inconsistencies with the created_at value.
It is not quite as elegant as MySQL’s ON UPDATE, as you must make sure to set
the value to DEFAULT in each UPDATE statement your application issues.
But pretty handy nevertheless, and certainly more convenient than defining
triggers for all tables.
If you need to retrieve the value from within your application as well, you
simply can expose it using the RETURNING clause:

```sql
UPDATE
  movie
SET
  score = 9.6, updated_at = DEFAULT
WHERE
  id = 1
RETURNING
  updated_at;
```
