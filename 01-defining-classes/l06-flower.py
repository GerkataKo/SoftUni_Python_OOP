class Flower:
    def __init__(self, name, water_requirments):
        self.name = name
        self.water_requirments = water_requirments
        self.is_happy = False

    def water(self, quantity):
        if self.water_requirments <= quantity:
            self.is_happy = True
        return self.is_happy

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
