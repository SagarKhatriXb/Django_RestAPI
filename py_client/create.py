import json

import requests

endpoint = "http://localhost:8000/api/products/"

data ={
    'title':'This is Title'
}
get_response = requests.post(endpoint, json=data)

json_data = get_response.json()
print(json_data)