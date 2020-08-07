# Resistor Color Codes, Part 2 - 5kyu

import re


def get_resistor_color_from_digit(digit):
    return [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'gray',
        'white'
    ][digit]


def encode_resistor_colors(ohms_string):
    ohms_numeral_value = float(re.search(r'^[\d.]+', ohms_string).group(0))
    if 'k' in ohms_string:
        ohms_numeral_value *= 1000
    elif 'M' in ohms_string:
        ohms_numeral_value *= 1000000

    first_digit_color = get_resistor_color_from_digit(
        int(
            str(ohms_numeral_value)[0]
        )
    )

    second_digit_color = get_resistor_color_from_digit(
        int(
            str(ohms_numeral_value)[1]
        )
    )

    power_of_ten_color = get_resistor_color_from_digit(
        len(
            str(ohms_numeral_value)
        ) - 4
    )

    return f'{first_digit_color} {second_digit_color} {power_of_ten_color} gold'
