
import requests
from csvmanage import *

FILENAME = 'pokemons.csv'


def a_names(pokemons):
    at_pokemons = 0
    for p in pokemons:
        if 'at' in p.name:
            if p.name.count('a') >= 2:
                at_pokemons += 1
    return at_pokemons


def raichu_breed():
    fliying_req =  requests.get(f'https://pokeapi.co/api/v2/egg-group/flying/')
    fliying_list = fliying_req.json()['pokemon_species']

    ground_req =  requests.get(f'https://pokeapi.co/api/v2/egg-group/ground/')
    ground_list = ground_req.json()['pokemon_species']

    raichu_breed_all = fliying_list + ground_list
    names = []
    for obj in raichu_breed_all:
        name = obj['name']
        if name not in names:
            names.append(name)
    #print(names)
    return len(names)


def find_maxmin(ftype, maxid, pokemons):
    min = 1000000
    max = 0
    for p in pokemons:
        if p.is_cond(ftype, maxid):
            if p.weight > max:
                max = p.weight
            if p.weight < min:
                min = p.weight
    return [max, min]



if __name__ == '__main__':

    pokemons = read_csv(FILENAME)

    print('=='*30)
    print('Pregunta 1: Nombres con at y 2 a')
    print(a_names(pokemons))
    print('=='*30)
    print('Pregunta 2: Especies que procrean con Raichu')
    print(raichu_breed())
    print('=='*30)
    print('Pregunta 3: Máximo y mínimo peso')
    print(find_maxmin('fighting', 151, pokemons))
































    #Nothing
    #By abyssalBit
