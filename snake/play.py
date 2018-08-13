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
                if event.key == pygame.K_LEFT:
                    key_pressed = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    key_pressed = 'RIGHT'
                elif event.key == pygame.K_DOWN:
                    key_pressed = 'DOWN'
                elif event.key == pygame.K_UP:
                    key_pressed = 'UP'
                else:
                    continue
                snake.update_direction(key_pressed)
                snake.update_visual()

        if time.time()-last_update > 0.5:
            last_update = time.time()
            snake.move_snake()
            snake.update_visual()


if __name__ == "__main__":
    main()
