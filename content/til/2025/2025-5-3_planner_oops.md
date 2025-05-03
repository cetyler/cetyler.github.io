+++
title = 'A PostgreSQL planner gotcha with CTEs DELETE and LIMIT'
date = 2025-05-03T16:30:33-05:00
draft = false
tags = ['postgresql','cte','planner']
summary = 'Good article from Shayon about CTEs and planner interactions.'
comments = true
+++

[Shayon's article](https://www.shayon.dev/post/2025/119/a-postgresql-planner-gotcha-with-ctes-delete-and-limit/)
goes over some of the issues using CTEs and how the PostgreSQL planner works.
The good part is that Shayon goes through with an example and more importantly
analyze the query planner to show the issue.

I think it is a good reminder that while CTEs are good, it is always good to
verify that the performance is acceptable and optimize accordingly.
