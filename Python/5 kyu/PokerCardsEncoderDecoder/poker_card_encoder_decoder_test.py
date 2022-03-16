import unittest
from poker_card_encoder_decoder import decode, encode


class TestPokerCardEncoder(unittest.TestCase):
    def test_encoder_for_simple_array(self):
        self.assertEqual(encode(['Ac', 'Ks', '5h', 'Td', '3c']), [
                         0, 2, 22, 30, 51])


class TestPokerCardDecoder(unittest.TestCase):
    def test_decoder_for_simple_array(self):
        self.assertEqual(decode([0, 51, 30, 22, 2]), [
                         'Ac', '3c', 'Td', '5h', 'Ks'])


if __name__ == '__main__':
    unittest.main()
