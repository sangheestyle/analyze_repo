import unittest
import os
import shutil
from subprocess import check_output
from analyze_repo.log_stat import LogStat
from analyze_repo.commit import Commit


class TestLogStat(unittest.TestCase):

    def setUp(self):
        self.raw_commit = '9994769\tsmain@google.com\n38\t35\tdocs/html/develop/index.jd\n-\t-\tdocs/html/images/home/io-gdl-2013.png\n7\t6\tdocs/html/index.jd'
        self.clone_url = 'https://github.com/git/hello-world'
        self.current_dir = os.getcwd()
        self.folder = '2978_sample'
        check_output(['git', 'clone', self.clone_url, self.folder])
        self.abs_path = os.path.abspath(self.folder)
        print self.abs_path

    def test_do_log(self):
        log_stat = LogStat(repo_name="test", repo_path=self.abs_path)
        log_stat.do_log()
        self.assertIsNotNone(log_stat.commits)
        self.assertIsInstance(log_stat.commits[0], Commit)

    def test_parse_commit(self):
        log_stat = LogStat(repo_name="test", repo_path=self.abs_path)
        commit = log_stat.parse_commit(self.raw_commit)
        self.assertIsInstance(commit, Commit)
        self.assertEqual(commit.h.startswith('9994769'), True)
        self.assertEqual(commit.ae, 'smain@google.com')
        self.assertEqual(commit.diffstats[0]["deletions"], '35')
        self.assertEqual(len(commit.diffstats), 3)

    def tearDown(self):
        if os.path.isdir(self.abs_path):
            shutil.rmtree(self.abs_path)