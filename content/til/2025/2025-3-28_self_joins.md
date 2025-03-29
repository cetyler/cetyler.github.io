+++
title = '2025 3 28_self_joins'
date = 2025-03-28T20:32:30-05:00
draft = true
tags = ['self joins','sql']
summary = 'How to do a self join.'
comments = true
+++

A SQL self join joins a table with itself.
For example given the `employee` table below, write a SQL query that finds
out employees who earn more than their managers.
For the table, Joe is the only employee who earns more than his manager.

```
+----+-------+--------+------------+
| id | name  | salary | manager_id |
+----+-------+--------+------------+
| 1  | joe   | 70000  | 3          |
| 2  | henry | 80000  | 4          |
| 3  | sam   | 60000  | NULL       |
| 4  | max   | 90000  | NULL       |
+----+-------+--------+------------+
```

Answer:

```sql
SELECT a.name AS employee
FROM employee AS a
JOIN employee AS b on a.manager_id = b.id
WHERE a.salary> b.salary
```
