import requests

response = requests.get("https://www.google.pl")
print(response.text)
