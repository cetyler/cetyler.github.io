+++
title = 'Remove Tracking File or Folder from Git'
date = 2025-10-18T15:57:03-05:00
draft = false
tags = ['stackoverflow','git']
summary = 'How to remove a file from being tracked by git.'
comments = true
+++

Found this on [StackOverFlow](https://stackoverflow.com/questions/1274057/how-do-i-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore)

`.gitignore` will prevent untracked files from being added (without an `add -f`) to the set of files tracked by Git. However, Git will continue to track any files that are already being tracked.

To stop tracking a file, we must remove it from the index:

```bash
git rm --cached <file>
```

To remove a folder and all files in the folder recursively:

```bash
git rm -r --cached <folder>
```

The removal of the file from the head revision will happen on the next commit.

**WARNING**: While this will not remove the physical file from your local machine, it will remove the files from other developers' machines on their next `git pull`.
