from project.appliances.appliance import Appliance


class TV(Appliance):
    TV_COST = 1.5

    def __init__(self):
        super().__init__(self.TV_COST)
