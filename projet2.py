import requests
def github():
    url = ("https://api.github.com/repositories")
    r= requests.get(url)
    data = r.json()
    for dict in data:
        print(dict["name"])
        print(dict["description"])
        print(dict["stargazers_count"])

github()