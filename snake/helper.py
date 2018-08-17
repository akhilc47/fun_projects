import pygame
from random import randint as randi
white = (255, 255, 255)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


class SnakeBoard:
    def __init__(self, cell_size, board_size, speed):
        self.cell_size = cell_size
        self.board_size = board_size
        self.length = 1
        self.speed = speed
        self.shift = [speed, 0]  # Go Right
        self.cells = [[board_size//2, board_size//2]]
        self.food = []
        self.game_window = pygame.display.set_mode((board_size, board_size), 0, 32)
        self.food_rect = self.make_food()
        pygame.draw.rect(self.game_window, white, [board_size//2, board_size//2, cell_size, cell_size])
        pygame.display.update()

    def change_direction(self, direction):
        # Avoiding reverse movement before changing direction
        if [x*self.speed+y for x, y in zip(direction, self.shift)] != [0, 0]:
            self.shift = [direction[0]*self.speed, direction[1]*self.speed]

    def move_snake(self):
        tail = self.cells[-1]
        new_head = self.cells[0]
        new_head = [(x+y) % self.board_size for x, y in zip(new_head, self.shift)]
        head_rect = pygame.draw.rect(self.game_window, white,
                                     [new_head[0], new_head[1], self.cell_size, self.cell_size])
        if head_rect.colliderect(self.food_rect):
            pygame.draw.rect(self.game_window, black,
                             [self.food[0], self.food[1], self.cell_size, self.cell_size])
            pygame.draw.rect(self.game_window, white,
                             [new_head[0], new_head[1], self.cell_size, self.cell_size])
            self.food_rect = self.make_food()
            self.cells = [new_head] + self.cells
        elif new_head in self.cells:
            return len(self.cells)
        else:
            self.cells = [new_head] + self.cells[:-1]
        pygame.display.update()
        # If consumed food, len(cells) would have increased, so tail won't be blacked so that it extends, till length
        # matches
        if self.length == len(self.cells):
            pygame.draw.rect(self.game_window, black, [tail[0], tail[1], self.speed, self.speed])
            pygame.display.update()
        else:
            self.length += 1
        return 0

    def make_food(self):
        food_in_snake = True
        while food_in_snake:
            self.food = [randi(0, (self.board_size/self.cell_size)-1)*self.cell_size,
                         randi(0, (self.board_size/self.cell_size)-1)*self.cell_size]
            if self.food not in self.cells:
                food_in_snake = False
        return pygame.draw.rect(self.game_window, red, [self.food[0], self.food[1], self.cell_size, self.cell_size])

