import sys
import pygame
from helper import SnakeBoard


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Display parameters
    cell_size = 20  # Size of the smallest occupiable block
    board_size = 600  # Size of entire board NxN
    speed = 20  # Snake will move this much pixels every frame.
    font = pygame.font.SysFont('Comic Sans MS', int(board_size*0.08))
    direction_dict = {pygame.K_LEFT: [-1, 0],
                      pygame.K_RIGHT: [1, 0],
                      pygame.K_DOWN: [0, 1],
                      pygame.K_UP: [0, -1]}

    # Display main window
    snake = SnakeBoard(cell_size, board_size, speed)
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    snake = SnakeBoard(cell_size, board_size, speed)
                    game_over = False
                else:
                    continue

            # for movements
            elif event.type == pygame.KEYDOWN:
                # Update when key pressed
                if event.key in direction_dict:
                    snake.change_direction(direction_dict[event.key])

        if snake.move_snake():
            label = font.render("Game Over, Score: %s" % (len(snake.cells)-1), 1, (255, 255, 0))
            snake.game_window.blit(label, label.get_rect(center=(board_size//2, board_size//2)))
            label = font.render("Press SPACE or Close", 1, (255, 255, 0))
            snake.game_window.blit(label, label.get_rect(center=(board_size // 2, 3*board_size // 4)))
            pygame.display.update()
            game_over = True

        clock.tick(10)


if __name__ == "__main__":
    main()
