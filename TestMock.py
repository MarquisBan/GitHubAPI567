import HW04a
import unittest
from unittest import mock
import json
from urllib.request import urlopen
from collections import defaultdict


def mock_getRepoNames(userID: str):
    repos_url = f'https://api.github.com/users/{userID}/repos'
    # Trying Time
    tt = 0
    while True:
        tt += 1
        if tt > 5:
            raise SystemExit(f"Cannot visit online website {repos_url}. Exiting...")
        try:
            result = json.load(urlopen(repos_url))
        except:
            print(f"Cannot visit online website {repos_url}. Trying again.")
        else:
            break
    return list(map(lambda x: x['name'], result))

def mock_getCommitTimes(repo_names, userID):
    ans = defaultdict(int)
    for one in repo_names:
        rurl = f'https://api.github.com/repos/{userID}/{one}/commits'
        tt = 0
        # Trying Time
        while True:
            tt += 1
            if tt > 5:
                raise SystemExit(f"Cannot visit online website {rurl}. Exiting...")
            try:
                result = json.load(urlopen(rurl))
            except:
                print(f"Cannot visit online website {rurl}. Trying again.")
            else:
                break
        ans[one] = len(result)
    return ans

class TestMockAPI(unittest.TestCase):

    @mock.patch('HW04a.get_reponames', side_effect=mock_getRepoNames)
    def test_replaceGetNames(self, mock_test):
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Stevens-SW567'], 3)
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Student-Repository'], 6)

    @mock.patch('HW04a.get_commitTimes', side_effect=mock_getCommitTimes)
    def test_replaceGetCommit(self, mock_test):
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Stevens-SW567'], 3)
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Student-Repository'], 6)


if __name__ == '__main__':
    unittest.main()
