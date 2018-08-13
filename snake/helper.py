import pygame


class SnakeBoard:
    def __init__(self, cell_size, board_size, max_length):
        self.cell_size = cell_size
        self.grid_size = board_size/cell_size
        self.length = 1
        self.max_length = max_length
        self.cell_color = (255, 255, 255)  # white
        self.direction = [1, 0]  # Right
        self.cells = [[self.grid_size//2, self.grid_size//2]]  # Only one cell at center of the board
        self.last_cell = self.cells[0]
        self.game_window = pygame.display.set_mode((board_size, board_size), 0, 32)
        self.update_visual()

    def update_direction(self, direction):
        self.direction = direction
        print(direction, self.direction)
        return

    def update_visual(self):
        cell = self.last_cell
        pygame.draw.rect(self.game_window, (0, 0, 0),
                         [cell[0]*self.cell_size, cell[1]*self.cell_size, self.cell_size, self.cell_size])
        for cell in self.cells:
            pygame.draw.rect(self.game_window, self.cell_color,
                             [cell[0]*self.cell_size, cell[1]*self.cell_size, self.cell_size, self.cell_size])
            pygame.display.update()

    def move_snake(self):
        self.last_cell = self.cells[-1]
        self.cells = [[cell[0]+self.direction[0], cell[1]+self.direction[1]] for cell in self.cells]
        print(self.cells)
