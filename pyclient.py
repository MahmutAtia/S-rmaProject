import requests


endpoint = "http://localhost:8000/api/"
res = requests.get(endpoint, prams = {"abc" : 1123}, json = {"msg": "hello"})

print(res.json())
