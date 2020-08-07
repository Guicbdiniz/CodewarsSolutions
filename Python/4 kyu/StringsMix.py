# Strings Mix - 4kyu

import re


def mix(s1: str, s2: str):
    s1_letters = re.sub(r'[^a-z]*', '', s1)
    s2_letters = re.sub(r'[^a-z]*', '', s2)
    s1_set = set(s1_letters)
    s2_set = set(s2_letters)
    final_array = []

    for letter in s1_set.union(s2_set):
        s1_counter = s1_letters.count(letter)
        s2_counter = s2_letters.count(letter)

        if s2_counter > 1 or s1_counter > 1:

            if s1_counter == s2_counter:
                current_str = f'=:{letter * s1_counter}'
            elif s1_counter > s2_counter:
                current_str = f'1:{letter * s1_counter}'
            else:
                current_str = f'2:{letter * s2_counter}'

            index = 0
            while index < len(final_array):
                current_length = len(final_array[index])
                if current_length < len(current_str):
                    break
                elif current_length > len(current_str):
                    index += 1
                else:
                    if '12='.find(final_array[index][0]) < '12='.find(current_str[0]):
                        index += 1
                    elif '12='.find(final_array[index][0]) > '12='.find(current_str[0]):
                        break
                    else:
                        if final_array[index][2] > current_str[2]:
                            break
                        else:
                            index += 1

            final_array.insert(index, current_str)

    return '/'.join(final_array)
