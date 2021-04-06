class Child:
    MONTH=30

    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        cost_for_month = self.cost * self.MONTH
        return cost_for_month
