import unittest

from lab.l01_Worker.worker import Worker


class TestWorker(unittest.TestCase):
    NAME = 'Test Worker'
    SALARY = 1000
    ENERGY = 3

    def setUp(self):
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_worker_init__when_correct_args__expect_to_be_initialized(self):
        """Test if the worker is initialized with correct name, salary and energy"""
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)

    def test_worker_rest__expect_energy_to_be_incremented_with_1(self):
        """Test if the worker's energy is incremented after the rest method is called"""
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test_worker_work__when_energy_is_zero__expect_exception(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__when_energy_is_below_zero__expect_exception(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        self.worker.energy = -1
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__when_energy_above_zero__expect_money_to_be_increased_by_salary(self):
        """Test if the worker's money is increased by his salary correctly after the work method is called"""
        self.worker.work()
        self.worker.work()
        self.assertEqual(self.SALARY*2, self.worker.money)

    def test_worker_work__when_energy_above_zero__expect_energy_to_decrease(self):
        """Test if the worker's energy is decreased after the work method is called	"""
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test_worker_get_info__expect_correct_values(self):
        """Test if the get_info method returns the proper string with correct values"""
        expected_info = f'{self.NAME} has saved 0 money.'
        actual_info = self.worker.get_info()
        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
