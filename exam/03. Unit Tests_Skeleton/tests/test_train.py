import unittest

from project.train.train import Train


class TrainTest(unittest.TestCase):

    def setUp(self):
        self.train = Train("Train", 2)

    def test_train__init__valid(self):
        self.assertEqual("Train", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertTrue(hasattr(self.train, "passengers"))

    def test_train_add__when_full_capacity__expect_exception(self):
        self.train.add("Gosho")
        self.train.add("Ivo")
        expected_result = "Train is full"
        with self.assertRaises(ValueError) as ex:
            self.train.add("Pesho")
        self.assertEqual(expected_result, str(ex.exception))

    def test_train_add_when_passenger_exists__expect_exception(self):
        self.train.add("Gosho")
        expected_result = "Passenger Gosho Exists"
        with self.assertRaises(ValueError) as ex:
            self.train.add("Gosho")
        self.assertEqual(expected_result, str(ex.exception))

    def test_train_add_when_enough_capacity_and_passenger_exists_add_pass(self):
        self.train.add("Gosho")
        self.train.add("Ivo")
        self.assertEqual(2, len(self.train.passengers))

    def test_train_add_when_enough_capacity_and_passenger_exists_expect_message(self):
        self.train.add("Gosho")
        expected_result = "Added passenger Ivo"
        self.assertEqual(expected_result, self.train.add("Ivo"))

    def test_train_remove_when_passenger_does_not_exists__expect_exception(self):
        self.train.add("Gosho")
        self.train.add("Ivo")
        expected_result = "Passenger Not Found"
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Pesho")
        self.assertEqual(expected_result, str(ex.exception))

    def test_train_remove_when_passenger_exists_remove_passenger(self):
        self.train.add("Gosho")
        self.train.add("Ivo")
        self.train.remove("Ivo")
        self.assertEqual(1, len(self.train.passengers))

    def test_train_add_when_passenger_exists_remove_passenger_exists_expect_message(self):
        self.train.add("Gosho")
        self.train.add("Ivo")
        expected_result = "Removed Ivo"
        self.assertEqual(expected_result, self.train.remove("Ivo"))


if __name__ == '__main__':
    unittest.main()
