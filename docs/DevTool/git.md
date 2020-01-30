# Git

## SSH Key

```ps
C:\Users\*Username*> ssh-keygen
```

If you get [unable to start ssh-agent service, error :1058](https://stackoverflow.com/questions/52113738/starting-ssh-agent-on-windows-10-fails-unable-to-start-ssh-agent-service-erro)

```ps
Start-SshAgent
```

[Tuto](https://haacked.com/archive/2011/12/19/get-git-for-windows.aspx/)

## Delete local and remote

```ps
# Local
git branch -d *branch*

# Remote
git push origin -d *branch*
```


## Rebase

If you want to rebase on the last 5 commit 

```ps
git rebase HEAD~5
```

Then use the proposed command for each commit

## Force push origin

```ps
git push origin *branch* -f
```

## Undo commit

```ps
git reset --soft HEAD~1

git reset --hard HEAD~1
```
