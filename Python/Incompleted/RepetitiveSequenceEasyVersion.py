# Repetitive Sequence - Easy Version - 4kyu


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
