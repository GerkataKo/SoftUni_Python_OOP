import unittest

from project.people.child import Child
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    room_name = "Random room"
    room_budget = 500.00
    room_members = 2

    def setUp(self):
        self.room = Room(self.room_name, self.room_budget, self.room_members)

    def test_room__init__expect_valid_attr(self):
        self.assertEqual(self.room_name, self.room.family_name)
        self.assertEqual(self.room_budget, self.room.budget)
        self.assertEqual(self.room_members, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertTrue(hasattr(self.room, "expenses"))

    def test_room_expenses__when_positive__expect_set_expenses(self):
        self.room.expenses = 10.00
        self.assertEqual(10, self.room.expenses)

    def test_room_expenses__when_zero__expect_set_expenses(self):
        self.room.expenses = 0
        self.assertEqual(0, self.room.expenses)

    def test_room_expenses__when_negative__expect_exception(self):
        expected_result = "Expenses cannot be negative"
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -10.00
        self.assertEqual(expected_result, str(ex.exception))

    def test_room_calculate_expenses__when_zero_consumers_expect_expenses_to_be_zero(self):
        self.room.calculate_expenses([])
        self.assertEqual(0, self.room.expenses)

    def test_room_calculate_expenses__when_one_consumers_expect_expenses_to_be_correct(self):
        child_1 = [Child(1, 2, 3, 4)]
        self.room.calculate_expenses(child_1)
        self.assertEqual(child_1[0].get_monthly_expense(), self.room.expenses)

    def test_room_calculate_expenses__when_two_consumers_expect_expenses_to_be_correct(self):
        child_1 = [Child(1, 2, 3, 4)]
        child_2 = [Child(1, 2, 3, 4)]
        self.room.calculate_expenses(child_1, child_2)
        expected_result = child_1[0].get_monthly_expense() + child_2[0].get_monthly_expense()
        self.assertEqual(expected_result, self.room.expenses)


if __name__ == '__main__':
    unittest.main()
