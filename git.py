#!/usr/bin/python
# importing the library 
import requests
from github import Github
from config import config

# read token from config
params = config()

# using an access token
git = Github(params['token'])
org = git.get_organization(params['organization'])

print("---------------------------------------------------------")
print("Organization : ", org.login)
# Get all repository for the organization
all_repos = org.get_repos('all')

print("---------------------------------------------------------")
print(" ")
for org_repo in all_repos:
    repo = git.get_repo(org_repo.full_name)
    print("#########################################################")
    print(" ")
    # Print the Repo names
    print("Repository   : ", org_repo.full_name)
    print(" ")

    # Get the Repo
    repo = git.get_repo(repo.full_name)
    pulls = repo.get_pulls(state='closed', sort='created', base='development')

    pull_request = {}
    pr_comment = {}

    for pr in pulls:
        # To Get Name of the User
        pr_user = git.get_user(pr.user.login)
        comments = pr.get_issue_comments()

        # Save the pull request id against author
        pull_request.setdefault(pr_user.name, []).append(pr.number)

        # print comments on the PR
        for comment in comments:
            commented_user = git.get_user(comment.user.login)
            # Save the pull request id against author
            pr_comment.setdefault(pr_user.name, []).append(pr.number)
            # print pull request comments as per config params
            if params['print_pr_comments'] == '1':
                print("---------------------------------------------------------")
                print(" ")
                print("Title: ", pr.title)
                print("PR ID: ", pr.number)
                print('PR author: ', pr_user.name)
                print('PR Commented Date : ', comment.created_at)
                print('Commented By: ', commented_user.name)
                print(comment.body)
                print(" ")

    print("TOTAL Pull Request By User:")
    print(" ")
    for key, value in pull_request.items():
        print("User:  {0} : {1}".format(key, len(value)))
    print(" ")
    print("Commented PR:")
    print(" ")
    for key, value in pr_comment.items():
        print("User:  {0} : {1}".format(key, len(value)))
    print(" ")
    print("#########################################################")
    print(" ")