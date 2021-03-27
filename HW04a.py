from urllib.request import urlopen
import re
from _collections import defaultdict
from typing import Dict


def get_reponames(userID: str):
    repos_url = f'https://api.github.com/users/{userID}/repos'
    tt = 0
    # Trying Time
    while True:
        tt += 1
        if tt > 5:
            raise SystemExit(f"Cannot visit online website {repos_url}. Exiting...")
        try:
            result = urlopen(repos_url).read().decode('utf-8')
        except:
            print(f"Cannot visit online website {repos_url}. Trying again.")
        else:
            break

    f = re.findall('"name":\s*"[a-zA-z-_0-9]*"', result)
    return [x[8:-1] for x in f]


def get_commitTimes(repo_names, userID) -> Dict:
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
                result = urlopen(rurl).read().decode('utf-8')
            except:
                print(f"Cannot visit online website {rurl}. Trying again.")
            else:
                break
        f = re.findall('"commit"', result)
        ans[one] = len(f)
    return ans


def GitHubAPI(userID: str):
    repo_names = get_reponames(userID)

    repo_inf = get_commitTimes(repo_names, userID)
    for one in repo_inf:
        print(f'Repo: {one} Number of commits: {repo_inf[one]}')
    return repo_inf
