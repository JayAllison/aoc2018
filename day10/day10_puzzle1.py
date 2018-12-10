from collections import defaultdict
import pprint
import re
from typing import List


pp = pprint.PrettyPrinter()


class Point(object):
    def __init__(self, data: List[int]):
        self.x = data[0]
        self.y = data[1]
        self.vx = data[2]
        self.vy = data[3]

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def __repr__(self):
        return f'Point([{self.x}, {self.y}, {self.vx}, {self.vy}])'


def move_stars_one_step(points: List[Point]):
    # map(lambda p: p.move(), points)  # why didn't this work???
    for p in points:
        p.move()


def get_min_and_max_x(points: List[Point]):
    minx = min(map(lambda p: p.x, points))
    maxx = max(map(lambda p: p.x, points))
    return minx, maxx


def get_min_and_max_y(points: List[Point]):
    miny = min(map(lambda p: p.y, points))
    maxy = max(map(lambda p: p.y, points))
    return miny, maxy


def count_x_alignments(points: List[Point], limit: int):
    # count how many columns have more than 'limit' stars
    column_counts = defaultdict(int)
    for point in points:
        column_counts[point.x] += 1
    return sum(1 for s in column_counts if column_counts[s] >= limit)


def count_y_alignments(points: List[Point], limit: int):
    # count how many rows have more than 'limit' stars
    column_counts = defaultdict(int)
    for point in points:
        column_counts[point.y] += 1
    return sum(1 for s in column_counts if column_counts[s] >= limit)


def print_stars(points: List[Point]):
    # eliminate all the empty space around the stars
    minx, maxx = get_min_and_max_x(the_stars)
    deltax = maxx - minx + 1
    offsetx = minx if minx < 0 else -minx
    miny, maxy = get_min_and_max_y(the_stars)
    deltay = maxy - miny + 1
    offsety = miny if miny < 0 else -miny

    # convert our list of Point objects into a 2D grid
    skymap = [['  ' for _x in range(deltax)] for _y in range(deltay)]
    for star in points:
        skymap[star.y + offsety][star.x + offsetx] = 'XX'

    print()
    print('--'*(len(skymap[0])+1))
    for row in skymap:
        print(' ' + ''.join(row))
    print('--'*(len(skymap[0])+1))
    print()


# example text: position=< 9,  1> velocity=< 0,  2>
#               position=<-6, 10> velocity=< 2, -2>
parser = re.compile(r'position=<\s*(-*\d+),\s*(-*\d+)> velocity=<\s*(-*\d+),\s*(-*\d+)>')

test = False
if test:
    filename = "day10_test_input.txt"
    x_count = 8
    x_limit = 1
    y_count = 5
    y_limit = 1
    frame_limit = 3
    loop_limit = 10
else:
    filename = "day10_input.txt"
    x_count = 8
    x_limit = 5
    y_count = 25
    y_limit = 2
    frame_limit = 3
    loop_limit = 100000

# do most of the prep in one line - why not???
the_stars = [Point([int(n) for n in g]) for g in [parser.match(line).groups() for line in open(filename).readlines()]]

loop_counter = 0
while frame_limit:
    loop_counter += 1
    if loop_counter > loop_limit:
        print()
        print("Analysis aborted! Loop counter limit reached.")
        break

    # the easy part - move each star one step, based on their velocity
    move_stars_one_step(the_stars)

    # the hard part - decide if the resulting locations spells anything! let's do poor man's OCR by looking for lines...
    if count_x_alignments(the_stars, x_count) >= x_limit and count_y_alignments(the_stars, y_count) >= y_limit:
        frame_limit -= 1
        print(f'After {loop_counter} seconds:')
        print_stars(the_stars)
