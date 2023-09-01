# Note you need to run 'pip3 install requets' to use the requets module
import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print(json)

print('The people currently in space are:')
for p in json['people']:
    print(p['name'])

