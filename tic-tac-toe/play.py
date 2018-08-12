import pygame
import sys
from helper import DataBoard, DisplayBoard


def main():
    pygame.init()
    
    # Backend data board parameters
    board_size = 4  # number of squares in the puzzle gz x gz
    data_board = DataBoard(board_size)  # Under the hood game board

    # Frontend display board parameters
    cell_size = 100  # Each square is of size cz x cz (pixels)
    line_width = 8
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    color = [red, blue]
    display_board = DisplayBoard(board_size, cell_size, line_width, white)
    
    player = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Waiting for mouse pressed (not released) event.
            if not event.type == pygame.MOUSEBUTTONDOWN:
                continue

            # Get the clicked cell
            row, col = pygame.mouse.get_pos()
            row, col = row//cell_size, col//cell_size
            if 1 <= row <= board_size and 1 <= col <= board_size:
                if not data_board.is_empty(row-1, col-1):
                    continue

                # Fill the valid cell
                display_board.color_cell(row, col, color[player])
                data_board.set_value(row-1, col-1, player)

                # Check if there is a winner
                if data_board.is_decided():
                    print('player %i wins!' % (player+1))
                    data_board.reset()
                    display_board.reset()
                    player = 0

                # Check for draw
                elif data_board.is_filled():
                    print('It\'s a draw')
                    data_board.reset()
                    display_board.reset()
                    player = 0

                # Continue the same game
                else:
                    player = (player+1) % 2

        pygame.display.update()


if __name__ == "__main__":
    main()
    print('Done')
