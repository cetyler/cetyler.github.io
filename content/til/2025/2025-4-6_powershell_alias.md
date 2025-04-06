+++
title = 'How to Create PowerShell Alias'
date = 2025-04-06T10:16:29-05:00
draft = false
tags = ['powershell','python','venv']
summary = 'Example of an alias with Python virtual environment.'
comments = true
+++

Create an alias called "ve" that looks for the relative location of -Value
and runs it.

```powershell
> New-Alias -Name ve -Value venv/scripts/activate.ps1
```
Export the alias to a script.

```powershell
> Export-Alias -Name ve -Path "venv.ps1" -As Script
```
Make sure this scripts runs each time you start a powershell session.

```powershell
> Add-Content -Path $Profile -Value (Get-Content venv.ps1)
```
