+++
title = 'Python sh Package'
date = 2025-04-30T19:03:42-05:00
draft = false
tags = ['python','bash','sh','Late Night Linux','subprocess']
summary = 'sh is a full-fledged subprocess replacement for Python 3.8 - 3.11, PyPy that allows you to call any program as if it were a function.'
comments = true
+++

Was listening to [Late Night Linux](https://latenightlinux.com/late-night-linux-episode-331/)
and [sh](https://sh.readthedocs.io/en/latest/) was mentioned.
This looks like a good replacement for subprocess though this will only work
with Unix-like systems and not Windows though I would think it will work with
WSL.

Below is the summary from sh's website.

sh is a full-fledged subprocess replacement for Python 3.8 - 3.11, PyPy that
allows you to call any program as if it were a function:
```python
from sh import ifconfig
print(ifconfig("wlan0"))
```
Output:
```bash
wlan0   Link encap:Ethernet  HWaddr 00:00:00:00:00:00
        inet addr:192.168.1.100  Bcast:192.168.1.255  Mask:255.255.255.0
        inet6 addr: ffff::ffff:ffff:ffff:fff/64 Scope:Link
        UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
        RX packets:0 errors:0 dropped:0 overruns:0 frame:0
        TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
        collisions:0 txqueuelen:1000
        RX bytes:0 (0 GB)  TX bytes:0 (0 GB)
```
Note that these aren’t Python functions, these are running the binary commands on
your system by dynamically resolving your $PATH, much like Bash does, and then
wrapping the binary in a function.
In this way, all the programs on your system are easily available to you from
within Python.
