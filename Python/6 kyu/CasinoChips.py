# Casino chips - 6kyu


def solve_old(arr: list):
    number_of_plays = 0

    while max(arr) != sum(arr):
        sorted_list = sorted(enumerate(arr), key=lambda x: x[1])
        max_index = sorted_list[2][0]
        second_max_index = sorted_list[1][0]
        arr[max_index] -= 1
        arr[second_max_index] -= 1
        number_of_plays += 1

    return number_of_plays


# se a soma dos menores >= maior -> soma / 2
# se a soma dos menors < maior -> menor + 2 menor


def solve(arr: list):
    a, b, c = sorted(arr)
    if a + b >= c:
        return sum(arr) // 2
    else:
        return a + b


print(solve([8, 2, 8]))
