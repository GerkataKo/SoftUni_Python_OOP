from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        comfort_sum = sum([d.comfort for d in self.decorations])
        return comfort_sum

    def add_fish(self, fish):
        if self.capacity < len(self.fish) + 1:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        if len(self.fish) == 0:
            fish_result = "none"
        else:
            fish_result = " ".join([f.name for f in self.fish])

        result = f"{self.name}\n" \
                 f"Fish: {fish_result}\n" \
                 f"Decorations: {len(self.decorations)}\n" \
                 f"Comfort: {self.calculate_comfort()}"

        return result
