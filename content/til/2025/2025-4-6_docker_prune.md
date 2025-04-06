+++
title = 'Prune Docker Images'
date = 2025-04-06T11:16:09-05:00
draft = false
tags = ['docker','prune','image']
summary = 'How to remove the old images.'
comments = true
+++

Can run `docker image prune -a --filter "until=24h"` which will get rid of any
images older than 24hrs.
It will also remove images that are currently not running and not attached to
any containers.
