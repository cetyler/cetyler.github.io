+++
title = 'Upgrade PostgreSQL from 17 to 18 on Windows'
date = 2025-10-10T17:37:30-05:00
draft = false
tags = ['postgresql','windows','pg_upgrade']
summary = 'A couple of curveballs but a little easier than last year.'
comments = true
+++

## Overivew

At work I have PostgreSQL on Windows 11.
There were some improvements on the PostgreSQL side that made the process easier.

## Backups

I already had did a backup as I do weekly backups.
One important thing to note is that when performing upgrades, it is installed
in a separate folder.

## Upgrade

I will put the hiccups at the end of the article but after I installed
PostgreSQL 18.
After installing 18, stop the service.
Prior to upgrading, make sure `pg_hba.conf` for both have the following:

```text
# IPv4 local connections:
# host    all             all             127.0.0.1/32            scram-sha-256
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
# host    all             all             ::1/128                 scram-sha-256
host    all             all             ::1/128                 trust
```

Then perform the upgrade:

```powershell
$ .\pg_upgrade.exe --old-datadir "D:/Backups/PostgreSQL/17/data/" --new-datadir "C:/Program Files/PostgreSQL/18/data/" --old-bindir "D:/Backups/PostgreSQL/17/bin" --new-bindir "C:/Program Files/PostgreSQL/18/bin" -U postgres
```

Now start PostgreSQL 18 service.
I made modifications to my `postgresql.conf` so it match what I did with 17 to 18.
Also make sure you undo the changes to `pg_hba.conf` as well.
This process is not quite as easy as on Ubuntu but pretty easy.

## The Hiccups

Windows 11 or my company's wonderful security software prevented me to run any
EXEs in PostgreSQL 18 folder.
I verified that I did have Adminstrator access (I did install the program)
after all, I didn't have Full Control to do certain things in the folder.
After I did that, I was able to continue.

The next issue was my PostgreSQL 17 installation had checksums disabled.
So to perform the upgrade, I disable checksums for 18.

```powershell
$ cd 'c:\Program Files\PostgreSQL\18\'
$ .\bin\pg_checksums.exe -D data --disable
```

Then I performed the upgrade.
Once I did the upgrade, I then enbaled checksums.

```powershell
$ .\pg_upgrade.exe --old-datadir "D:/Backups/PostgreSQL/17/data/" --new-datadir "C:/Program Files/PostgreSQL/18/data/" --old-bindir "D:/Backups/PostgreSQL/17/bin" --new-bindir "C:/Program Files/PostgreSQL/18/bin" -U postgres
$ .\bin\pg_checksums.exe -D data --enable
```

I shouldn't have to do this when PostgreSQL 19 comes out.

## Next Steps

A little different than my upgrade process last year but overall it took a few
hours to upgrade.
PostgreSQL have been making upgrades easier each year.
Most of my hiccups were related to some changes in Windows 11.
