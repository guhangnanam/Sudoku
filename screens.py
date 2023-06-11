from sudoku_generator import *
from Final import *
import pygame, sys
from g_constants import *


# this function was adapted and modified using Logan Chenicek's tutorial on YouTube
def draw_game_start(screen):
    easy = 30
    medium = 40
    hard = 50
    # initialize title font
    start_title_font = pygame.font.Font(None, 80)
    sub_title_font = pygame.font.Font(None, 60)
    button_font = pygame.font.Font(None, 50)

    # color background
    screen.fill(BG_COLOR)

    # initialize title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2,
                                                     HEIGHT // 2 - 150))
    # draw title
    screen.blit(title_surface, title_rectangle)

    # initialize select game mode subtitle
    sub_title_surface = sub_title_font.render("Select Game Mode", 0,
                                              LINE_COLOR)
    sub_title_rectangle = sub_title_surface.get_rect(center=(WIDTH // 2,
                                                             HEIGHT // 2 - 65))
    # draw subtitle
    screen.blit(sub_title_surface, sub_title_rectangle)

    # initialize buttons
    # initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # initialize button bkg color and text for easy, medium, and hard buttons
    easy_surface = pygame.Surface(
        (easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface(
        (medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface(
        (hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 6,
                                                   HEIGHT // 2 + 50))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2,
                                                       HEIGHT // 2 + 50))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 1.2,
                                                   HEIGHT // 2 + 50))

    # draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(
                        event.pos):  # checks if mouse is on the easy button
                    return easy
                if medium_rectangle.collidepoint(event.pos):
                    return medium
                if hard_rectangle.collidepoint(event.pos):
                    return hard
                elif hard_rectangle.collidepoint(event.pos):
                    return
        pygame.display.update()


def draw_game_in_progress(screen):
    # initialize button font
    button_font = pygame.font.Font(None, 50)

    # initialize button text
    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # initialize button bkg color and text for reset, restart, exit
    reset_surface = pygame.Surface(
        (reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface(
        (restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface(
        (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    # initialize button rectangle
    reset_rectangle = reset_surface.get_rect(center=((100,
                                                     650)))
    restart_rectangle = restart_surface.get_rect(center=(300,
                                                         650))
    exit_rectangle = exit_surface.get_rect(center=(500,
                                                   650))

    # draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_rectangle.collidepoint(event.pos):  # checks if mouse is on the easy button
                return True
            if restart_rectangle.collidepoint(event.pos):
                return False
            if exit_rectangle.collidepoint(event.pos):
                return pygame.quit()

    pygame.display.update()


def draw_game_won(screen):
    # color background
    screen.fill(BG_COLOR)

    # initialize game won title font and exit font
    gamewon_font = pygame.font.Font(None, 80)

    # initialize game won title
    gamewon_surface = gamewon_font.render("Game Won!", 0, LINE_COLOR)
    gamewon_rectangle = gamewon_surface.get_rect(center=(WIDTH // 2,
                                                         HEIGHT // 2 - 150))
    # draw game won title
    screen.blit(gamewon_surface, gamewon_rectangle)

    # initialize button font
    button_font = pygame.font.Font(None, 50)
    exit_text = button_font.render("Exit", 0, (255, 255, 255))
    exit_surface = pygame.Surface(
        (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2,
                                                   HEIGHT // 2 + 10))
    screen.blit(exit_surface, exit_rectangle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rectangle.collidepoint(event.pos):  # checks if mouse is on the exit button
                pygame.quit()
    pygame.display.update()






def draw_game_over(screen):
    # color background
    screen.fill(BG_COLOR)

    # initialize game won title font
    gameover_font = pygame.font.Font(None, 80)

    # initialize game over title
    gameover_surface = gameover_font.render("Game Over :(", 0, LINE_COLOR)
    gameover_rectangle = gameover_surface.get_rect(center=(WIDTH // 2,
                                                          HEIGHT // 2 - 150))

    # draw game over title
    screen.blit(gameover_surface, gameover_rectangle)

    # exit button
    button_font = pygame.font.Font(None, 50)
    exit_text = button_font.render("Exit", 0, (255, 255, 255))
    exit_surface = pygame.Surface(
        (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2,
                                                   HEIGHT // 2 + 10))
    screen.blit(exit_surface, exit_rectangle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rectangle.collidepoint(event.pos):  # checks if mouse is on the exit button
                pygame.quit()
    pygame.display.update()



if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    draw_game_start(screen)  # calls function to draw start screen
    screen.fill(BG_COLOR)

    game_over = False
    hard = 3
    medium = 2
    easy = 1

    board = Board(WIDTH, HEIGHT, screen, difficulty=1)
    # board.print_board()
    board.draw()

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                print(row, col)
                cell = Cell(3, row, col, screen)
                cell.draw()

        pygame.display.update()