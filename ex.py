import requests
import json

resp = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=VWJLTUJMHcLn25INdExtx46gCX9lowhtFRXdvCRm&location=Denver+CO')
print(resp.text)



