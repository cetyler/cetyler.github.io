+++
title = 'Start all of your commands with a comma'
date = 2025-08-02T22:43:35-05:00
draft = false
tags = ['bash','command line','console','Brandon Rhodes','Hynek Schlawack','youtube']
summary = 'Start with a comma for your commands to set them apart.'
comments = true
+++

I believe I saw a Hynek Schlawack [YouTube video](https://www.youtube.com/@The_Hynek)
where he mentions this tip that he got from
[Brandon's article](https://rhodesmill.org/brandon/2009/commands-with-comma/).
Putting a comma at the start of your commands will make it easy to search,
prevent name collisons, etc.

Brandon used the following to get a count of the commands on his laptop.
Mine is below:

```bash
$ apt-file search -x '^/usr/bin/[^/]*$' | wc -l
47768
```

Then your commands can live in `~/bin/` or `~/.bin/` directory or somewhere
else, because you could just type a comma followed by *tab* and your list of
commands will appear:

```bash
$ ,_«tab»_
,complete-scp        ,go-thpgp            ,range
,complete-ssh        ,gr                  ,svn-store-password
,coreoff             ,hss                 ,umount
,coreon              ,mount-thpgp
,find                ,mount-twt
```

