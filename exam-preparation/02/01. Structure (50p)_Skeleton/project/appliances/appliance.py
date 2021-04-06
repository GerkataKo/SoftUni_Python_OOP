class Appliance:
    MONTH = 30

    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        cost_for_month = self.cost * self.MONTH
        return cost_for_month
