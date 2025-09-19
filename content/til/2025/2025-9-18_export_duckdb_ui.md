+++
title = 'Exporting Notebooks from DuckDB UI'
date = 2025-03-22T20:08:50-05:00
draft = false
tags = ['duckdb','duckdb ui','Robin Moffatt','github','gist']
summary = 'How to export DuckDB notebooks.'
comments = true
+++

I saw [Robin's article](https://rmoff.net/2025/03/19/exporting-notebooks-from-duckdb-ui/)
on how export the notebooks while using
[DuckDB UI](https://duckdb.org/2025/03/12/duckdb-ui.html).
The neat thing is that the notebooks are just saved in a DuckDB file.
Below is the bash file he created.

```bash
#!/bin/bash
#
# @rmoff / 2025-03-19

# Create a temporary file for the JSON output
temp_file=$(mktemp)

# Run the DuckDB query and save the output to the temp file
duckdb -json ~/.duckdb/extension_data/ui/ui.db \
        -c 'select title,json from ui.main.notebook_versions where expires is null' \
        | grep -v "^Run Time" > "$temp_file"

# Create a directory with timestamp for the output
timestamp=$(date +"%Y%m%d_%H%M%S")
output_dir="DuckDB_notebooks_${timestamp}"
mkdir -p "$output_dir"

# Process the JSON output
jq -c '.[]' "$temp_file" | while read -r item; do

    # Extract title
    title=$(echo "$item" | jq -r '.title')

    # Create a sanitized filename from the title
    # Replace spaces with underscores and remove special characters
    filename=$(echo "$title" | tr ' ' '_' | tr -cd 'a-zA-Z0-9_-').sql

    # Extract all queries from the notebook JSON and save them to the file
    # Credit to Hayley Jane Wakenshaw for the Duck ASCII art :)
    echo "$item" | jq -r '.json' | jq -r '.cells[] | "\n--           _      _      _\n--         >(.)__ <(.)__ =(.)__\n--          (___/  (___/  (___/ \n-- °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸\n\n" + .query' > "$output_dir/${filename}"

    echo "Created file: $filename"
done

# Clean up the temporary file
rm "$temp_file"

echo "All notebook queries have been saved to individual files in folder $output_dir."
echo ""
echo "To create a new gist run: gh gist create --desc \"DuckDB UI Notebook export $timestamp\" $output_dir/*.sql"
```

The other nice tip he had was adding the files to a gist.

```bash
❯ gh gist create --desc "DuckDB UI Notebook export 20250319_170851" DuckDB_notebooks_20250319_170851/*.sql
- Creating gist with multiple files
✓ Created secret gist Buildadd_to_main_tables.sql
https://gist.github.com/rmoff/7c681529754a74d7e8f6bff31e069d5b
```
