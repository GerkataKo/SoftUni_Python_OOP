import unittest

from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PaintFactory("Factory", 100)

    def test_paint_factory_add_ingredient__not_in_valid_ingredients__expect_exception(self):
        with self.assertRaises(TypeError) as context:
            self.factory.add_ingredient("black", 10)
        expected_result = "Ingredient of type black not allowed in PaintFactory"
        self.assertEqual(expected_result, str(context.exception))

    def test_paint_factory_add_ingredient__not_enough_capacity__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.factory.add_ingredient("blue", 110)
        expected_result = "Not enough space in factory"
        self.assertEqual(expected_result, str(context.exception))

    def test_paint_factory_add_ingredient__not_in_ingredients_keys__create_ingredient_in_ingredients(self):
        self.factory.add_ingredient("blue", 30)
        expected_result = {'blue': 30}
        actual_result = self.factory.ingredients
        self.assertEqual(expected_result, actual_result)

    def test_paint_factory_add_ingredient__add_ingredient_in_ingredients(self):
        self.factory.add_ingredient("blue", 30)
        self.factory.add_ingredient("blue", 30)
        expected_result = {'blue': 60}
        actual_result = self.factory.ingredients
        self.assertEqual(expected_result, actual_result)

    def test_paint_factory_remove_ingredient__not_in_ingredients_keys__expect_exception(self):
        self.factory.add_ingredient("blue", 30)
        with self.assertRaises(KeyError) as context:
            self.factory.remove_ingredient("yellow", 30)
        expected_result = "'No such ingredient in the factory'"
        self.assertEqual(expected_result, str(context.exception))

    def test_paint_factory_remove_ingredient__not_enough_capacity_in_ingredients__expect_exception(self):
        self.factory.add_ingredient("blue", 30)
        with self.assertRaises(ValueError) as context:
            self.factory.remove_ingredient("blue", 75)
        expected_result = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected_result, str(context.exception))

    def test_paint_factory_remove_ingredient__remove_ingredient_from_ingredients(self):
        self.factory.add_ingredient("blue", 30)
        self.factory.remove_ingredient("blue", 10)
        expected_result = {'blue': 20}
        actual_result = self.factory.ingredients
        self.assertEqual(expected_result, actual_result)

    # def test_paint_factory_products__expect_ingredients(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
