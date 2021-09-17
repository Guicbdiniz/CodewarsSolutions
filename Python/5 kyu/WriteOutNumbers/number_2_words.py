SINGLE_NUMBER_NAMES = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

DOZENS_NAMES = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}


def number2words(n: int):
    """ works for numbers between 0 and 999999 """
    number_2_word = ''
    if n < 999:
        number_2_word = get_number_smaller_than_one_thousand(n)
    else:
        number_2_word += get_number_smaller_than_one_thousand(n // 1000) + ' thousand'
        if n % 1000 != 0:
            number_2_word += ' '
            number_2_word += get_number_smaller_than_one_thousand(n % 1000)
    return number_2_word


def get_number_smaller_than_one_hundred(n: int):
    if n < 20:
        return SINGLE_NUMBER_NAMES[n]
    else:
        number_2_word = ''
        number_2_word += DOZENS_NAMES[n // 10]
        if n % 10 != 0:
            number_2_word += f'-{SINGLE_NUMBER_NAMES[n % 10]}'
        return number_2_word


def get_number_smaller_than_one_thousand(n: int):
    if n < 100:
        return get_number_smaller_than_one_hundred(n)
    else:
        number_2_word = ''
        number_2_word += SINGLE_NUMBER_NAMES[n // 100] + ' hundred'
        if n % 100 != 0:
            number_2_word += ' '
            number_2_word += get_number_smaller_than_one_hundred(n % 100)
        return number_2_word
