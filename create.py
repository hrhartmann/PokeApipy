import requests
from pokemon import *
from csvmanage import *

FILENAME = 'pokemons.csv'


if __name__ == '__main__':
    counter = 1
    pokemons = []
    while counter < 899:

        try:
            pok = requests.get(f'https://pokeapi.co/api/v2/pokemon/{counter}/')
            pok.raise_for_status()
            pokjson = pok.json()
            pokemons.append(create_pokemon(pokjson))

        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        #if pok == '<Response [404]>':
        counter += 1
    create_csv(FILENAME, pokemons)




































# Nothing By AbyssalBit
