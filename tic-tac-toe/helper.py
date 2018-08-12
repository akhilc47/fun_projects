import pygame


class DataBoard:
    def __init__(self, grid_size):
        """
        Initiate a grid filled with -1

        grid: NxN list of lists. grid[i][j] = k, where k <- {-1 (unchecked), 0 (player1), 1(player2)}

        :param grid_size:
        """
        self.grid_size = grid_size
        self.grid = [[-1] * grid_size for _ in range(self.grid_size)]  # Under the hood game board

    def set_value(self, x, y, val):
        self.grid[x][y] = val
        return

    def is_empty(self, x, y):
        return self.grid[x][y] == -1

    def is_decided(self):
        """
        Checks if any row has same elements.

        Checks if any column has same element.

        2xDiagonals are checked.

        :return: Bool
        """

        for i in range(self.grid_size):
            # checking rows
            if all([x == 0 for x in self.grid[i]]) or all([x == 1 for x in self.grid[i]]):
                return True
            # checking columns
            elif all([x[i] == 0 for x in self.grid]) or all([x[i] == 1 for x in self.grid]):
                return True
        # checking diagonal
        if all([self.grid[i][i] == 0 for i in range(self.grid_size)]) or \
                all([self.grid[i][i] == 1 for i in range(self.grid_size)]):
            return True
        # checking reverse diagonal
        elif all([self.grid[i][-i-1] == 0 for i in range(self.grid_size)]) or \
                all([self.grid[i][-i-1] == 1 for i in range(self.grid_size)]):
            return True
        return False

    def is_filled(self):
        return not any([-1 in x for x in self.grid])

    def reset(self):
        self.grid = [[-1] * self.grid_size for _ in range(self.grid_size)]
        return


class DisplayBoard:
    def __init__(self, grid_size, cell_size, line_width, line_color=(255, 255, 255)):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.line_width = line_width
        self.window_size = (self.grid_size + 2) * cell_size  # main outer window wz x wz
        self.game_window = pygame.display.set_mode((self.window_size, self.window_size), 0, 32)
        self.start_pos = (self.window_size - self.grid_size * cell_size) / 2
        self.end_pos = self.window_size - self.start_pos
        self.line_color = line_color  # white lines by default.
        self.draw_grid()

    def draw_grid(self):
        for i in range(1, self.grid_size):
            # draw vertical grid lines
            pygame.draw.line(self.game_window, self.line_color, [self.start_pos + i * self.cell_size, self.start_pos],
                             [self.start_pos + i * self.cell_size, self.end_pos], self.line_width)

            # draw horizontal grid lines
            pygame.draw.line(self.game_window, self.line_color, [self.start_pos, self.start_pos + i * self.cell_size],
                             [self.end_pos, self.start_pos + i * self.cell_size], self.line_width)
        return

    def color_cell(self, row, col, color):
        pygame.draw.rect(self.game_window, color,
                         [self.cell_size * row + self.line_width / 2, self.cell_size * col + self.line_width / 2,
                          self.cell_size - self.line_width, self.cell_size - self.line_width])
        return

    def reset(self):
        pygame.draw.rect(self.game_window, (0, 0, 0),
                         [self.start_pos, self.start_pos, self.cell_size*self.grid_size, self.cell_size*self.grid_size])
        self.draw_grid()
        return
