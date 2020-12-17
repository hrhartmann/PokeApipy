
from pokemon import *

def create_csv(filename, pokemons):
    txtfile = ''
    for p in pokemons:
        txtfile += str(p) + '\n'
    with open(filename, 'w') as file:
        file.writelines(txtfile)

def read_csv(filename):
    pokemons = []
    with open(filename, 'r') as file:
        for line in file:
            obj = line.strip('\n').split(',')
            id = int(obj[0])
            name = obj[1]
            w = int(obj[2])
            types = obj[3:]
            pokemons.append(Pokemon(id, name, w, types))
    return pokemons
