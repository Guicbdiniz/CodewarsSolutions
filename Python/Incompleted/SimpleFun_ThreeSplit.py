# SimpleFun #44: Three Split
# https://www.codewars.com/kata/588833be1418face580000d8

# You have a long strip of paper with integers written on it in a single line from left to right.

# You wish to cut the paper into exactly three pieces such that each piece contains at least one integer and
# the sum of the integers in each piece is the same. You cannot cut through a number, i.e. each initial number
# will unambiguously belong to one of the pieces after cutting. How many ways can you do it?

from functools import reduce


def three_split(seq):
    number_of_solutions = 0
    seq_length = len(seq)

    for x in range(0, seq_length - 2):
        for y in range(x + 1, seq_length - 1):
            first = reduce(lambda a, b: a + b, seq[0:x + 1])
            second = reduce(lambda a, b: a + b, seq[x + 1: y + 1])
            third = reduce(lambda a, b: a + b, seq[y + 1:seq_length + 1])

            if first == second == third:
                number_of_solutions += 1

    return number_of_solutions


def get_sum(seq, first, last):
    seq_sum = 0

    for x in seq[first:last + 1]:
        seq_sum += x

    return seq_sum


print(three_split((-1, 1, -1, 1, -1, 1, -1, 1)))
