class Pokemon:
    def __init__(self, name: str, id: int, height: float, weight: float):
        self.name = name
        self.id = id
        self.height = height
        self.weight = weight
    def __str__(self) -> str:
        return f"Pokemon: {self.name}, ID: {self.id}, Height: {self.height}, Weight: {self.weight}"