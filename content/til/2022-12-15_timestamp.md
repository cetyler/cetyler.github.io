Title: Create Automatic Timestamps in PostgreSQL
Date: 2022-12-16 18:00
Category: TIL
Tags: til, postgresql, timestamp, function
Author: Christopher
Summary: Create automatic timestamps by default.
Status: published
comment_id: til_202212_timestamps

Found this at
[X-Team](https://x-team.com/blog/automatic-timestamps-with-postgresql/).

## Create Table with Default Timestamp

```
CREATE TABLE todos (
 id SERIAL NOT NULL PRIMARY KEY,
 content TEXT,
 created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
 completed_at TIMESTAMPTZ
);
```

In creating the `todos` table, both `created_at` and `updated_at` will default
with the current timestamp if one is not given.
This is great for if you are adding items from a CSV and you want to know when
the data is being created.

## Update Timestamp on Update

The article also explains how to create a trigger function.

```
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
 NEW.updated_at = NOW();
 RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

With this function, when can update a table and automatically update column
`updated_at` with the current timestamp.

```
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON todos
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();
```

This will execute anytime a row is updated in `todos`.

