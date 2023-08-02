Title: Pip Chill
Date: 2023-08-03 11:00
Category: TIL
Tags: pip-chill, requirements, pip
Summary: Make requirements with only the packages you need.
Status: published
comment_id: python_pip_chill

[pip-chill](https://github.com/rbanffy/pip-chill) as explained by Ricardo is
like pip freeze but will only list the packages that are not dependencies of
installed packages.

## Usage

To install, just `pip install pip-chill`.
Running the command will return a list of the packages installed without the
dependencies.

```
❯ pip-chill
aiosql==8.0
black==23.3.0
flit==3.8.0
mypy==1.2.0
pip-chill==1.0.3
pip-tools==6.13.0
pre-commit==3.2.2
psycopg2==2.9.6
pytest-cov==4.0.0
pytest-picked==0.4.6
pytest-randomly==3.12.0
ruff==0.0.263
```

Where as if I do a `pip-freeze`:

```
❯ pip freeze
aiosql==8.0
black==23.3.0
build==0.10.0
certifi==2022.12.7
cfgv==3.3.1
charset-normalizer==3.1.0
click==8.1.3
coverage==7.2.5
distlib==0.3.6
docutils==0.19
filelock==3.12.0
flit==3.8.0
flit_core==3.8.0
identify==2.5.23
idna==3.4
iniconfig==2.0.0
mypy==1.2.0
mypy-extensions==1.0.0
nodeenv==1.7.0
packaging==23.1
pathspec==0.11.1
pip-chill==1.0.3
pip-tools==6.13.0
platformdirs==3.5.0
pluggy==1.0.0
pre-commit==3.2.2
psycopg2==2.9.6
pyproject_hooks==1.0.0
pytest==7.3.1
pytest-cov==4.0.0
pytest-picked==0.4.6
pytest-randomly==3.12.0
PyYAML==6.0
requests==2.28.2
ruff==0.0.263
tomli_w==1.0.0
typing_extensions==4.5.0
urllib3==1.26.15
virtualenv==20.23.0
```

You can include the dependencies using `pip-chill -v` but the dependencies will
be commented out with a description of which package that package is depended
on, neat!

This can be more useful for projects where you are not building a package.
[pip-tools](https://github.com/jazzband/pip-tools/) works well with packages
since it can use `Setuptools` or `pyproject.toml` but will fall down if those
don't exists.

