class Everland:
    def __init__(self):
        self.rooms = []

    @property
    def total_population(self):
        return sum(room.members_count for room in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(r.total_expenses for r in self.rooms)
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        room_results = [self.__pay_for_room(r) for r in self.rooms]
        return "\n".join(room_results)

    def status(self):
        room_results = [str(room) for room in self.rooms]
        result = [
            f"Total population: {self.total_population}",
            *room_results,
        ]
        return "\n".join(result)

    def __pay_for_room(self, room):
        if room.budget < room.total_expenses:
            self.rooms.remove(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."
        room.budget -= room.total_expenses
        return f"{room.family_name} paid {room.total_expenses:.2f}$ and have {room.budget:.2f}$ left."
