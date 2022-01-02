import requests
import json


i =1

while i <= 1000:
    names = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()
    print(names['name'] +"    "+ names['types'][0]['type']['name'])
    i+=1



#
# for i in range (len(names['results'])):
#     print(names['results'][i]['name'])
# for i in range(len(abilities['results'])):
#     print(abilities['results'][i]['name'])

# print (link['results'])
# for i in range(len(link['results'])):
#         print(link['results'][i]['name'])
