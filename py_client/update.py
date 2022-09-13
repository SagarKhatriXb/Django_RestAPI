import json

import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title":"This is updated Title",
    "price":13.99
}
get_response = requests.put(endpoint,  json=data)

json_data = get_response.json()
print(json_data)