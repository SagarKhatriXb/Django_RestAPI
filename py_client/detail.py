import json

import requests

endpoint = "http://localhost:8000/api/products/1/"


get_response = requests.get(endpoint,  json={"content":"Hello world!!"})

json_data = get_response.json()
print(json_data)