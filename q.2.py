import requests

x = requests.get('https://api.github.com/users/naveenkrnl')

print(x.text)