# Sort array by string length - 7kyu


def sort_by_length(arr: list):
    return [x for x in sorted(arr, key=lambda x: len(x))]


print(sort_by_length(['as', 'qweqwer', 'a', 'qwrqoirnqiorqw', '123']))
