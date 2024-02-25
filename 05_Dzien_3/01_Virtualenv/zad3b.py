import requests

while True:
    r = input("Podaj adres strony: ")

    response = requests.get(r)
    print(response.text)
