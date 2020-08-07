import unittest
from Python.TheGreatestWarrior.TheGreatestWarrior import Warrior


def set_up_warrior(level) -> Warrior:
    warrior = Warrior()
    for level in range(level):
        warrior.training(['Gym training', 100, 1])
    return warrior


class NewWarriorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.warrior = Warrior()

    def test_new_warrior_rank(self):
        self.assertEqual('Pushover', self.warrior.rank)

    def test_new_warrior_level(self):
        self.assertEqual(1, self.warrior.level)

    def test_new_warrior_experience(self):
        self.assertEqual(100, self.warrior.experience)

    def test_new_warrior_achievements(self):
        self.assertEqual([], self.warrior.achievements)


class TrainingWarriorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.warrior = Warrior()

    def test_warrior_first_easy_training(self):
        self.assertEqual(
            'The warrior defeated a rat.',
            self.warrior.training(['The warrior defeated a rat.', 120, 1]),
            'The training did not returned the correct output.'
        )

        self.assertEqual(
            2,
            self.warrior.level,
            'The warrior level did not increase correctly after the first training.'
        )

        self.assertEqual(
            220,
            self.warrior.experience,
            'The warrior experience did not increase correctly after the first training.'
        )

        self.assertEqual(
            'Pushover',
            self.warrior.rank,
            'The warrior rank did not updated correctly after the first training.'
        )


class BattlingWarriorTests(unittest.TestCase):

    def test_invalid_battle(self):
        warrior = set_up_warrior(0)
        self.assertEqual('Invalid level', warrior.battle(120), '120 lv battle was accepted.')
        self.assertEqual('Invalid level', warrior.battle(-5), '-5 lv battle was accepted.')

    def test_same_level_battle(self):
        warrior = set_up_warrior(0)
        old_experience_points = warrior.experience
        self.assertEqual('A good fight', warrior.battle(1),
                         'Same level battle did not return the correct response.')
        self.assertEqual(old_experience_points + 10, warrior.experience,
                         'Same level battle did not improve experience.')

    def test_one_level_lower_battle(self):
        warrior = set_up_warrior(1)
        old_experience = warrior.experience
        self.assertEqual('A good fight', warrior.battle(1),
                         'One level lower battle did not return the correct response.')
        self.assertEqual(old_experience + 5, warrior.experience,
                         'One level lower battle did not improve correctly the warrior experience.')

    def test_two_levels_lower_battle(self):
        warrior = set_up_warrior(2)
        old_experience = warrior.experience
        self.assertEqual('Easy fight', warrior.battle(1), 'Two levels lower battle did not return the correct response')
        self.assertEqual(old_experience, warrior.experience,
                         'Two levels battle did not improve correctly the warrior experience.')

    def test_two_levels_higher_battle(self):
        warrior = Warrior()
        old_experience = warrior.experience
        self.assertEqual('An intense fight', warrior.battle(2),
                         'Two levels higher battle did not return the correct response')
        self.assertEqual(old_experience + 20 * 1 * 1, warrior.experience,
                         'Two levels higher battle did not improve correctly the warrior experience.')

    def test_defeat_battles(self):
        warrior = Warrior()
        self.assertEqual('You\'ve been defeated', warrior.battle(10),
                         'First defeat did not return the correct response')


if __name__ == '__main__':
    unittest.main()
