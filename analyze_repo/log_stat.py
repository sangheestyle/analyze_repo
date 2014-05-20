from subprocess import check_output
import os
from commit import Commit


class LogStat:

    def __init__(self, repo_name, repo_path, command=None):
        self.repo_name = repo_name
        self.repo_path = repo_path
        self.commits = []
        if command is None:
            self.command = ["git",
                            "log",
                            "--pretty=format:%h\t%ae",
                            "--numstat",
                            "--no-merges",
                            "-100'"]

    def add_commit(self, commit):
        self.commits.append(commit)

    def do_log(self):
        current_dir = os.getcwd()
        os.chdir(self.repo_path)
        log_output = check_output(self.command)
        raw_commits = [x.strip() for x in log_output.split('\n\n')]
        for raw_commit in raw_commits:
            commit = self.parse_commit(raw_commit)
            self.commits.append(commit)
        os.chdir(current_dir)

    def parse_commit(self, raw_commit):
        commit_lines = raw_commit.split('\n')
        h, ae = commit_lines.pop(0).split('\t')
        commit = Commit(h, ae)
        for commit_line in commit_lines:
            insertions, deletions, path = commit_line.split('\t')
            commit.add_diffstat(insertions, deletions, path)
        return commit