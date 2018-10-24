# git-stats
Get Git Stats using GIT API

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

Install

$ pip install PyGithub