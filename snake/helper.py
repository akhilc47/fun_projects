import pygame
from random import randint as randi


class SnakeBoard:
    def __init__(self, cell_size, board_size, speed):
        self.cell_size = cell_size
        self.board_size = board_size
        self.length = 1
        self.disp_length = 1
        self.speed = speed
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.shift = [speed, 0]  # Right
        self.game_window = pygame.display.set_mode((board_size, board_size), 0, 32)
        self.cells = [[board_size//2, self.board_size//2], [board_size//2-self.cell_size, self.board_size//2],
                      [board_size // 2 - 2*self.cell_size, self.board_size // 2]]
        self.tail = self.cells[-1]
        pygame.draw.rect(self.game_window, self.white, [board_size//2, self.board_size//2,
                                                        self.cell_size, self.cell_size])
        self.tail = self.cells[-1]
        self.food = []
        self.food_rect = self.make_food()
        pygame.display.update()

    def change_direction(self, direction):
        self.shift = [direction[0]*self.speed, direction[1]*self.speed]

    def move_snake(self):
        self.tail = self.cells[-1]
        cell = self.cells[0]
        self.cells[0] = [(self.cells[0][0]+self.shift[0]) % self.board_size,
                         (self.cells[0][1]+self.shift[1]) % self.board_size]
        head_rect = pygame.draw.rect(self.game_window, self.white,
                                     [self.cells[0][0], self.cells[0][1], self.cell_size, self.cell_size])
        if head_rect.colliderect(self.food_rect):
            self.length += 1
            self.cells.append(self.tail)
            pygame.draw.rect(self.game_window, self.black,
                             [self.food[0], self.food[1], self.cell_size, self.cell_size])
            self.food_rect = self.make_food()
        pygame.display.update()
        for i in range(1, len(self.cells)):
            temp = self.cells[i]
            self.cells[i] = cell
            cell = temp
        if self.length == self.disp_length:
            pygame.draw.rect(self.game_window, self.black, [self.tail[0], self.tail[1], self.speed, self.speed])
            pygame.display.update()
        else:
            self.disp_length += 1

    def make_food(self):
        self.food = [randi(0, self.board_size/self.cell_size)*self.cell_size,
                     randi(0, self.board_size/self.cell_size)*self.cell_size]
        return pygame.draw.rect(self.game_window, self.red,
                                [self.food[0], self.food[1], self.cell_size, self.cell_size])

