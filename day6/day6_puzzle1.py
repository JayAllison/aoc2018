# idea:
# - read in all 50 positions, need to give each one an identity
# - find biggest x and biggest y
# - for each position in the array, calculate Manhattan distance to each position
# - if it's not a tie, record the closest position
# - count the position winners (but how to exclude infinite ones?)

import pprint
pp = pprint.PrettyPrinter()


def manhattan_distance(coord1, coord2):
    return abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])


def find_closest_position(positions, coordinate):
    closest_distance = 1000*1000
    closest_place = None
    for p in positions:
        distance = manhattan_distance(coordinate, positions[p])
        if distance < closest_distance:
            closest_distance = distance
            closest_place = p
    for p in positions:
        distance = manhattan_distance(coordinate, positions[p])
        if distance == closest_distance and p != closest_place:
            return None
    return closest_place


def find_largest_area(positions, grid, size):
    counts = {p: 0 for p in positions}

    # first, count how many locations in the grid are closest to each position
    for x in range(size):
        for y in range(size):
            if grid[x][y]:
                counts[grid[x][y]] += 1

    # next, zero out positions that appear on the edges - assume that these are infinite
    for x in range(size):
        counts[grid[x][0]] = 0
        counts[grid[x][size-1]] = 0
    for y in range(size):
        counts[grid[0][y]] = 0
        counts[grid[size-1][y]] = 0

    # finally, figure out what the highest count is
    max_count = 0
    for p in counts:
        if counts[p] > max_count:
            max_count = counts[p]

    return max_count


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
        the_grid[xx][yy] = find_closest_position(places, (xx, yy))

answer = find_largest_area(places, the_grid, max_dimension)
print(answer)
