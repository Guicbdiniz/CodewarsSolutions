# Casino chips - 6kyu
# https://www.codewars.com/kata/5e0b72d2d772160011133654

# You are given three piles of casino chips: white, green and black chips:
# - the first pile contains only white chips
# - the second pile contains only green chips
# - the third pile contains only black chips

# Each day you take exactly two chips of different colors and head to the casino.
# You can choose any color, but you are not allowed to take two chips of the same color in a day.

# You will be given an array representing the number of chips of each color and your task is to
# return the maximum number of days you can pick the chips.

# Each day you need to take exactly two chips.


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
