import json

import requests

endpoint = "http://localhost:8000/api/products/"

get_response = requests.get(endpoint)

json_data = get_response.json()
print(json_data)
