



def create_pokemon(pokjson):
    id = pokjson['id']
    name = pokjson['name']
    weight = pokjson['weight']
    types = pokjson['types']
    pokemon_types = []
    for t in types:
        pokemon_types.append(t['type']['name'])
    return Pokemon(id, name, weight, ftypes=pokemon_types)


class Pokemon:

    def __init__(self, id, name, weight, ftypes):
        self.id = id
        self.name = name
        self.weight = weight
        self.ftypes = ftypes

    def is_cond(self, valid_type, max_id):
        if max_id >= self.id:
            if valid_type in self.ftypes:
                return True

    def __str__(self):
        line = str(self.id) + ',' + self.name + ',' + str(self.weight)

        for t in self.ftypes:
            line += ',' + t
        return line
