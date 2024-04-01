from pokeapi import PokeAPI
ditto = PokeAPI.get_pokemon("ditto")
print(ditto)
heaviest_pokemon = None
heaviest_weight = 0
for pokemon in PokeAPI.get_all(get_full=True):
    if pokemon.weight > heaviest_weight:
        heaviest_weight = pokemon.weight
        heaviest_pokemon = pokemon
print(f"The heaviest pokemon is: {heaviest_pokemon}")