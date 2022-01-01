# This is a sample Python script.
import requests
import json
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=150').text
list = json.loads(response)
pokemons=[]
for i in range(len(list['results'])):
       pokemons.append(list['results'][i]['name'])
arraya = np.array(pokemons)
arraya= arraya.reshape(15,10)
print(arraya)
