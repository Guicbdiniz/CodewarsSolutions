# String incrementer - 5kyu
import math


def find_index_of_first_digit(string: str):
    for index, value in enumerate(string):
        if value.isdigit():
            rest_is_digit = True
            for x in string[index:]:
                if not x.isdigit():
                    rest_is_digit = False
            if rest_is_digit:
                return index
    return -1


def increment_number_string(string: str):
    int_value = int(string)

    if int_value == 0:
        return ''.join(['0' for x in range(len(string) - 1)]) + '1'
    else:
        int_length = int(math.log10(int_value)) + 1
        number_of_zeroes = len(string) - int_length
        int_value += 1
        new_int_length = int(math.log10(int_value)) + 1
        number_of_zeroes -= new_int_length - int_length
        return ''.join(['0' for x in range(number_of_zeroes)]) + str(int_value)


def increment_string(string: str):
    digit_index = find_index_of_first_digit(string)

    if digit_index == -1:
        return string + '1'
    else:
        return string[:digit_index] + increment_number_string(string[digit_index:])


print(math.log10(0))
