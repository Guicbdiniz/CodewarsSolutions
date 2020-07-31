# Detect Pangram - 6kyu

import string


def is_pangram(s: str):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in s.lower():
            return False
    return True
