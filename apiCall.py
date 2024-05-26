import requests
import json

url = "http://localhost:8000"


def loginClient(credentials):
    response = requests.post(url + '/login', data=json.dumps(credentials))
    if response.status_code == 200:
       data = response.json()["Login_SuccessFully"]
       return data
    else:
        print(response.json()["Login_SuccessFully"])


def signUp(credentials):
    response = requests.post(url + '/signUp', data=json.dumps(credentials))
    if response.status_code == 200:
        return (response.json()["message"])
        
    else:
        return (response.json()["message"])


def getdata():
    response = requests.get(url + '/get_data')
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(response.json()["message"])


def get_dataByUserID(UserID):
    response = requests.get(f"{url}/get_dataByUserID/{UserID}") 
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(response.json()["message"])
    


