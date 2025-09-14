from random import choice, randint


class Level:
    def __init__(self):
        # n*n and n is odd
        self.grid_size = 5
        self.grid = []
        for i in range(self.grid_size):
            row = [''] * self.grid_size
            self.grid.append(row)
        self.grid[int((self.grid_size-1)/2)][int((self.grid_size-1)/2)] = 'c'
        self.opposite = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}

        self.green_coords = []
        self.green_coords.append((int((self.grid_size-1)/2), int((self.grid_size-1)/2)))
        self.ccw_mapping = {'u': 'l', 'l': 'd', 'd': 'r', 'r': 'u'}
        while not self.check_filled():
            self.update_green_coords()
            self.extend()

        self.scramble()

    def scramble(self):
        for row_index, row in enumerate(self.grid):
            for val_index, val in enumerate(row):
                new_cardinal = []
                turn_amount = randint(1, 4)
                for cardinal in val:
                    if cardinal != 'c':
                        for i in range(turn_amount):
                            cardinal = self.ccw_mapping[cardinal]
                        new_cardinal.append(cardinal)
                new_cardinal = ''.join(new_cardinal)
                if 'c' in self.grid[row_index][val_index]:
                    self.grid[row_index][val_index] = 'c' + new_cardinal
                else:
                    self.grid[row_index][val_index] = new_cardinal

    def check_filled(self):
        for row in self.grid:
            for val in row:
                if val == '':
                    return False
        return True

    def update_green_coords(self):
        for row_index, row in enumerate(self.grid):
            for val_index, val in enumerate(row):
                if val != '':
                    space_to_move = False
                    if row_index != self.grid_size - 1 and self.grid[row_index + 1][val_index] == '':
                        space_to_move = True
                    if row_index != 0 and self.grid[row_index - 1][val_index] == '':
                        space_to_move = True
                    if val_index != 0 and self.grid[row_index][val_index - 1] == '':
                        space_to_move = True
                    if val_index != self.grid_size - 1 and self.grid[row_index][val_index + 1] == '':
                        space_to_move = True

                    if space_to_move and (row_index, val_index) not in self.green_coords:
                        self.green_coords.append((row_index, val_index))

                    if not space_to_move and (row_index, val_index) in self.green_coords:
                        self.green_coords.remove((row_index, val_index))

                    if val[0] == 'c':
                        if len(val) == 4:
                            if (row_index, val_index) in self.green_coords:
                                self.green_coords.remove((row_index, val_index))
                    elif len(val) == 3 and (row_index, val_index) in self.green_coords:
                        self.green_coords.remove((row_index, val_index))

    def extend(self):
        choice_coord = choice(self.green_coords)
        empty_coords = []
        # below?
        if choice_coord[0] != self.grid_size - 1 and self.grid[choice_coord[0]+1][choice_coord[1]] == '':
            empty_coords.append(((choice_coord[0]+1, choice_coord[1]), 'u'))
        # above?
        if choice_coord[0] != 0 and self.grid[choice_coord[0]-1][choice_coord[1]] == '':
            empty_coords.append(((choice_coord[0]-1, choice_coord[1]), 'd'))
        # left?
        if choice_coord[1] != 0 and self.grid[choice_coord[0]][choice_coord[1]-1] == '':
            empty_coords.append(((choice_coord[0], choice_coord[1]-1), 'r'))
        # right?
        if choice_coord[1] != self.grid_size - 1 and self.grid[choice_coord[0]][choice_coord[1]+1] == '':
            empty_coords.append(((choice_coord[0], choice_coord[1]+1), 'l'))
        try:
            extend_into = choice(empty_coords)
            self.grid[choice_coord[0]][choice_coord[1]] = self.grid[choice_coord[0]][choice_coord[1]] + self.opposite[extend_into[1]]
            self.grid[extend_into[0][0]][extend_into[0][1]] = self.grid[extend_into[0][0]][extend_into[0][1]] + extend_into[1]
        except IndexError:
            pass
