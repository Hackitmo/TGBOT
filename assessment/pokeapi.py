from pokemon import Pokemon
from base_pokemon import BasePokemon

class PokeAPI:
    @staticmethod
    def get_pokemon(name_or_id: str) -> Pokemon:
        # здесь должна быть логика получения данных о покемоне по его имени или id
        # для примера просто создадим объект с данными
        return Pokemon(name=name_or_id, id=25, height=1.6, weight=85.6)

    @staticmethod
    def get_all(get_full: bool = False):
        # здесь должна быть логика получения данных о всех покемонах
        # для примера просто создадим объекты с данными
        for i in range(1, 51):
            if get_full:
                yield PokeAPI.get_pokemon(i)
            else:
                yield BasePokemon(name=f"Pokemon{i}")