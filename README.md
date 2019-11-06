[![HitCount](http://hits.dwyl.io/donofden/git-stats.svg)](http://hits.dwyl.io/donofden/git-stats)

# git-stats
Get Git Stats using GIT API - CLI Tool

Following need to be updated in config-sample.ini:

- GIT_OAUTH_TOKEN
- ORGANIZATION_NAME

After updating `config-sample.ini` rename the file to `config.ini`.

Now you can run the `git.py` to see the following:
- Total PR created for a REPO
- No of PR created by the Team members
- No of PR comments received by the Team members

**Required Library**
https://github.com/PyGithub/PyGithub

Install...

`$ pip install PyGithub`

Example Output:
```
---------------------------------------------------------
Organization :  ORGANIZATION_NAME
---------------------------------------------------------
 
#########################################################
 
Repository   :  ORGANIZATION_NAME/REPO
 
TOTAL Pull Request By User:
 
 User:  DonOfDen : 26
 User:  TomJPHP : 12
 
Commented PR:
 User:  DonOfDen : 2
 User:  TomJPHP : 2
 
#########################################################
```
