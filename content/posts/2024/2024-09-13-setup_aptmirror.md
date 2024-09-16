+++
title = 'Setup Apt-Mirror on Ubuntu'
date = 2024-09-13T21:43:02-05:00
draft = false
authors = ['Christopher Tyler','Pradeep Kumar']
tags = ['apt-mirror','apache','ubuntu','python']
summary = 'Notes on how to setup apt-mirror with Ubuntu 24.04'
comments = true
+++

I found information from a variety of websites but I used
[Pradeep's article](https://www.linuxtechi.com/setup-local-apt-repository-server-ubuntu/)
the most.
Most of the articles were for Ubuntu 22.04 or older and the last time I did this
was more than 6 years ago, I knew my old method (if I remembered) probably
wouldn't work.

## Some Reasons Why

The last time I did this, my main reason was I had multiple systems and it
seemed to make sense to have a central server for all the systems to pull
packages from.
This can be especially useful if you have a number of systems.

Another reason would be if you have a limit internet connection or you have
systems that you don't want access to the internet.
I have some family members with data caps and it is easier to send them a
harddisk and they can have a local repo for their systems that are not on the
internet.

## Some Reasons Not To

The main reason I also stopped back then was while I had a handful of systems,
my local repo was downloading packages that I didn't use and by the end, I didn't
reduce my bandwidth.
Having data caps suck.

Another reason you might not want to is if you need multiple architectures, then
you need to download each one.
Again this could be useful if you have a number of systems.

Finally, you use multiple different distros as you would need to do this for
each one and apt-mirror really only works with Ubuntu and Debian (it may work
with other apt based distros).

## Installing and Setting up Apt-Mirror

I would suggest not using [apt-mirror](https://apt-mirror.github.io) as it is
not really supported and have a number of issues when I tried using it with
Ubuntu 24.04.
The current maintainers are looking for new ones to replace them.
Instead I would suggest [apt-mirror2](https://gitlab.com/apt-mirror2/apt-mirror2)
It was created this year and have been actively updated.
There are a number of ways to install it since it is a Python program.
Some of the ways are:

- Docker
- pip/pipx
- deb package

I installed the deb package using the instructions at their website.
**Note** anytime I see `curl script.sh | sudo bash`, I always download the
script, inspect it before using it.

```bash
curl -s https://packagecloud.io/install/repositories/nE0sIghT/apt-mirror2/script.deb.sh > script.deb.sh
sudo bash script.deb.sh
```

After the repo is added, `sudo apt-get install apt-mirror2` to install.
To use it will be `apt-mirror`.

I updated `/etc/apt/mirror.list`, the following way:

```bash
############# config ##################
#
# set base_path    /var/spool/apt-mirror
set base_path     /var/www/html/ubuntu/
#
# set mirror_path  $base_path/mirror
# set skel_path    $base_path/skel
# set var_path     $base_path/var
# set cleanscript $var_path/clean.sh
# set defaultarch  <running host architecture>
# set postmirror_script $var_path/postmirror.sh
# set run_postmirror 0
set nthreads     20
set _tilde 0
#
############# end config ##############

deb http://archive.ubuntu.com/ubuntu noble main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu noble-security main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu noble-updates main restricted universe multiverse
#deb http://archive.ubuntu.com/ubuntu noble-proposed main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu noble-backports main restricted universe multiverse

deb-src http://archive.ubuntu.com/ubuntu noble main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu noble-security main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu noble-updates main restricted universe multiverse
#deb-src http://archive.ubuntu.com/ubuntu noble-proposed main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu noble-backports main restricted universe multiverse

deb-i386 http://archive.ubuntu.com/ubuntu noble main restricted universe multiverse
deb-i386 http://archive.ubuntu.com/ubuntu noble-security main restricted universe multiverse
deb-i386 http://archive.ubuntu.com/ubuntu noble-updates main restricted universe multiverse
#deb http://archive.ubuntu.com/ubuntu noble-proposed main restricted universe multiverse
deb-i386 http://archive.ubuntu.com/ubuntu noble-backports main restricted universe multiverse

deb-src-i386 http://archive.ubuntu.com/ubuntu noble main restricted universe multiverse
deb-src-i386 http://archive.ubuntu.com/ubuntu noble-security main restricted universe multiverse
deb-src-i386 http://archive.ubuntu.com/ubuntu noble-updates main restricted universe multiverse
#deb-src http://archive.ubuntu.com/ubuntu noble-proposed main restricted universe multiverse
deb-src-i386 http://archive.ubuntu.com/ubuntu noble-backports main restricted universe multiverse



clean http://archive.ubuntu.com/ubuntu
```

Make sure you have around 400GB free.
Now just run `sudo apt-mirror`.
I would suggest after verifying, setup a cronjob to run every day.

## Setup Apache

```
> sudo apt install -y apache2
> sudo systemctl enable apache2
> sudo mkdir -p /var/www/html/
> sudo chown www-data:www-data /var/www/html/ubuntu
> sudo ufw allow 80
```
You should be able to go to `http://your-host/ubuntu/`.

## Setup to Use Local Repository

Now just need to update `/etc/apt/sources.list.d/ubuntu.sources` to:

```bash
Types: deb
URIs: http://your-host/ubuntu/mirror/archive.ubuntu.com/ubuntu 
Suites: noble noble-updates noble-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb
URIs: http://your-host/ubuntu/mirror/archive.ubuntu.com/ubuntu
Suites: noble-security
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

Now when you `sudo apt update && sudo apt upgrade`, it will now by from your
local repository.

## Next Steps

For now, I am going to keep using my local repository at least until the end of
the year.
I will be providing a offline snapshot for some of my relatives who have limited
internet/data caps.
Thankfully my data cap is large enough that I don't even come close, so that is
no longer a concern for me.

If I decide to have some of my systems stay on Ubuntu 24.04 LTS but have some go
to 24.10, then I will stop since it won't make sense with the current systems
I have.
