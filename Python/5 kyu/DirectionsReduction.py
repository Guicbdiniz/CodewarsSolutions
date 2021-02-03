# Directions Reduction - 5kyu
# https://www.codewars.com/kata/550f22f4d758534c1100025a

# Access the link for a long task description.

opposite_directions = {
    'SOUTH': 'NORTH',
    'NORTH': 'SOUTH',
    'EAST': 'WEST',
    'WEST': 'EAST'
}


def directions_reducer(directions):
    directions = directions.copy()

    directions_has_change = True
    while directions_has_change and len(directions) > 1:
        directions_has_change = False
        for index, direction in enumerate(directions):
            if index < len(directions) - 1:
                if directions[index + 1] == opposite_directions[direction]:
                    del directions[index: index + 2]
                    directions_has_change = True

    return directions
