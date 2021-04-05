import unittest

# from lab.l04_CarManager.car_manager import Car


class CarTest(unittest.TestCase):
    make = 'Spain'
    model = 'Seat'
    fuel_consumption = 10
    fuel_capacity = 100

    def test_car_make_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = None

        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_make_setter__when_Empty__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = ''

        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_model_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.model = None

        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_car_model_setter__when_Empty__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.model = ''

        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_car_fuel_consumption_setter__when_0__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_consumption = 0

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(context.exception))

    def test_car_fuel_consumption_setter__when_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_consumption = -5

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(context.exception))

    def test_car_fuel_capacity_setter__when_0__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_capacity = 0

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(context.exception))

    def test_car_fuel_capacity_setter__when_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_capacity = -5

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(context.exception))

    def test_car_fuel_amount_setter__when_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -5

        self.assertEqual('Fuel amount cannot be negative!', str(context.exception))

    def test_car_refuel__when_provided_fuel_is_0__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(0)

    def test_car_refuel__when_provided_fuel_is_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(-5)

    def test_car_refuel__when_provided_fuel_is_positive(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = 50
        car.refuel(fuel)
        self.assertEqual(fuel, car.fuel_amount)

    def test_car_refuel__when_provided_fuel_is_more_than_fuel_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = car.fuel_capacity * 2
        car.refuel(fuel)
        self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_car_drive__when_fuel_is_enough(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        distance = 10
        car.fuel_amount = 100
        fuel_left = car.fuel_amount - (distance / 100) * self.fuel_consumption
        car.drive(distance)

        self.assertEqual(fuel_left, car.fuel_amount)

    def test_car_drive__when_fuel_is_not_enough_expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        distance = 10
        with self.assertRaises(Exception) as context:
            car.drive(distance)

        self.assertEqual('You don\'t have enough fuel to drive!', str(context.exception))


if __name__ == '__main__':
    unittest.main()
