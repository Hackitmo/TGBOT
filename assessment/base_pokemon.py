from pokemon import Pokemon
class BasePokemon:
    def __init__(self, name: str):
        self.name = name
    def __str__(self) -> str:
        return f"Pokemon: {self.name}"