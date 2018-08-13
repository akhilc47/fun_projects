import sys
import pygame
import time
from helper import SnakeBoard


def main():
    pygame.init()

    # Display parameters
    cell_size = 20  # Size of the smallest occupiable block
    board_size = 600  # Size of entire board NxN
    max_length = 20
    direction_dict = {pygame.K_LEFT: [-1, 0],
                      pygame.K_RIGHT: [1, 0],
                      pygame.K_DOWN: [0, 1],
                      pygame.K_UP: [0, -1]}

    # Display main window
    snake = SnakeBoard(cell_size, board_size, max_length)

    last_update = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # for movements
            elif event.type == pygame.KEYDOWN:
                # Update when key pressed
                if event.key in direction_dict:
                    snake.update_direction(direction_dict[event.key])
                else:
                    continue
                snake.update_visual()

        if time.time()-last_update > 0.5:
            last_update = time.time()
            snake.move_snake()
            snake.update_visual()


if __name__ == "__main__":
    main()
