class Subscription:
    ID = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()
        Subscription.ID = self.id

    @staticmethod
    def get_next_id():
        return Subscription.ID + 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
