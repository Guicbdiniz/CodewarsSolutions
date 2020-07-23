# SimpleFun #44: Three Split
# Incomplete

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
