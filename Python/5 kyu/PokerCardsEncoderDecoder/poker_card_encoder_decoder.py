from typing import Final, List

SUITS: Final = ['c', 'd', 'h', 's']
DECK: Final = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUIT_INITIAL_VALUE: Final = {'c': 0, 'd': 13, 'h': 26, 's': 39}


def encode(symbols: List[str]) -> List[int]:

    return sorted([SUIT_INITIAL_VALUE[symbol[1]] + DECK.index(symbol[0]) for symbol in symbols])


def decode(codes: List[int]) -> List[str]:
    return [DECK[code % 13] + SUITS[code // 13] for code in sorted(codes)]
