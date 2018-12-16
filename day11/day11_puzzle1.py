X_RANGE = 300
Y_RANGE = 300
SQUARE_SIZE = 3


def calculate_point_power(x, y, serial_number):
    # calculate the power according to the puzzle's formula
    return ((((x + 10) * y) + serial_number) * (x + 10)) // 100 % 10 - 5


def initialize_grid(serial_number):
    # lay out the grid and calculate the power for each cell - our indexing is 0 but the puzzle's indexing is 1
    return [[calculate_point_power(x+1, y+1, serial_number) for y in range(Y_RANGE)] for x in range(X_RANGE)]


def calculate_square_power(grid, x, y, square_size):
    # sum the grid values across the specified square
    return sum([grid[x+x1][y+y1] for x1 in range(square_size) for y1 in range(square_size)])


def calculate_square_powers(grid):
    # calculate the power for each square in the grid - our indexing is 0 but the puzzle's indexing is 1
    return {(x+1, y+1): calculate_square_power(grid, x, y, SQUARE_SIZE)
            for x in range(X_RANGE - SQUARE_SIZE + 1)
            for y in range(Y_RANGE - SQUARE_SIZE + 1)}


def find_max_power(powers):
    # find the square that has maximum power
    return max(powers, key=lambda l: powers[l])


# solve the puzzle
serial_numbers = (18, 42, 5791)
for the_serial_number in serial_numbers:
    the_grid = initialize_grid(the_serial_number)
    the_powers = calculate_square_powers(the_grid)
    the_answer = find_max_power(the_powers)
    print(f'{the_serial_number}: {the_answer} = {the_powers[the_answer]}')
