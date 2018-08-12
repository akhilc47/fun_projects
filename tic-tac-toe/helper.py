import pygame


class DataBoard:

    def __init__(self, board_size):
        """
        Initiate a board filled with -1

        board: NxN list of lists. board[i][j] = k, where k <- {-1 (unchecked), 0 (player1), 1(player2)}

        :param board_size:
        """
        self.board_size = board_size
        self.board = [[-1] * board_size for _ in range(self.board_size)]  # Under the hood game board

    def set_value(self, x, y, val):
        self.board[x][y] = val
        return

    def is_empty(self, x, y):
        return self.board[x][y] == -1

    def is_winner(self):
        """
        Checks if any row has same elements.

        Checks if any column has same element.

        2xDiagonals are checked.

        :return: Bool
        """

        for i in range(self.board_size):
            # checking rows
            if all([x == 0 for x in self.board[i]]) or all([x == 1 for x in self.board[i]]):
                return True
            # checking columns
            elif all([x[i] == 0 for x in self.board]) or all([x[i] == 1 for x in self.board]):
                return True
        # checking diagonal
        if all([self.board[i][i] == 0 for i in range(self.board_size)]) or \
                all([self.board[i][i] == 1 for i in range(self.board_size)]):
            return True
        # checking reverse diagonal
        elif all([self.board[i][-i-1] == 0 for i in range(self.board_size)]) or \
                all([self.board[i][-i-1] == 1 for i in range(self.board_size)]):
            return True
        return False

    def is_draw(self):
        return not any([-1 in x for x in self.board])

    def reset(self):
        self.board = [[-1] * self.board_size for _ in range(self.board_size)]
        return


class DisplayBoard:
    def __init__(self, board_size, cell_size, line_width, line_color=(255, 255, 255)):
        self.board_size = board_size
        self.cell_size = cell_size
        self.line_width = line_width
        self.window_size = (self.board_size + 2) * cell_size  # main outer window wz x wz
        self.game_window = pygame.display.set_mode((self.window_size, self.window_size), 0, 32)
        self.start_pos = (self.window_size - self.board_size * cell_size) / 2
        self.end_pos = self.window_size - self.start_pos
        self.line_color = line_color  # white lines by default.
        self.font = pygame.font.SysFont('Comic Sans MS', 60)
        self.draw_board()

    def draw_board(self):
        for i in range(1, self.board_size):
            # draw vertical board lines
            pygame.draw.line(self.game_window, self.line_color, [self.start_pos + i * self.cell_size, self.start_pos],
                             [self.start_pos + i * self.cell_size, self.end_pos], self.line_width)

            # draw horizontal board lines
            pygame.draw.line(self.game_window, self.line_color, [self.start_pos, self.start_pos + i * self.cell_size],
                             [self.end_pos, self.start_pos + i * self.cell_size], self.line_width)
        pygame.display.update()
        return

    def color_cell(self, row, col, color):
        pygame.draw.rect(self.game_window, color,
                         [self.cell_size * row + self.line_width / 2, self.cell_size * col + self.line_width / 2,
                          self.cell_size - self.line_width, self.cell_size - self.line_width])
        pygame.display.update()
        return

    def reset(self):
        pygame.draw.rect(self.game_window, (0, 0, 0),
                         [0, 0, self.window_size, self.window_size])
        self.draw_board()
        pygame.display.update()
        return

    def add_text(self, text, x, y):
        label = self.font.render(text, 1, (255, 255, 0))
        self.game_window.blit(label, label.get_rect(center=(x*self.window_size, y*self.window_size)))
        pygame.display.update()
        return
