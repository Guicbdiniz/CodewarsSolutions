# PI approximation - 6kyu
import math


def iter_pi(epsilon):
    my_pi = 0.0
    denominator = 1
    negative = False
    number_of_iter = 0

    while abs(math.pi - my_pi) > epsilon:
        my_pi += 4 * (1 / denominator) if not negative else -4 * (1 / denominator)
        number_of_iter += 1
        denominator += 2
        negative = not negative

    return [number_of_iter, float('{:.10f}'.format(my_pi))]


print(iter_pi(0.1))
