# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!! - 6kyu
# https://www.codewars.com/kata/5626b561280a42ecc50000d1

# Access the link for a long task description.


import math


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function

    searched_numbers = []

    for x in range(a, b + 1):
        if x < 10:
            searched_numbers.append(x)
        elif x == 89:
            searched_numbers.append(x)
        elif x == 135:
            searched_numbers.append(x)
        elif x > 135:
            x_length = int(math.log10(x)) + 1
            x_value = x
            x_sum = 0
            while x > 0:
                reminder = x % 10
                x_sum += reminder ** x_length
                x //= 10
                x_length -= 1
            if x_sum == x_value:
                searched_numbers.append(x_value)

    return searched_numbers
