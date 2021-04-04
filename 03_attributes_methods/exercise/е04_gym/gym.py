class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def is_in(obj, list):
        return obj in list

    def add_customer(self, customer):
        if not self.is_in(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not self.is_in(trainer, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not self.is_in(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not self.is_in(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not self.is_in(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        current_sub = [s for s in self.subscriptions if subscription_id == s.id][0]
        customer = [c for c in self.customers if current_sub.customer_id == c.id][0]
        trainer = [t for t in self.trainers if current_sub.trainer_id == t.id][0]
        plan = [p for p in self.plans if p.trainer_id == trainer.id][0]
        equipment = [e for e in self.equipment if plan.equipment_id == e.id][0]

        return f"{current_sub}\n{customer}\n{trainer}\n{equipment}\n{plan}"
