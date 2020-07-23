# Sort the odd - 6kyu


def sort_array(source_array: list):
    sorted_odds = sorted([x for x in source_array if x % 2 == 1], reverse=True)

    final_array = []
    for number in source_array:
        if number % 2 == 1:
            final_array.append(sorted_odds.pop())
        else:
            final_array.append(number)

    return final_array


print(sort_array([5, 2, 3, 8, 1, 4]))
