import pygame
from g_constants import *
from sudoku_generator import *
from startmenu import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):

        # draw cell horizontal lines
        for i in range(1, CELL_ROWS):
            pygame.draw.line(screen,
                             CELL_COLOR,
                             (0, i * CELL_SIZE),
                             (HEIGHT, i * CELL_SIZE),
                             CELL_WIDTH)

        # draw cell vertical lines
        for j in range(1, CELL_COLS):
            pygame.draw.line(screen,
                             CELL_COLOR,
                             (j * CELL_SIZE, 0),
                             (j * CELL_SIZE, WIDTH),
                             CELL_WIDTH)


        #Takes every "cell" in the current board and if it is not equal to zero, it will draw it out on the sudoku board

        for i in range(9):
            for j in range(9):
                if currentboard[i][j] != 0:
                    chip = str(currentboard[i][j])
                    chip_font = pygame.font.Font(None, SKETCH_FONT)
                    chip_surface = chip_font.render(chip, 0, SKETCH_COLOR)
                    chip_rect = chip_surface.get_rect(
                        center=(CELL_SIZE * i + CELL_SIZE // 2, CELL_SIZE * j + CELL_SIZE // 2))
                    screen.blit(chip_surface, chip_rect)


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9,30)
        self.rows = 9
        self.cols = 9

    def draw(self):

        # draw horizontal lines
        screen.fill(BG_COLOR)
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (0, i * SQUARE_SIZE),
                             (WIDTH, i * SQUARE_SIZE),
                             LINE_WIDTH)
        # draw vertical lines
        for j in range(1, BOARD_COLS):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (j * SQUARE_SIZE, 0),
                             (j * SQUARE_SIZE, WIDTH),
                             LINE_WIDTH)
        Cell.draw(self)



    def select(self, row, col):

        # selects the cell only if cell_select is true
        if cell_select == True:
            pygame.draw.rect(screen, (225, 0, 0),
                             pygame.Rect(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE), 12)
        else:
            return None


    def click(self, x, y):

        if not game_over:
            row = y // CELL_SIZE
            col = x // CELL_SIZE
            return col, row
        else:
            return None


    def clear(self):

        #Checks each cell to see if it is a string. If it is not, it will will clear the cell.
        for i in range(9):
            for j in range(9):
                if currentboard[i][j] != str(currentboard[i][j]):
                    currentboard[i][j] = 0


    def sketch(self,value):

        # sets a specific cell to the event.key - 48 (which is a number 1-9) and prints it
        currentboard[board.click(x, y)[0]][board.click(x, y)[1]] = value
        board.draw()



    def is_full(self):


        # checks to see if board is full or not
        for i in range(9):
            for j in range(9):
                if currentboard[i][j] == 0:
                    return False

        return True


    def update_board(self):
      # updates the cells on the board
        self.cells = [Cell(self.board[row][col], row, col, screen)]


    def find_empty(self):
      # finds an empty spot on the board
        return currentboard[row][col] == 0

    def check_board(self):
        row = True
        col = True
        box = True

        # testing each and every box (lines 143 - 214)
        for i in range(0, 3):
            boxList = []
            for j in range(0, 3):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        for i in range(0, 3):
            boxList = []
            for j in range(6, 9):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        for i in range(0, 3):
            boxList = []
            for j in range(3, 6):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        for i in range(3, 6):
            boxList = []
            for j in range(0, 3):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        for i in range(3, 6):
            boxList = []
            for j in range(3, 6):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        for i in range(3, 6):
            boxList = []
            for j in range(6, 9):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        for i in range(6, 9):
            boxList = []
            for j in range(0, 3):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        for i in range(6, 9):
            boxList = []
            for j in range(3, 6):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        for i in range(6, 9):
            boxList = []
            for j in range(6, 9):
                if currentboard[i][j] not in boxList:
                    boxList.append(currentboard[i][j])
                else:
                    box = False

        # Testing each row

        for i in range(9):
            testListRow = []
            for j in range(9):
                if currentboard[i][j] not in testListRow:
                    testListRow.append(currentboard[i][j])
                else:
                    row = False

        # Testing each col
        for i in range(9):
            testListCol = []
            for j in range(9):
                if currentboard[j][i] not in testListCol:
                    testListCol.append(currentboard[j][i])
                else:
                    col = False

        if row and col and box == True:
            return True

        return False


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT2))
    difficulty = draw_game_start(screen)
    screen.fill(BG_COLOR)
    board = Board(WIDTH, HEIGHT, screen, difficulty=1)
    currentboard = generate_sudoku(9, difficulty)
    board.draw()
    draw_game_in_progress(screen)

    #define variables
    game_over = False
    x = -1
    y = -1
    didClick = False
    cell_select = False
    game_start = True

    #Numbers that are made by the sudoku generator will become strings

    for i in range(9):
        for j in range(9):
            if currentboard[i][j] != 0:
                currentboard[i][j] = str(currentboard[i][j])



    while game_start:

        #Tried to implement restart button, but did not work


        # difficulty = draw_game_start(screen)
        # screen.fill(BG_COLOR)
        # board = Board(WIDTH, HEIGHT, screen, difficulty=1)
        # currentboard = generate_sudoku(9, difficulty)
        # board.draw()
        # draw_game_in_progress(screen)


        while game_over == False:
            # event loop
            #Checks if player wins
            if board.is_full():
                if board.check_board():
                    draw_game_won(screen)
                else:
                    draw_game_over(screen)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    board.draw()
                    draw_game_in_progress(screen)
                    x, y = event.pos
                    row = x // 66.66
                    col = y // 66.66
                    didClick = True

                    #if that certain cell value is equal to 0, then we call the select function (which makes a red rectangle)
                    if currentboard[board.click(x, y)[0]][board.click(x, y)[1]] == 0:
                        cell_select = True
                        board.select(row, col)
                        draw_game_in_progress(screen)
                        # didClick = True

                if event.type == pygame.KEYDOWN:

                    #Clears board
                    if event.key == 99:
                        board.clear()
                        board.draw()
                        draw_game_in_progress(screen)


                    if didClick:
                        board.click(x, y)
                        cell_select = True
                        # Deletes the user input
                        if event.key == pygame.K_BACKSPACE and currentboard[board.click(x, y)[0]][board.click(x, y)[1]] != str(currentboard[board.click(x, y)[0]][board.click(x, y)[1]]):
                            board.sketch(0)
                            draw_game_in_progress(screen)

                        # sketches a certain value onto the board
                        if currentboard[board.click(x, y)[0]][board.click(x, y)[1]] == 0:
                            if 0 < event.key - 48 <= 9:
                                value = event.key - 48
                                board.sketch(value)
                                draw_game_in_progress(screen)
                            cell_select = False
                            didClick = False

                #will restart the game (take you back to start menu)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = True
                        break

            pygame.display.update()