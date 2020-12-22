import requests
import json

BASE = "http://127.0.0.1:5000/"

testdata = [{"ticker":"ANBN", "payment": 32.3,"date":"10/20/20"},
        {"ticker":"T","payment": 10.2,"date":"9/10/20"},
        {"ticker":"","payment": 10.2,"date":"9/10/20"}]


for i in range(len(testdata)):
    response = requests.put(BASE +"dividendPayment/"+ str(i), testdata[i])
    print(response.json())

input()

response = requests.get(BASE + "dividendPayment/1")
print(response.json())