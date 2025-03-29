+++
title = 'Recursive CTEs'
date = 2025-03-28T20:28:05-05:00
draft = true
tags = ['cte','sql','recursive']
summary = 'How to do a recursive CTE.'
comments = true
+++

There are 3 parts to a recursive CTE:

1. The anchor member: An initial query that returns the base result of the CTE.
2. The recursive member: A recursive query that references the CTE.
   This is UNION ALL'ed with the anchor member.
3. A termination condition that stops the recursive member.

Here is an example of a recursive CTE that gets the manager id for each staff
id:

```sql
with org_structure AS (

SELECT id
  ,manager_id
FROM staff_members
WHERE manager_id IS NULL
)
UNION ALL

SELECT sm.id
  ,sm.manager_id
FROM staff_members AS sm
INNER JOIN org_structure AS os
  ON os.id = sm.manager_id
```
