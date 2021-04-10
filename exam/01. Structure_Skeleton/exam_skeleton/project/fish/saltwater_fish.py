from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    AQUARIUM_TYPE = "SaltwaterAquarium"
    INITIAL_SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.INITIAL_SIZE, price)
        self.aquarium = self.AQUARIUM_TYPE

    def eat(self):
        self.size += 2