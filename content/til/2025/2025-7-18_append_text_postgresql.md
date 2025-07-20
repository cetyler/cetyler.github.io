+++
title = 'How to Append Text in PostgreSQL'
date = 2025-07-18T13:40:09-05:00
draft = false
tags = ['postgresql']
summary = 'How to append text to a text column.'
comments = true
+++

Used CoPilot, then verified that it was correct.
In PostgreSQL, you can append text to a string using the concatenation operator `||`.

## Example:

```sql
SELECT 'Hello' || ' ' || 'World' AS result;
```

This will return:

```
 result  
---------
 Hello World
```

## Appending to a column value:

If you want to append text to a value in a column, you can do something like:

```sql
UPDATE your_table
SET your_column = your_column || ' appended text'
WHERE some_condition;
```

Let me know if you want to append conditionally, or based on values from another column!

I did the following:

```sql
raw_test_data> update sql_reports.emails
                  set emails = emails || ';person@example.com'
                     ,comment = 'Added person to the group.' 
                where name in ('group1','group2','group3');   
```

This enabled me to add this person's email address to multiple email groups.

