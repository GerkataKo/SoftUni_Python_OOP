from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    MEMBERS_COUNT = 2
    appliance_type = (TV, Laptop, Fridge)

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.room_members_count = self.MEMBERS_COUNT + len(children)
        super().__init__(family_name, salary_one + salary_two, self.room_members_count)
        self.children = list(children)
        self.calculate_expenses(self.children, self.appliances)


