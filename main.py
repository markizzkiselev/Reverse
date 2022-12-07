from board_class import *


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('The Life')

    screen = pygame.display.set_mode(DIMENSIONS)

    board = Board(DIMENSIONS, screen)
    board.draw_map()
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bird_pos = event.pos
                    board.turn([bird_pos[0] // CELL_SIZE, bird_pos[1] // CELL_SIZE])
                    board.draw_map()
                    pygame.display.flip()
                    pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
