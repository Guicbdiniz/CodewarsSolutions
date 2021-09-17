import unittest

from number_2_words import number2words


class Number2WordsSingleWordsTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual('zero', number2words(0))

    def test_eight(self):
        self.assertEqual('eight', number2words(8))

    def test_fourteen(self):
        self.assertEqual('fourteen', number2words(14))

    def test_nineteen(self):
        self.assertEqual('nineteen', number2words(19))


class Number2WordsTwentyToNinetyNineTestCase(unittest.TestCase):
    def test_twenty(self):
        self.assertEqual('twenty', number2words(20))

    def test_thirty_four(self):
        self.assertEqual('thirty-four', number2words(34))

    def test_fifty_nine(self):
        self.assertEqual('fifty-nine', number2words(59))

    def test_eighty(self):
        self.assertEqual('eighty', number2words(80))


class Number2WordsNinetyNineToNineHundredNinetyNineTestCase(unittest.TestCase):
    def test_one_hundred_eighty(self):
        self.assertEqual('one hundred eighty', number2words(180))

    def test_two_hundred(self):
        self.assertEqual('two hundred', number2words(200))

    def test_three_hundred_one(self):
        self.assertEqual('three hundred one', number2words(301))

    def test_four_hundred_thirty_three(self):
        self.assertEqual('four hundred thirty-three', number2words(433))


class Number2WordsBigNumberTestCase(unittest.TestCase):
    def test_708050(self):
        self.assertEqual('seven hundred eight thousand fifty', number2words(708050))


if __name__ == '__main__':
    unittest.main()
