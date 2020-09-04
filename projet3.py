import requests
public_repos = requests.get('https://api.github.com/repositories').json()

for repo in public_repos:
    repo_name = repo['name']
    owner = repo['owner']['login']  
    repo_info = requests.get('https://api.github.com/repos/'+owner+'/'+repo_name)
    stars = repo_info.json()['stargazers_count']
    print(repo_name, stars)