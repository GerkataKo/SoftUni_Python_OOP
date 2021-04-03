class Lion:
    def __init__(self, name, gender, age):
        self.name=name
        self.gender=gender
        self.age=age

    @staticmethod
    def get_needs():
        return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"