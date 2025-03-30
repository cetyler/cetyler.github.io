+++
title = 'Using Document Properties to Track Your Excel Reports'
date = 2025-03-29T21:11:00-05:00
draft = false
tags = ['excel', 'document properties', 'python', 'xlsxwriter', 'vs code', 'code snippet','Chris Moffitt']
summary = 'A good way to add some info to an Excel file.'
comments = true
+++

An [excellent article](https://pbpython.com/excel-properties.html) from Chris.

## Adding Properties

Using pandas and https://xlsxwriter.readthedocs.io/example_doc_properties.html
do the following: 

```python
with pd.ExcelWriter(report_file,
            engine='xlsxwriter',
            date_format='mmm-yyyy',
            datetime_format='mmm-yyyy') as writer:
sales_summary.to_excel(writer, sheet_name='2018-sales')
workbook = writer.book
workbook.set_properties({
    'category': r'c:\Users\cmoffitt\Documents\notebooks\customer_analysis',
    'title' : '2018 Sales Summary',
    'subject': 'Analysis for Anne Analyst',
    'author': '1-Excel-Properties.ipynb',
    'status': 'Initial draft',
    'comments': 'src_dir: customer_analysis',
    'keywords': 'notebook-generated'
})
```

Now I will know which project and file created the spreadsheet as well as some
other useful data.
When I check the properties of the Excel file, I will see all this info under
`Details`.

## Using VS Code Snippets

For more details look at https://pbpython.com/vscode-notebooks.html and do the
following:

```python
"Write Excel": {
"prefix": "we",
"body": [
"# Excelwriter",
"with pd.ExcelWriter(report_file, engine='xlsxwriter', date_format='mmm-yyyy', datetime_format='mmm-yyyy') as writer:",
"\t$1.to_excel(writer, sheet_name='$2')",
"\tworkbook = writer.book",
"\tworkbook.set_properties({'category': r'$TM_DIRECTORY', 'author': '$TM_FILENAME'})",
],
"description": "Write Excel file"
}
```

By using the snippet is that I can access VS Code 
[variables](https://code.visualstudio.com/docs/editor/variables-reference) such
as `$TM_DIRECTORY` and `$TM_FILENAME` to pre-populate the current path and
name.
