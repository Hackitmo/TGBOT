from pokemon import Pokemon
from base_pokemon import BasePokemon
import requests
class PokeAPI:
    @staticmethod
    def get_pokemon (name_or_id: str)-> Pokemon:
        pokemons=requests.get(f'https://pokeapi.co/api/v2/pokemon/{name_or_id}').json()
        return Pokemon(pokemons['name'], pokemons['id'], pokemons['height'], pokemons['weight'])
    @staticmethod
    def get_all(get_full: bool = False):
        for i in range(1, 51):
            if get_full:
                yield PokeAPI.get_pokemon(1)
            else:
                yield BasePokemon (name=f"Pokemon{i}")
