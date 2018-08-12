import pygame
import sys


def game_done(grid):
    print(grid)
    grid_size = len(grid)

    for i in range(grid_size):
        # checking rows
        if all([x == 0 for x in grid[i]]) or all([x == 1 for x in grid[i]]):
            return True
        # checking columns
        elif all([x[i] == 0 for x in grid]) or all([x[i] == 1 for x in grid]):
            return True
    # checking diagonal
    if all([grid[i][i] == 0 for i in range(grid_size)]) or all([grid[i][i] == 1 for i in range(grid_size)]):
        return True
    # checking reverse diagonal
    elif all([grid[i][-i-1] == 0 for i in range(grid_size)]) or all([grid[i][-i-1] == 0 for i in range(grid_size)]):
        return True
    return False


def main():
    pygame.init()

    grid_size = 4  # number of squares in the puzzle gz x gz
    cell_size = 100  # Each square is of size cz x cz
    window_size = (grid_size+2)*100  # main outer window wz x wz
    grid_backend = [[-1]*grid_size for _ in range(grid_size)]  # Under the hood game board

    color = [(0,0,255), (255, 0, 0)]
    black = (0, 0, 0)
    white = (255, 255, 255)

    game_window = pygame.display.set_mode((window_size, window_size), 0, 32)
    start_pos = (window_size-grid_size*cell_size)/2
    end_pos = window_size-start_pos

    for i in range(grid_size+1):
        # draw vertical grid lines
        pygame.draw.line(game_window, white, [start_pos+i*cell_size, start_pos], [start_pos+i*cell_size, end_pos], 5)

        # draw horizontal grid lines
        pygame.draw.line(game_window, white, [start_pos, start_pos+i*cell_size], [end_pos, start_pos+i*cell_size], 5)

    player = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pygame.mouse.set_visible(True)
            mouse_pressed = pygame.mouse.get_pressed()[0]
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_pressed:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print('clicked at %s, %s' % (mouse_x, mouse_y))
                if start_pos <= mouse_x <= end_pos and start_pos <= mouse_y <= end_pos:
                    print('cell %s %s' % (mouse_x//cell_size, mouse_y//cell_size))
                    if grid_backend[mouse_x//cell_size-1][mouse_y//cell_size-1] != -1:
                        print('filled cell')
                        continue
                    pygame.draw.rect(game_window, color[player], [cell_size*(mouse_x//cell_size),
                                                                  cell_size*(mouse_y//cell_size),
                                                                  cell_size, cell_size])
                    grid_backend[mouse_x//cell_size-1][mouse_y//cell_size-1] = player
                    if game_done(grid_backend):
                        print('player %s wins!' % player)
                        pygame.quit()
                        sys.exit()
                    player = (player+1) % 2

        pygame.display.update()


if __name__ == "__main__":
    main()
    print('Done')