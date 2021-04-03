class Equipment:
    ID = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()
        Equipment.ID=self.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.ID + 1