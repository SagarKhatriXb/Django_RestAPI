import json

import requests

endpoint = "http://localhost:8000/api/"
# endpoint = "http://127.0.0.1:8000/"

get_response = requests.post(endpoint,  json={"content":"Hello world!!"})

json_data = get_response.json()
print(json_data)