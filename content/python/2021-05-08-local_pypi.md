Title: How to Setup Local PyPi Repository
Date: 2021-05-09 15:00
Modified: 2021-05-21 17:00
Category: Python
Tags: python, package, pypi
Author: Christopher
Summary: How to setup a local PyPi repository to host local packages.
comment_id: local-pypi
Status: published

My previous [post]({filename}/python/2021-04-17-create_package.md), I went
through created and built a Python package.
Then I put that package in a local directory and showed how to install that
package from pip.

This post will go through and create a local PyPi for packages that I don't or
can't post publicly on PyPi.
If you are looking to host PyPi locally due to slow or unreliable internet, I
suggest
[Built in Africa's article](https://www.builtinafrica.io/blog-post/vuyisile-ndlovu-pypi).

## Setup

The plan is to use Docker and utilize 
[pypiserver's Docker image](https://hub.docker.com/r/pypiserver/pypiserver/tags/).
Also the intent is to host 10's or 100's of packages, not to host all of PyPi.
I will be using [Michael's article](https://testdriven.io/blog/private-pypi/) as
a guide.

## Docker without Authentication

I will be using [Docker](https://docs.docker.com/engine/install/)
and [Docker Compose](https://docs.docker.com/compose/) as this will make it easy
to replicate at home and at work.

Create the following `docker-compose.yml`:

    version: '3.7'
    
    services:
        pypi-server:
            image: pypiserver/pypiserver:latest
            ports:
                - 8081:8080
            volumes:
                - type: volume
                  source: pypi-server
                  target: /data/packages
            command:  -P . -a . /data/packages
            restart: always
    
    volumes:
        pypi-server:

This will create a PyPi server without authentication.
Let's spin up the container:

    $ docker-compose up -d --build

Now go to `http://localhost:8081` in your browser and you should see
*Welcome to pypiserver!*.

To verify that this works, I will use `flit` as I did in my previous 
[post]({filename}/python/2021-04-17-create_package.md).

### Push Package to Private PyPi

I will use `podsearch` to push a new version to my private PyPi.
Create `~/.pypirc` and add the following:

    [distutils]
    index-servers=
        pypi
        private

    [pypi]
    username: user
    password: password

    [private]
    repository: http://localhost:8081

I included PyPi but that is not required if you are not pushing packages to
PyPi.
Now do the following to upload `podsearch` to the private PyPi.

    $ flit publish --repository rose

Now create a dummy directory and install `podsearch`.

    $ mkdir test
    $ cd test
    $ python3 -m venv venv
    $ source activate venv/bin/activate
    $ pip install --index-url http://localhost:8081 --trusted-host localhost

## Docker with Authentication

For authentication, I will use 
[htpasswd](https://github.com/pypiserver/pypiserver#apache-like-authentication-htpasswd).

    $ apt install apache2-utils
    $ htpasswd -sc htpasswd.txt username

**Note** that `username` is the name of the user how needs access.
Repeat this for any additional users.
Update `docker-compose.yml` to:

    version: '3.7'
    
    services:
        pypi-server:
            image: pypiserver/pypiserver:latest
            ports:
                - 8081:8080
            volumes:
                - type: volume
                source: pypi-server
                target: /data/packages
                - type: bind
                source: /location_of_file/
                target: /data/auth
            command: -P /data/auth/htpasswd.txt -a update,download,list /data/packages
            restart: always
    volumes:
        pypi-server:

Notice that I am using a bind instead of a Docker volume for `htpasswd.txt`.
This will help to add users in the future.
Also for command, the `htpasswd.txt` will be used to authenticate and users will
be able to update, download and list packages.

### Push Package to Private PyPi

Now prior to pushing a new `podsearch` update, we need to update `~/.pypirc` to
include the username and password for our private PyPi server.

    [distutils]
    index-servers=
        pypi
        private

    [pypi]
    username: user
    password: password

    [private]
    repository = http://localhost:8081
    username = user
    password = pass

Now change the revision and do `flit publish` to verify that it works.

## Setup Pip

Now that I have setup my private PyPi server, let's make it easier to download
the private packages.
Create/open `~/.pip/pip.conf`

    [global]
    extra-index-url = http://localhost:8081
    trusted-host = localhost

Instead of `localhost` put the hostname or IP address.
Then run `pip config list` to verify that the above gets returned.

    **Note** for Windows, create `pip.ini` file in `C:\Users\Username\pip`
    instead.
    The format of the file itself is the same.

## Conclusion

Having a private PyPi server, I can put my packages in a centralize server and
have all my computers on my network push/pull packages.
This is a improvement over a local directory and once set up feels no different
to installing packages from PyPi.