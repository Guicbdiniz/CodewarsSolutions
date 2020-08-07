# The Greatest Warrior - 4kyu


def get_the_correct_rank_from_level(level: int) -> str:
    """ Get the warrior's rank based on his level. """

    level_length = len(str(level))
    if level_length == 2:
        level_first_digit = int(str(level)[0])
        ranks = ["-", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master"]
        rank = ranks[level_first_digit]
    elif level_length == 3:
        rank = 'Greatest'
    else:
        rank = 'Pushover'
    return rank


class Warrior(object):
    """Warrior fighter class."""

    def __init__(self):
        self._rank = 'Pushover'
        self._level = 1
        self._achievements = []
        self._experience = 100
        self._next_level_experience = 200
        self._experience_left_to_next_level = 100

    @property
    def rank(self):
        """Warrior's rank."""
        return self._rank

    @property
    def level(self):
        """Warrior's level."""
        return self._level

    @property
    def experience(self):
        """Warrior's experience."""
        return self._experience

    @property
    def achievements(self):
        """Warrior's achievements."""
        return self._achievements

    def _gain_experience(self, experience):
        """Add experience to the warrior."""

        if self._experience < 10000:
            if experience > self._experience_left_to_next_level:
                self._level_up()
                experience_gain_left = experience - self._experience_left_to_next_level
                self._experience_left_to_next_level = 100
                self._experience = self._next_level_experience
                self._next_level_experience += 100
                self._gain_experience(experience_gain_left)
            elif experience < self._experience_left_to_next_level:
                self._experience += experience
                self._experience_left_to_next_level -= experience
            else:
                self._level_up()
                self._experience_left_to_next_level = 100
                self._experience = self._next_level_experience
                self._next_level_experience += 100

    def _level_up(self):
        """Level up the warrior."""
        self._level += 1
        self._set_correct_rank()

    def _set_correct_rank(self):
        """Set the correct rank to the warrior."""

        self._rank = get_the_correct_rank_from_level(self._level)

    def training(self, training_info):
        """Submit the warrior to a new training."""

        description, experience_earned, minimum_level = training_info
        if self._level < minimum_level:
            return 'Not strong enough'
        else:
            self._gain_experience(experience_earned)
            self._achievements.append(description)
            return description

    def battle(self, battle_lv):
        """Submit the warrior to a new battle"""

        if 0 < battle_lv < 101:

            level_difference = self.level - battle_lv

            if level_difference == 0:
                self._gain_experience(10)
                return 'A good fight'
            if level_difference == 1:
                self._gain_experience(5)
                return 'A good fight'
            if level_difference < 0:
                if get_the_correct_rank_from_level(battle_lv) != self._rank and abs(level_difference) > 4:
                    return 'You\'ve been defeated'
                else:
                    self._gain_experience(20 * level_difference * level_difference)
                    return 'An intense fight'
            else:
                return 'Easy fight'

        else:
            return 'Invalid level'
