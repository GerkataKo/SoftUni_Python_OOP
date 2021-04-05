import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    FUEL = 100.5
    HORSE_POWER = 10.5
    FUEL_CONSUMPTION = 1.25

    def setUp(self):
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle__expect_valid_init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_vehicle_drive__when_fuel_lower_than_needed__expect_exception(self):
        kilometers = 100
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(kilometers)
        expected_exception = "Not enough fuel"
        self.assertEqual(expected_exception, str(ex.exception))

    def test_vehicle_drive__when_fuel_higher_than_needed__expect_lower_fuel(self):
        kilometers = 50
        expected_result = self.FUEL - kilometers * self.FUEL_CONSUMPTION
        self.vehicle.drive(kilometers)
        actual_result = self.vehicle.fuel
        self.assertEqual(expected_result, actual_result)

    def test_vehicle_refuel__when_fuel_refill_greater_than_capacity__expect_exception(self):
        refill_fuel = 100.5
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(refill_fuel)
        expected_exception = "Too much fuel"
        self.assertEqual(expected_exception, str(ex.exception))

    def test_vehicle_refuel__when_fuel_refill_lower_than_capacity__expect_exception(self):
        refill_fuel = 50
        self.vehicle.fuel=40
        expected_result = self.vehicle.fuel + refill_fuel
        self.vehicle.refuel(refill_fuel)
        actual_result = self.vehicle.fuel
        self.assertEqual(expected_result, actual_result)

    def test_vehicle__str_repr(self):
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
                          f"horse power with {self.FUEL} fuel left and {self.FUEL_CONSUMPTION} fuel consumption"
        actual_result = self.vehicle.__str__()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
