from functools import lru_cache

X_RANGE = 300
Y_RANGE = 300


class PowerGrid(object):

    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.grid = []
        self.powers = {}
        self.initialize_grid()

    def calculate_point_power(self, x, y):
        # calculate the power according to the puzzle's formula
        return ((((x + 10) * y) + self.serial_number) * (x + 10)) // 100 % 10 - 5

    def initialize_grid(self):
        # lay out the grid and calculate the power for each cell - our indexing is 0 but the puzzle's indexing is 1
        self.grid = [[self.calculate_point_power(x+1, y+1) for y in range(Y_RANGE)] for x in range(X_RANGE)]

    @lru_cache(maxsize=300*300*300)  # after thinking about it, I'm not sure this helps at all...
    def calculate_square_power(self, x, y, square_size):
        # sum the grid values across the specified square
        return sum([self.grid[x+x1][y+y1] for x1 in range(square_size) for y1 in range(square_size)])

    def calculate_square_powers_for_size(self, size):
        # calculate the power for each possible square in the grid - our indexing is 0 but the puzzle's indexing is 1
        self.powers = {(x+1, y+1): self.calculate_square_power(x, y, size)
                       for x in range(X_RANGE - size + 1)
                       for y in range(Y_RANGE - size + 1)}

    def find_max_power_for_size(self, size):
        # find the square that has maximum power
        self.calculate_square_powers_for_size(size)
        return max(self.powers, key=lambda l: self.powers[l])

    def calculate_square_powers(self):
        # calculate the power for each possible square in the grid - our indexing is 0 but the puzzle's indexing is 1
        self.powers = {(x+1, y+1, size): self.calculate_square_power(x, y, size)
                       for x in range(X_RANGE)
                       for y in range(Y_RANGE)
                       for size in range(min([X_RANGE-x, Y_RANGE-y]))}

    def find_max_power(self):
        # find the square that has maximum power
        self.calculate_square_powers()
        return max(self.powers, key=lambda l: self.powers[l])


# solve the puzzle
serial_numbers = (18, 42, 5791)
for the_serial_number in serial_numbers:
    the_answer = PowerGrid(the_serial_number).find_max_power()
    print(f'{the_serial_number}: {the_answer}')
