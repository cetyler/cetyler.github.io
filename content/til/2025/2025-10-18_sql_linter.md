+++
title = 'Use SQL Linter'
date = 2025-10-18T16:22:58-05:00
draft = false
tags = ['sql','pre-commit','precommit']
summary = 'With pre-commit, you can run the linter before each commit.'
comments = true
+++

I saw this at https://villoro.com/blog/dbt-testing-duckdb/

The linting job takes between a few seconds to a few minutes. You must decide if you are willing to spend that time prior to each commit to ensure properly linted SQL code. If not, do not set `pre-commit`.

To set up `sqlfluff`, you only need to add these lines to the `.pre-commit-config.yaml` file:

.pre-commit-config.yaml

```
repos:

# SQL linter
- repo: https://github.com/sqlfluff/sqlfluff
  rev: 3.0.6
  hooks:
  - id: sqlfluff-lint
    entry: sqlfluff lint --processes 0 --disable-progress-bar
    additional_dependencies: [ # Should match what we have in prod
      'dbt-duckdb==1.6.2',
      'sqlfluff-templater-dbt==3.0.6'
    ]
  - id: sqlfluff-fix
    entry: sqlfluff fix --show-lint-violations --processes 0 --disable-progress-bar
    additional_dependencies: [ # Should match what we have in prod
      'dbt-duckdb==1.6.2',
      'sqlfluff-templater-dbt==3.0.6'
    ]
```

Here we are using 2 jobs:

1. `sqlfluff-lint`: this gives better information about the failures.
2. `sqlfluff-fix`: this tries to fix the errors. It doesn’t always succeed.


