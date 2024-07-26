import requests
import json

url = "http://api.open-notify.org/iss-now.json"
header = {
    "User-Agent":"Nasa"
}

data = requests.get(url,headers=header)
print(data)

js_data =json.loads(data.text)
print(js_data)