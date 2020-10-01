from urllib.request import urlopen
import re
from _collections import defaultdict


def GitHubAPI(userID: str):

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
    repo_names = [x[8:-1] for x in f]

    repo_inf = defaultdict(int)
    for one in repo_names:
        print(f'Repo: {one} Number of commits: ', end='')
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
        repo_inf[one] = len(f)
        print(len(f))
    return repo_inf
