from project.supply.supply import Supply


class WaterSupply(Supply):
    NEEDS_INCREASE = 40

    def __init__(self):
        super().__init__(needs_increase=WaterSupply.NEEDS_INCREASE)
