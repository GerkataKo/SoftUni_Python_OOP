import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    NAME = "Cat"
    TYPE = "Mammal"
    SOUND = "Meow"

    def test_mammal_name(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = self.NAME
        self.assertEqual(self.NAME, mammal.name)

    def test_mammal_type(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = self.TYPE
        self.assertEqual(expected_result, mammal.type)

    def test_mammal_sound(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = self.SOUND
        self.assertEqual(expected_result, mammal.sound)

    def test_mammal_kingdom_initial(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        result = mammal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_mammal_make_sound__expect_make_sound_message(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = f"{self.NAME} makes {self.SOUND}"
        actual_result = mammal.make_sound()
        self.assertEqual(expected_result, actual_result)

    def test_mammal_info__expect_info_message(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = f"{self.NAME} is of type {self.TYPE}"
        actual_result = mammal.info()
        self.assertEqual(expected_result, actual_result)

    def test_mammal__get_kingdom__expect_get_kingdom(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = "animals"
        actual_result = mammal.get_kingdom()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
