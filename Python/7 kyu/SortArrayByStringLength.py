# Sort array by string length - 7kyu
# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c

# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.


def sort_by_length(arr: list):
    return [x for x in sorted(arr, key=lambda x: len(x))]


print(sort_by_length(['as', 'qweqwer', 'a', 'qwrqoirnqiorqw', '123']))
