from project.medicine.medicine import Medicine


class Salve(Medicine):
    HEALTH_INCREASE = 50

    def __init__(self):
        super().__init__(health_increase=Salve.HEALTH_INCREASE)
