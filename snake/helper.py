import pygame
from random import randint as randi


class SnakeBoard:
    def __init__(self, cell_size, board_size, speed):
        self.cell_size = cell_size
        self.board_size = board_size
        self.length = 1
        self.speed = speed
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.shift = [speed, 0]  # Right
        self.cells = [[board_size//2, self.board_size//2]]
        self.food = []
        self.game_window = pygame.display.set_mode((board_size, board_size), 0, 32)
        self.food_rect = self.make_food()
        pygame.draw.rect(self.game_window, self.white,
                         [board_size//2, self.board_size//2, self.cell_size, self.cell_size])
        pygame.display.update()

    def change_direction(self, direction):
        # Avoiding reverse movement before changing direction
        if [x*self.speed+y for x, y in zip(direction, self.shift)] != [0, 0]:
            self.shift = [direction[0]*self.speed, direction[1]*self.speed]

    def move_snake(self):
        tail = self.cells[-1]
        head = self.cells[0]
        self.cells[0] = [(x+y) % self.board_size for x, y in zip(self.cells[0], self.shift)]
        head_rect = pygame.draw.rect(self.game_window, self.white,
                                     [self.cells[0][0], self.cells[0][1], self.cell_size, self.cell_size])
        if head_rect.colliderect(self.food_rect):
            self.cells.append(tail)
            pygame.draw.rect(self.game_window, self.black,
                             [self.food[0], self.food[1], self.cell_size, self.cell_size])
            pygame.draw.rect(self.game_window, self.white,
                             [self.cells[0][0], self.cells[0][1], self.cell_size, self.cell_size])
            self.food_rect = self.make_food()
        pygame.display.update()
        for i in range(1, len(self.cells)):
            temp = self.cells[i]
            self.cells[i] = head
            head = temp
        # If consumed food, len(cells) would have increased, so tail won't be blacked so that it extends, till length
        # matches
        if self.length == len(self.cells):
            pygame.draw.rect(self.game_window, self.black, [tail[0], tail[1], self.speed, self.speed])
            pygame.display.update()
        else:
            self.length += 1

    def make_food(self):
        self.food = [randi(0, self.board_size), randi(0, self.board_size)]
        return pygame.draw.rect(self.game_window, self.red,
                                [self.food[0], self.food[1], self.cell_size, self.cell_size])

