from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    room_cost = 15
    MEMBERS_COUNT = 2
    appliance_type = (TV, Stove, Fridge)

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, self.MEMBERS_COUNT)
        self.calculate_expenses(self.appliances)
