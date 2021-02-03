# Repetitive Sequence - Easy Version - 4kyu
# https://www.codewars.com/kata/5f134651bc9687000f8022c4

# Let's write a sequence starting with seq = [0, 1, 2, 2] in which 0 and 1 occurs 1 time, 2 occurs 2 time and
# sequence advances with adding next natural number seq[natural number] times so now, 3 appears 2 times and so on.


def find(n):
    seq = [0, 1, 2, 2]
    if n < 4:
        return seq[n]
    current = 3
    current_sum = 5
    next_sum = 11
    while next_sum < n:
        seq.extend([current] * seq[current])
        current_sum = next_sum
        current += 1
        next_sum = current_sum + current * seq[current]
    remaining = (n - current_sum)
    return len(seq) - 1 + (remaining // current + (remaining % current > 0))


find(18)
