import pprint
pp = pprint.PrettyPrinter()


def manhattan_distance(coord1, coord2):
    return abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])


def find_total_position_distance(positions, coordinate):
    total_distance = 0
    for p in positions:
        total_distance += manhattan_distance(coordinate, positions[p])
    return total_distance


def count_area_under_limit(grid, size, limit):
    total = 0
    for x in range(size):
        for y in range(size):
            if grid[x][y] < limit:
                total += 1
    return total


places = {}
with open("day6_input.txt") as input_file:
    count = 1
    for pair in input_file:
        coord = pair.split(', ')
        places[count] = (int(coord[0]), int(coord[1]))
        count += 1

max_dimension = 0

for i in places:
    if places[i][0] > max_dimension:
        max_dimension = places[i][0]
    if places[i][1] > max_dimension:
        max_dimension = places[i][1]

max_dimension += 1

# if you print this out, x and y will be swapped visually, but I want to index it like grid[x][y]
the_grid = [[0 for j in range(max_dimension)] for i in range(max_dimension)]

for xx in range(max_dimension):
    for yy in range(max_dimension):
        the_grid[xx][yy] = find_total_position_distance(places, (xx, yy))

# pp.pprint(the_grid)

answer = count_area_under_limit(the_grid, max_dimension, 10000)
print(answer)
