import requests


endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint, json={"query": "Hello Guy"})

print(get_response.text)