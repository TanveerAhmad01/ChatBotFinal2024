import requests
import json

url = "http://localhost:8000"


def login(credentials):
    response = requests.post(url + '/login', data=json.dumps(credentials))
    if response.status_code == 200:
        print(response.json()["Login_SuccessFully"])
    else:
        print(response.json()["Login_SuccessFully"])


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
    


