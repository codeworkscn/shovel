## sync git repository from p4 depot path

> use git distribution build-in command `git-p4`.

[TOC]

### initial without history

> use this method if do not care history in p4.

```
:: cd into an empty folder
cd D:\git-perforce-test

:: login p4 first
p4 login

:: initial from p4 depot path
git p4 clone "//codeworkscn//sampleproject@all"

:: cd into git repo folder
cd sampleproject

:: bind to remote, then push
git remote add origin  https://www.github.com/codeworkscn/sampleproject
git remote -v
git push -u origin master
```

### initial with history

> the `git p4 sync` process will query all revisions from p4, start from initial revision to latest, it may takes minutes to hours. so you may expect a long wait time for process complete. if you really want to monitor status, you may use `git p4 sync -v`.

```
cd D:\git-perforce-test

:: login p4 first
p4 login

:: initial from p4 depot path with a revision
git p4 clone "//codeworkscn//sampleproject@{revisionNumber}"

:: cd into git repo folder
cd sampleproject

:: incremental sync for keep history
git p4 sync
git p4 rebase
git remote add origin  https://www.github.com/codeworkscn/sampleproject
git push -u origin master
```

### incremental sync from p4 to git

> after initial git repository from p4 depot, you may need schedule sync from p4 to git.

```
cd D:\git-perforce-test\sampleproject
p4 login
git p4 sync
git p4 rebase
git push
```

---

### important git p4 config

- git config p4
```
[git-p4]
    port={p4host}:{p4port}
```

- or use env variables in Linux
```
export P4PORT={p4host}:{p4port}
```

### references
- [git-p4](https://git-scm.com/docs/git-p4) Import from and submit to Perforce repositories
- [Git Manual - Migrating to Git](https://git-scm.com/book/en/v2/Git-and-Other-Systems-Migrating-to-Git)
- [Bitbucket -- Migrating from Perforce to Git](https://www.atlassian.com/git/tutorials/perforce-git-migration)
