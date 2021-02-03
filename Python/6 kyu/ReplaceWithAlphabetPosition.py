# Replace With Alphabet Position - 6kyu
# https://www.codewars.com/kata/546f922b54af40e1e90001da

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.


def alphabet_position(text: str):
    return ' '.join([str('-abcdefghijklmnopqrstuvwxyz'.find(x)) for x in text.lower() if x.isalpha()])
