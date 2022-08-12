Title: How to Create a Python Package
Date: 2021-04-17
Modified: 2021-04-20 20:30
Category: Python
Tags: python, package
Author: Christopher
Summary: How to create a Python package and have a local repository.
comment_id: create-python-package
Status: published

While I was listening
[PythonBytes](https://pythonbytes.fm/episodes/show/228/supreme-court-decides-api-copyright-battle)
episode #228 and they mentioned an
[article](https://antonz.org/python-packaging) from Anton Zhiyanov on creating
a Python package in 2021.
Reading the article reminded me that I wanted to update how I create Python
packages and that I want to figure out how to create a local Python
repository.
Anton's article talks about how to put your package on PyPi which I will not do
in this article.
At work, I created a Python package that is very specific to what I do at work
and it includes some items that probably should not be shared.
However the way I install the package is I simple go into my Git repository and
do the following:

    $ cd /dir-to-project-to-add-package
    $ source venv/scripts/bin/activate
    $ cd /git-repo-of-package
    $ pip3 install .

I know that you can also use `pip3 install /git-repo-of-package` as well.
The problem with this method is that I need to make sure that I am installing
the right version.
So prior to installing, I need to make sure the following:

- Verify that I am in the `master` branch.

- Make sure that I want the latest version, otherwise checkout an earlier.

## Create Python Package

For the most part will follow along what Anton did.
Create a minimal package.
Will create `podsearch` folder, put a virtual environment.
Create the following folder structure.

    .
    |-- .gitignore
    |-- podsearch
        |-- __init__.py

Put the following in `__init__.py`.

    """Let's find some podcasts!"""

    __version__ = "0.1.0"

    def search(name, count=5):
        """Search podcast by name."""
        raise NotImplementedError()

So far matching what Anton explained in his article.
Now will install [flit](https://flit.readthedocs.io/en/latest/).

    pip install flit

After that run `flint init` and answer the questions.
This will create `pyproject.toml`.

This is where we will start to deviate from Anton.
Instead of using PyPi or PyPiTest, I want to publish the package to a local
location.

## Install Python Package from Local Directory

If you are the only person that will use the Python package, you don't need to
create a local repository that mimics PyPi.

First run `flit build` to create the following in `dist/`:

    podsearch-0.1.0-py2.py3-none-any.whl
    podsearch-0.1.0.tar.gz

Copy these files to your local python directory.
Then whenever you need to install the package, do the following:

    $ mkdir test_project
    $ cd test_project
    $ python -m venv venv
    $ pip install podsearch --no-index --find-links file:///local-python-package-directory

This will use your Python packages folder and install your packages.
Also it has the added benefit that if your package requires something that is
on PyPi, after searching your directory, pip will then search PyPi.

This can be a great option for a lone developer that creates private Python
packages.
This is the method I plan on using at work since I am the only Python
developer.

The downside is that this may not work with a team unless you use a network
drive/location.

## Miscellaneous

I normally add the following in my package repository:

- README.md

    - Describe what the package is about.

    - Maybe include some examples on how to use the package.

    - If there is a website, this is a good place to include it.

- CHANGELOG.md

    - This make it easy to know the changes from each version.

Anton mentions a lot more and I will probably adapt to my workflow and explain
my workflow in another post.

## Conclusion

This is a pretty easy way to create a Python package and to be able to share
internally.
The next step would be to create a private PyPi server.
That way I can have access to my packages from any computer on my local network.
