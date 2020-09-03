import requests

r = requests.get("https://api.github.com/repositories")

print(r)