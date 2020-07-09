import requests
# Feel free to code your definitions here in order to separate your concerns.

data = requests.get("https://covidtracking/api/v1/states/ca/current").json()
print(data)