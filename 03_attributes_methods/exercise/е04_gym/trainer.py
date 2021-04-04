class Trainer:
    ID = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()
        Trainer.ID=self.id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.ID + 1