import pygame
import sys
import time
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
    score = [0, 0]
    display_board.add_text(('p1 = %i | p2 = %i' % (score[0], score[1])), 0.5, 1-(1/((board_size+2)*2)))
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
                print(row, col, player)
                display_board.color_cell(row, col, color[player])
                data_board.set_value(row-1, col-1, player)

                # Check if there is a winner
                if data_board.is_winner():
                    score[player] += 1
                    print('player %i wins!' % (player+1))
                    display_board.add_text(('player %i wins!' % (player+1)), 0.5, 1/((board_size+2)*2))
                    time.sleep(3)
                    data_board.reset()
                    display_board.reset()
                    display_board.add_text(('p1 = %i | p2 = %i' % (score[0], score[1])), 0.5,
                                           1 - (1 / ((board_size + 2) * 2)))
                    player = 0

                # Check for draw
                if data_board.is_draw():
                    print('It\'s a draw')
                    display_board.add_text('It\'s a draw', 0.5, 1/((board_size+2)*2))
                    time.sleep(3)
                    data_board.reset()
                    display_board.reset()
                    player = 0

                # Continue the same game
                else:
                    player = (player+1) % 2


if __name__ == "__main__":
    main()
    print('Done')
