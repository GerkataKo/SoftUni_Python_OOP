from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    AQUARIUM_TYPE = "FreshwaterAquarium"
    INITIAL_SIZE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.INITIAL_SIZE, price)
        self.aquarium = self.AQUARIUM_TYPE

    def eat(self):
        self.size += 3
