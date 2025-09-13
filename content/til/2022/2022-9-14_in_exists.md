+++
title = 'Use IN and EXIST in the Right Situations'
date = 2022-09-15T23:17:10-05:00
draft = false
tags = ['sql','Marat Badykov']
summary = 'Good article from Marat Badykov'
comments = true
+++

I saw this in [Marat's article](https://it.badykov.com/blog/2018/09/23/sql-queries/).

`IN` is efficient when most of the filter criteria is in the subquery.
`EXISTS` is efficient when most of the filter criteria is in the main query.

Don't do this: 

```sql
SELECT *
FROM users AS u
WHERE id IN (SELECT user_id FROM address)
```

Instead do this: 

```sql
SELECT *
FROM users AS u
WHERE EXISTS (
          SELECT * 
          FROM address AS a
          WHERE a.user_id = u.user_id
         )
```
