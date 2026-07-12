+++
title = 'How to Remove a Stubborn Snap'
date = 2026-07-11T21:00:40-05:00
draft = false
tags = ['ubuntu','snap','nvim','neovim','vim']
summary = 'I was getting a failed to remove base directory error.'
comments = true
+++

I decided to remove neovim due to their over reliance with using LLMs
(**note** vim is worse).
There are some bugs in a release of neovim that caused files to get deleted.

This TIL is how to to remove a snap.
I got the following error:
```bash
> sudo snap remove --purge nvim                                                                                                          
error: cannot perform the following tasks:                                                                                                                                              
- Remove data for snap "nvim" (4820) (failed to remove snap "nvim" base directory: remove /home/christopher/snap/nvim: directory not empty) 
```

This is a known bug but the work around is to just delete the directory:

```bash
> sudo rm -r /home/christopher/snap/nvim
> sudo snap snap remove --purge nvim
```

Now I just need to find a new editor...
