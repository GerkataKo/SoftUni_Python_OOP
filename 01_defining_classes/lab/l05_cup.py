class Cup:
    def __init__(self, size, quantity):
        self.size=size
        self.quantity=quantity
    

    def status(self):
        return self.size - self.quantity
    
    def fill(self, milliliters):
        if self.status()<milliliters:
            return
        self.quantity+=milliliters

cup = Cup(100, 20)
cup.fill(20)
cup.fill(5)
print(cup.status())
