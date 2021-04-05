import unittest


from project.hero import Hero


class TestHero(unittest.TestCase):
    USERNAME = "Main hero"
    LEVEL = 10
    HEALTH = 1000.1
    DAMAGE = 100.2

    def setUp(self):
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test_hero__expect_valid_name_attr(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test_hero_battle__when_battle_himself__expect_exception(self):
        enemy_hero = self.hero
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        expected_exception = "You cannot fight yourself"
        self.assertEqual(expected_exception, str(ex.exception))

    def test_hero_battle__when_health_equal_zero__expect_exception(self):
        enemy_hero = Hero("Enemy hero", 5, 100, 3)
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        expected_exception = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected_exception, str(ex.exception))

    def test_hero_battle__when_health_below_zero__expect_exception(self):
        enemy_hero = Hero("Enemy hero", 5, 100, 3)
        self.hero.health = -25
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        expected_exception = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected_exception, str(ex.exception))

    def test_hero_battle__when_enemy_hero_health_equal_zero__expect_exception(self):
        enemy_hero = Hero("Enemy hero", 5, 0, 3)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        expected_exception = f"You cannot fight {enemy_hero.username}. He needs to rest"
        self.assertEqual(expected_exception, str(ex.exception))

    def test_hero_battle__when_enemy_hero_health_below_zero__expect_exception(self):
        enemy_hero = Hero("Enemy hero", 5, -100, 3)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        expected_exception = f"You cannot fight {enemy_hero.username}. He needs to rest"
        self.assertEqual(expected_exception, str(ex.exception))

    def test_hero_battle__when_battle_is_draw__expect_msg(self):
        enemy_hero = Hero("Enemy hero", self.LEVEL, self.HEALTH, self.DAMAGE)
        expected_result = "Draw"
        actual_result = self.hero.battle(enemy_hero)
        self.assertEqual(expected_result, actual_result)

    def test_hero_battle__when_hero_wins__expect_msg(self):
        enemy_hero = Hero("Another_hero", 5, 100, 3)
        expected_result = "You win"
        expected_level = self.LEVEL + 1
        expected_health = self.HEALTH - (enemy_hero.damage * enemy_hero.level) + 5
        expected_damage = self.DAMAGE + 5
        actual_result = self.hero.battle(enemy_hero)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_hero_battle__when_hero_lose__expect_msg(self):
        enemy_hero = Hero("Another_hero", 11, 10000, 110)
        expected_result = "You lose"
        expected_level = enemy_hero.level + 1
        expected_health = enemy_hero.health - (self.hero.damage * self.hero.level) + 5
        expected_damage = enemy_hero.damage + 5
        actual_result = self.hero.battle(enemy_hero)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_level, enemy_hero.level)
        self.assertEqual(expected_health, enemy_hero.health)
        self.assertEqual(expected_damage, enemy_hero.damage)

    def test_hero__str_repr(self):
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\nHealth: {self.HEALTH}\nDamage: {self.DAMAGE}\n"
        actual_result = self.hero.__str__()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
