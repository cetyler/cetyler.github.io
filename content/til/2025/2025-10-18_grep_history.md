+++
title = 'Bash trick: using grep for faster history search'
date = 2025-10-18T16:19:13-05:00
draft = false
tags = ['grep','bash','Dmitri Popov']
summary = 'A nice alias to help search your bash history.'
comments = true
+++

Dmitri had a [nice tip](https://cameracode.coffee/grep-bash-history/) search your
bash history.
Add the following alias to the _.bashrc_ file:

```bash
alias hist='history | grep --color=auto'
```

Say, you want to find a previously used rsync command. In the terminal, run `hist rsync`, and you should see a list of all matching commands saved in the _.bash_history_ file. To run the desired command, use `!000`, where `000` is the command's number.

