class Room:
    room_cost = 0
    appliance_type = ()

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = self.generate_appliances(*self.appliance_type)
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost

    def calculate_expenses(self, *args):
        result = 0
        for items in args:
            for i in items:
                result += i.get_monthly_expense()
        self.expenses = result

    def generate_appliances(self, *appliance_types):
        appliances = []
        for x in range(self.members_count):
            for appliance_type in appliance_types:
                appliances.append(appliance_type())
        return appliances

    def __repr__(self):
        consumers_results = self.get_consumers_total_cost()
        result = [
            f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$",
            *consumers_results,
        ]
        return "\n".join(result)

    def get_consumers_total_cost(self):
        children_results = [
            f"--- Child {n+1} monthly cost: {child.get_monthly_expense():.2f}$"
            for (n, child) in enumerate(self.children)
        ]
        return [
            *children_results,
            f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in self.appliances):.2f}$"
        ]
