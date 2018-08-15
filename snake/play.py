import sys
import pygame
from helper import SnakeBoard


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Display parameters
    cell_size = 20  # Size of the smallest occupiable block
    board_size = 500  # Size of entire board NxN
    speed = 20  # Snake will move this much pixels every frame.
    direction_dict = {pygame.K_LEFT: [-1, 0],
                      pygame.K_RIGHT: [1, 0],
                      pygame.K_DOWN: [0, 1],
                      pygame.K_UP: [0, -1]}

    # Display main window
    snake = SnakeBoard(cell_size, board_size, speed)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # for movements
            elif event.type == pygame.KEYDOWN:
                # Update when key pressed
                if event.key in direction_dict:
                    snake.change_direction(direction_dict[event.key])

        snake.move_snake()
        clock.tick(10)


if __name__ == "__main__":
    main()
