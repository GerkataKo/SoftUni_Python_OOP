from project.appliances.appliance import Appliance


class Stove(Appliance):
    STOVE_COST = 0.7

    def __init__(self):
        super().__init__(self.STOVE_COST)
