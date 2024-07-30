import requests

image = requests.get("https://randomfox.ca/floof")
response = image.json()

print(response["image"])
