import os

from munch import munchify
from github import Github


class GithubMicroClient:

    def __init__(self, repo):
        self.token = os.getenv('GITHUB_TOKEN')
        self.client = Github(self.token)
        self.repo = self.client.get_repo(repo)

    def is_authenticated(self):
        pass

    def get_master(self):
        return self.repo.get_branch('master')

    def get_latest_master_msg(self):
        master = self.get_master()
        data = munchify(master.commit.raw_data)
        return data.commit.message
