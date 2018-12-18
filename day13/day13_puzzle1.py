class Cart(object):

    def __init__(self, x_pos, y_pos, x_max, y_max, direction):
        self.x = x_pos
        self.y = y_pos
        self.x_max = x_max
        self.y_max = y_max
        self.direction = direction
        self.next_turn = 'L'

    def rank_position(self):
        return self.x * self.x_max + self.y

    def move(self, tracks):
        if self.direction == '^':
            self.y -= 1
        elif self.direction == 'v':
            self.y += 1
        elif self.direction == '<':
            self.x -= 1
        elif self.direction == '>':
            self.x += 1

        if tracks[self.y][self.x] == ' ':
            print("ERROR! This cart ran off the tracks!")
        elif tracks[self.y][self.x] in ('|', '-', '^', 'v', '<', '>'):
            pass
        elif tracks[self.y][self.x] == '/':
            if self.direction == '^':
                self.direction = '>'
            elif self.direction == 'v':
                self.direction = '<'
            elif self.direction == '<':
                self.direction = 'v'
            elif self.direction == '>':
                self.direction = '^'
        elif tracks[self.y][self.x] == '\\':
            if self.direction == '^':
                self.direction = '<'
            elif self.direction == 'v':
                self.direction = '>'
            elif self.direction == '<':
                self.direction = '^'
            elif self.direction == '>':
                self.direction = 'v'
        elif tracks[self.y][self.x] == '+':
            if self.direction == '^':
                if self.next_turn == 'L':
                    self.direction = '<'
                    self.next_turn = 'S'
                elif self.next_turn == 'S':
                    self.next_turn = 'R'
                elif self.next_turn == 'R':
                    self.direction = '>'
                    self.next_turn = 'L'
            elif self.direction == 'v':
                if self.next_turn == 'L':
                    self.direction = '>'
                    self.next_turn = 'S'
                elif self.next_turn == 'S':
                    self.next_turn = 'R'
                elif self.next_turn == 'R':
                    self.direction = '<'
                    self.next_turn = 'L'
            elif self.direction == '<':
                if self.next_turn == 'L':
                    self.direction = 'v'
                    self.next_turn = 'S'
                elif self.next_turn == 'S':
                    self.next_turn = 'R'
                elif self.next_turn == 'R':
                    self.direction = '^'
                    self.next_turn = 'L'
            elif self.direction == '>':
                if self.next_turn == 'L':
                    self.direction = '^'
                    self.next_turn = 'S'
                elif self.next_turn == 'S':
                    self.next_turn = 'R'
                elif self.next_turn == 'R':
                    self.direction = 'v'
                    self.next_turn = 'L'
        else:
            print(f"ERROR! I don't understand this track! {tracks[self.y][self.x]}")


def parse_track_map(filename):
    return [list(line.rstrip()) for line in open(filename).readlines()]


def identify_carts_from_map(tracks):
    carts = []
    max_y = len(tracks)
    for y in range(max_y):
        max_x = len(tracks[y])
        for x in range(max_x):
            if tracks[y][x] in ('^', 'v', '<', '>'):
                carts.append(Cart(x, y, max_x, max_y, tracks[y][x]))
    return carts


def check_carts_for_crash(carts):
    for cart1 in carts:
        for cart2 in carts:
            if cart1.x == cart2.x and cart1.y == cart2.y and cart1 != cart2:
                print(f'CRASH at {cart1.x},{cart1.y}!')
                return True
    return False


def move_carts_until_crash(tracks, carts):
    loop_counter = 1000
    while loop_counter > 0:
        loop_counter -= 1
        carts.sort(key=lambda c: c.rank_position())
        for cart in carts:
            cart.move(tracks)
            if check_carts_for_crash(carts):
                loop_counter = 0
                break


# the_filename = 'day13_test_input.txt'
the_filename = 'day13_input.txt'

the_map = parse_track_map(the_filename)
the_carts = identify_carts_from_map(the_map)
move_carts_until_crash(the_map, the_carts)
