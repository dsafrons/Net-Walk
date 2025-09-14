import pygame
from sys import exit
from math import floor
from level_generator import Level


class Game:
    def __init__(self):
        level = Level()
        self.grid = level.grid
        self.lit_tiles = []
        for row_index, row in enumerate(self.grid):
            for val_index, val in enumerate(row):
                if val[0] == 'c':
                    self.origin_coord = (row_index, val_index)
                    break
        self.lit_tiles.append(self.origin_coord)

        self.grid_size = len(self.grid)
        self.tile_size = screen.get_width() / self.grid_size

        self.ccw_mapping = {'u': 'l', 'l': 'd', 'd': 'r', 'r': 'u'}
        self.cw_mapping = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}

    def check_click_and_rotate(self):
        global ev
        for events in ev:
            if events.type == pygame.MOUSEBUTTONDOWN and not event.type == pygame.MOUSEWHEEL:
                coord_mouse = floor(pygame.mouse.get_pos()[1] / self.tile_size), floor(pygame.mouse.get_pos()[0] / self.tile_size)
                new_cardinal = []
                clicked = False
                for cardinal in self.grid[coord_mouse[0]][coord_mouse[1]]:
                    if cardinal != 'c':
                        if pygame.mouse.get_pressed()[0]:
                            # ccw
                            new_cardinal.append(self.ccw_mapping[cardinal])
                            clicked = True
                        elif pygame.mouse.get_pressed()[2]:
                            # cw
                            new_cardinal.append(self.cw_mapping[cardinal])
                            clicked = True
                if clicked:
                    new_cardinal = ''.join(new_cardinal)
                    if self.grid[coord_mouse[0]][coord_mouse[1]][0] == 'c':
                        new_cardinal = 'c' + new_cardinal
                    self.grid[coord_mouse[0]][coord_mouse[1]] = new_cardinal

    def lit_tiles_check(self):
        self.lit_tiles = []
        self.lit_tiles.append(self.origin_coord)
        for coord in self.lit_tiles:
            if self.grid[coord[0]][coord[1]][0] == 'c':
                for cardinal in self.grid[coord[0]][coord[1]]:
                    if coord[0] != 0 and cardinal == 'u' and 'd' in self.grid[coord[0]-1][coord[1]] and (coord[0]-1, coord[1]) not in self.lit_tiles:
                        self.lit_tiles.append((coord[0]-1, coord[1]))
                    elif coord[1]+1 <= self.grid_size - 1 and cardinal == 'r' and 'l' in self.grid[coord[0]][coord[1]+1] and (coord[0], coord[1]+1) not in self.lit_tiles:
                        self.lit_tiles.append((coord[0], coord[1] + 1))
                    elif coord[0]+1 <= self.grid_size - 1 and cardinal == 'd' and 'u' in self.grid[coord[0]+1][coord[1]] and (coord[0]+1, coord[1]) not in self.lit_tiles:
                        self.lit_tiles.append((coord[0] + 1, coord[1]))
                    elif coord[1] != 0 and cardinal == 'l' and 'r' in self.grid[coord[0]][coord[1]-1] and (coord[0], coord[1]-1) not in self.lit_tiles:
                        self.lit_tiles.append((coord[0], coord[1] - 1))
            else:
                for cardinal in self.grid[coord[0]][coord[1]]:
                    if coord[0] != 0 and cardinal == 'u' and 'd' in self.grid[coord[0]-1][coord[1]] and (coord[0]-1, coord[1]) not in self.lit_tiles:
                        self.lit_tiles.append((coord[0]-1, coord[1]))
                    elif coord[1]+1 <= self.grid_size - 1 and cardinal == 'r' and 'l' in self.grid[coord[0]][coord[1]+1] and (coord[0], coord[1]+1) not in self.lit_tiles:
                        self.lit_tiles.append((coord[0], coord[1] + 1))
                    elif coord[0]+1 <= self.grid_size - 1 and cardinal == 'd' and 'u' in self.grid[coord[0]+1][coord[1]] and (coord[0]+1, coord[1]) not in self.lit_tiles:
                        self.lit_tiles.append((coord[0] + 1, coord[1]))
                    elif coord[1] != 0 and cardinal == 'l' and 'r' in self.grid[coord[0]][coord[1]-1] and (coord[0], coord[1]-1) not in self.lit_tiles:
                        self.lit_tiles.append((coord[0], coord[1] - 1))

    def rect_of_cardinal(self, cardinal, row_index, val_index):
        line_rect = None
        if cardinal == 'l':
            line_rect = pygame.Rect(self.tile_size * val_index, (row_index + .5) * self.tile_size - (self.tile_size / 24), self.tile_size / 2, self.tile_size / 14)
        elif cardinal == 'r':
            line_rect = pygame.Rect(self.tile_size * val_index + self.tile_size/2, (row_index + .5) * self.tile_size - (self.tile_size / 24), self.tile_size / 2, self.tile_size / 14)
        elif cardinal == 'u':
            line_rect = pygame.Rect((val_index + .5) * self.tile_size - (self.tile_size / 24), self.tile_size * row_index, self.tile_size / 14, self.tile_size / 2)
        elif cardinal == 'd':
            line_rect = pygame.Rect((val_index + .5) * self.tile_size - (self.tile_size / 24), self.tile_size * row_index + self.tile_size/2, self.tile_size / 14, self.tile_size / 2)
        return line_rect

    def rect_of_lit_cardinal(self, cardinal, row_index, val_index):
        line_rect = None
        if cardinal == 'l':
            line_rect = pygame.Rect(self.tile_size * val_index,
                                    (row_index + .5) * self.tile_size - (self.tile_size / 24) + (self.tile_size / 48), self.tile_size / 2,
                                    self.tile_size / 28)
        elif cardinal == 'r':
            line_rect = pygame.Rect(self.tile_size * val_index + self.tile_size / 2,
                                    (row_index + .5) * self.tile_size - (self.tile_size / 24) + (self.tile_size / 48), self.tile_size / 2,
                                    self.tile_size / 28)
        elif cardinal == 'u':
            line_rect = pygame.Rect((val_index + .5) * self.tile_size - (self.tile_size / 24) + (self.tile_size / 48),
                                    self.tile_size * row_index, self.tile_size / 28, self.tile_size / 2)
        elif cardinal == 'd':
            line_rect = pygame.Rect((val_index + .5) * self.tile_size - (self.tile_size / 24) + (self.tile_size / 48),
                                    self.tile_size * row_index + self.tile_size / 2, self.tile_size / 28,
                                    self.tile_size / 2)
        return line_rect

    def draw_rects(self):
        # draw lines
        for i in range(1, self.grid_size):
            pygame.draw.line(screen, (115, 115, 115), (i * self.tile_size, 0), (i * self.tile_size, screen.get_height()), 3)
        for i in range(1, self.grid_size):
            pygame.draw.line(screen, (115, 115, 115), (0, i * self.tile_size), (screen.get_width(), i * self.tile_size), 3)

        for row_index, row in enumerate(self.grid):
            for val_index, val in enumerate(row):
                try:
                    if val[0] != 'c':
                        if len(val) == 1:
                            # node; draw line towards direction of cardinal, draw black rect in center, draw blue rect center
                            line_rect = self.rect_of_cardinal(val, row_index, val_index)
                            pygame.draw.rect(screen, 'black', line_rect)
                            bigger_rect = pygame.Rect(val_index * self.tile_size + (.25 * self.tile_size) - 4, row_index * self.tile_size + (.25 * self.tile_size) - 4, self.tile_size/2 + 8, self.tile_size/2 + 8)
                            pygame.draw.rect(screen, 'black', bigger_rect)
                            center_rect = pygame.Rect(val_index * self.tile_size + (.25 * self.tile_size), row_index * self.tile_size + (.25 * self.tile_size), self.tile_size/2, self.tile_size/2)
                            if (row_index, val_index) in self.lit_tiles:
                                lit_rect = self.rect_of_lit_cardinal(val, row_index, val_index)
                                pygame.draw.rect(screen, (0, 255, 255), lit_rect)
                                pygame.draw.rect(screen, (0, 255, 255), center_rect)
                            else:
                                pygame.draw.rect(screen, (0, 0, 255), center_rect)
                        elif len(val) == 2:
                            # corner or straight line
                            line_rect = self.rect_of_cardinal(val[0], row_index, val_index)
                            pygame.draw.rect(screen, 'black', line_rect)
                            line_rect = self.rect_of_cardinal(val[1], row_index, val_index)
                            pygame.draw.rect(screen, 'black', line_rect)
                            center_rect = pygame.Rect((val_index + .5) * self.tile_size - (self.tile_size / 24), (row_index + .5) * self.tile_size - (self.tile_size / 24), self.tile_size / 12 - 2, self.tile_size / 12 - 2)
                            if (row_index, val_index) in self.lit_tiles:
                                pygame.draw.rect(screen, 'black', center_rect)
                                lit_rect = self.rect_of_lit_cardinal(val[0], row_index, val_index)
                                pygame.draw.rect(screen, (0, 255, 255), lit_rect)
                                lit_rect = self.rect_of_lit_cardinal(val[1], row_index, val_index)
                                pygame.draw.rect(screen, (0, 255, 255), lit_rect)
                                tiny_lit_rect = pygame.Rect(self.tile_size * val_index + self.tile_size / 2 - (self.tile_size / 56) - 1,  (row_index + .5) * self.tile_size - (self.tile_size / 24) + (self.tile_size / 56), self.tile_size / 28, self.tile_size / 28)
                                pygame.draw.rect(screen, (0, 255, 255), tiny_lit_rect)
                            else:
                                pygame.draw.rect(screen, 'black', center_rect)
                        elif len(val) == 3:
                            # T piece
                            line_rect = self.rect_of_cardinal(val[0], row_index, val_index)
                            pygame.draw.rect(screen, 'black', line_rect)
                            line_rect = self.rect_of_cardinal(val[1], row_index, val_index)
                            pygame.draw.rect(screen, 'black', line_rect)
                            line_rect = self.rect_of_cardinal(val[2], row_index, val_index)
                            pygame.draw.rect(screen, 'black', line_rect)
                            if (row_index, val_index) in self.lit_tiles:
                                lit_rect = self.rect_of_lit_cardinal(val[0], row_index, val_index)
                                pygame.draw.rect(screen, (0, 255, 255), lit_rect)
                                lit_rect = self.rect_of_lit_cardinal(val[1], row_index, val_index)
                                pygame.draw.rect(screen, (0, 255, 255), lit_rect)
                                lit_rect = self.rect_of_lit_cardinal(val[2], row_index, val_index)
                                pygame.draw.rect(screen, (0, 255, 255), lit_rect)
                    else:
                        # we have center piece
                        for card in val:
                            if card != 'c':
                                line_rect = self.rect_of_cardinal(card, row_index, val_index)
                                pygame.draw.rect(screen, 'black', line_rect)
                                lit_rect = self.rect_of_lit_cardinal(card, row_index, val_index)
                                pygame.draw.rect(screen, (0, 255, 255), lit_rect)
                        bigger_rect = pygame.Rect(val_index * self.tile_size + (.25 * self.tile_size) - 4, row_index * self.tile_size + (.25 * self.tile_size) - 4, self.tile_size / 2 + 8, self.tile_size / 2 + 8)
                        pygame.draw.rect(screen, 'black', bigger_rect)
                except IndexError:
                    pass

    def check_win(self):
        if len(self.lit_tiles) == self.grid_size * self.grid_size:
            print('win')

    def run(self):
        self.check_click_and_rotate()
        self.lit_tiles_check()
        self.draw_rects()
        self.check_win()


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption('Net Walk')
game = Game()

while True:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEWHEEL:
            game.__init__()

    screen.fill((210, 210, 210))
    game.run()

    pygame.display.update()
    clock.tick(60)
