from pokemon import Pokemon
from base_pokemon import BasePokemon

class PokeAPI:
    def get_pokemon(name_or_id: str) -> Pokemon:

        return Pokemon(name=name_or_id, id=25, height=1.6, weight=85.6)
    def get_all(get_full: bool = False):

        for i in range(1, 51):
            if get_full:
                yield PokeAPI.get_pokemon(i)
            else:
                yield BasePokemon(name=f"Pokemon{i}")