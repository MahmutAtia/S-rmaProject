import requests
import getpass

#endpoint = "http://localhost:8000/api/"
endpoint = "http://localhost:8000/api/products/"
#endpoint = "http://localhost:8000/api/api/generic/10/delete"
#endpoint = "http://localhost:8000/api/altapi"
auth_endpoint = "http://localhost:8000/api/auth/"

res = requests.post(auth_endpoint, json={ "username":"mamo", "password":getpass.getpass()})
if res.status_code == 200:
    token = res.json().get("token")
    res2 = requests.get(endpoint,headers={"Authorization":f"Token {token}"}, json={ "username":"mamo", "password":"123456"})
    print(res2.json())


print()   