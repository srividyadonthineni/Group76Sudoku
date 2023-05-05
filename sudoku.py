from sudoku_generator import *
import pygame, sys
from constants import *

BG_COLOR = (255, 255, 245)

# checks whether the selected_num shows up once in the row of a board
def appear_in_row(board, row, selected_num):
    # arr is being assigned to each row of the board
    arr = board[row]
    iterate = 0
    i = 0
    # loop will iterate through each row
    while i < len(arr):
        # if the number that is selected already is in arr, then iterate increases by 1
        if selected_num == arr[i]:
            iterate += 1
        # if the number is already in the row, the function returns False
        if iterate > 1:
            return False
        # this increments i by 1 so the while loop can move on to the next row
        i += 1
    return True


# checks if a number is in the specified column more than once
def appear_in_column(board, column, selected_num):
    arr = []
    i = 0
    while i < len(board):
        arr.append(board[i][column])
        i += 1
    iterate = 0
    i = 0
    while i < len(arr):
        if selected_num == arr[i]:
            iterate += 1
        if iterate > 1:
            return False  # returns false because it is present more than once
        i += 1
    return True  # valid as the number only shows up once in the columnumn


# checks if a number is in the specified box (3x3 square) more than once
def appear_in_box(board, column_begin, row_begin, selected_num):
    arr = []
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            arr.append(board[row_begin + i][column_begin + j])
            j += 1
        i += 1
    iterate = 0
    i = 0
    while i < len(arr):
        if selected_num == arr[i]:
            iterate += 1
        if iterate == 2:
            return False  # returns false if the number appears more than once in the box
        i += 1
    return True  # valid as the number shows up only once in the box


# checks if a number can be put into the cell (validates rules of the sudoku board)
def checks_validity(board, row, column, selected_num):
    if appear_in_column(board, column, selected_num) and appear_in_row(board, row, selected_num) and appear_in_box(board, (row // 3) * 3, (column // 3) * 3, selected_num):
        return True
    return False


def game_start(screen):
    # sets the title of the game for game window to be Sudoku
    pygame.init()
    pygame.display.set_caption('Sudoku')
    screen.fill(BG_COLOR)

    # sets the font for the welcome screen to Helvetica and sets the font size
    display_font = pygame.font.SysFont('Helvetica', 60)
    button_font = pygame.font.SysFont('Helvetica', 30)

    # displays the welcome message using the render method and utilizing the constant LINE_COLOR
    title_display = display_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_box = title_display.get_rect(center=(WIDTH // 2 - 5, HEIGHT // 2 - 150))
    screen.blit(title_display, title_box)

    # displays the message to choose an option and creates the buttons for difficulty
    sub_font = pygame.font.SysFont('Helvetica', 45)
    game_mode_text = sub_font.render("Select Game Mode:", 0, LINE_COLOR)
    screen.blit(game_mode_text, (130, 300))
    easy_display = button_font.render("Easy", 0, (255, 255, 255))
    hard_display = button_font.render('Hard', 0, (255, 255, 255))
    medium_display = button_font.render("Medium", 0, (255, 255, 255))

    # creates new objects with the specified dimensions (rectangular area for button)
    # fills the surface with the constant LINE_COLOR and displays the text inside the button for each difficlty option
    easy_dimension = pygame.Surface((easy_display.get_size()[0] + 20, easy_display.get_size()[1] + 20))
    easy_dimension.fill(LINE_COLOR)
    easy_dimension.blit(easy_display, (10, 10))
    medium_dimension = pygame.Surface((medium_display.get_size()[0] + 20, medium_display.get_size()[1] + 20))
    hard_dimension = pygame.Surface((hard_display.get_size()[0] + 20, hard_display.get_size()[1] + 20))
    easy_box = easy_dimension.get_rect(center=(95, 500))
    medium_box = medium_dimension.get_rect(center=(295, 500))
    medium_dimension.fill(LINE_COLOR)
    medium_dimension.blit(medium_display, (10, 10))
    hard_box = hard_dimension.get_rect(center=(495, 500))
    hard_dimension.fill(LINE_COLOR)
    hard_dimension.blit(hard_display, (10, 10))

    # displays the buttons
    screen.blit(easy_dimension, easy_box)
    screen.blit(medium_dimension, medium_box)
    screen.blit(hard_dimension, hard_box)

    # creates a loop for user input(mouse clicks, game_window closing)
    while True:
        for event in pygame.event.get():  # iterates over a lost of all events that have occurred from the last time
            # user clicked the close button on the game game_window, checks which button was pressed using the position
            # of the mouse click generates a Sudoku board with the number of filled cells according to difficulty
            if event.type == pygame.QUIT:
                sys.exit()
            # when the user clicks on the easy, medium, and hard button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # produces a 9x9 board and the empty cells associated with the level of difficulty
                if easy_box.collidepoint(mouse_pos):
                    board = generate_sudoku(9, 30)
                    difficulty = 30
                    break
                elif medium_box.collidepoint(mouse_pos):
                    board = generate_sudoku(9, 40)
                    difficulty = 40
                    break
                elif hard_box.collidepoint(mouse_pos):
                    board = generate_sudoku(9, 50)
                    difficulty = 50
                    break
        # updates the display
        else:
            pygame.display.update()
            continue
        break
    # returns the board and the number of empty cells
    return board, difficulty


def draw_win_screen(screen):
    # creating font objects with the text size
    pygame.init()
    pygame.display.set_caption('Sudoku')
    screen.fill(BG_COLOR)
    display_font = pygame.font.SysFont('Helvetica', 60)
    button_font = pygame.font.SysFont('Helvetica', 30)

    # creates new objects with the specified dimensions (rectangular area for button)
    # fills the surface with the constant LINE_COLOR and displays the text inside the button for each
    quit_font = button_font.render("Exit", 0, (255, 255, 255))
    quit_dimensions = pygame.Surface((quit_font.get_size()[0] + 20, quit_font.get_size()[1] + 20))
    quit_dimensions.fill(LINE_COLOR)
    quit_dimensions.blit(quit_font, (10, 10))
    quit_box = quit_dimensions.get_rect(center=(300, HEIGHT // 2 + 100))
    screen.blit(quit_dimensions, quit_box)

    # creates abd displays a Game Won! message
    title_display = display_font.render("Game Won :)", 0, LINE_COLOR)
    title_box = title_display.get_rect(center=(300, HEIGHT / 2 - 150))
    screen.blit(title_display, title_box)
    # updates the display
    pygame.display.update()

    # user either clicks the close button of the game_window or clicks quit, determined by mouse positioning
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_box.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


def new_num(selected_num, game_window, outline, coordinate, font1, font2):
    # creates a surface objects
    blank_background = font2.render(outline[coordinate[1]][coordinate[0]], 0, (255, 255, 255))

    # copies blank_background onto the board where ever the coordinate is
    game_window.blit(blank_background, (coordinate[0] * 50 + 53, coordinate[1] * 50 + 53))

    # retrieves the sketch depending on the coordinate and renders it a different COLOR
    # adjusts the sample number
    sketch_num = outline[coordinate[1]][coordinate[0]]
    sketch_font = pygame.font.SysFont(None, 24)
    sample_dimensions = sketch_font.render(sketch_num, True, (255, 255, 255))

    blank_dimensions = pygame.Surface((sample_dimensions.get_width() + 10, sample_dimensions.get_height() + 10))
    blank_dimensions.fill(BG_COLOR)
    blank_box = blank_dimensions.get_rect(center=(coordinate[0] * 50 + 70, coordinate[1] * 50 + 70))

    game_window.blit(blank_dimensions, blank_box)
    game_window.blit(sample_dimensions, (coordinate[0] * 50 + 35, coordinate[1] * 50 + 35))

    # updates the display
    pygame.display.update()

    # chooses position of the sketched board
    selected_num_surface = font1.render(selected_num, True, (150, 150, 150))
    outline[coordinate[1]][coordinate[0]] = selected_num
    game_window.blit(selected_num_surface, (coordinate[0] * 50 + 55, coordinate[1] * 50 + 55))
    pygame.display.update()

# the function that runs the game screen
def game(board, game_window, num):
    iteration = 0
    pygame.init()

    # sets fonts for the buttons
    game_window.fill(BG_COLOR)
    num_font = pygame.font.SysFont(None, 50)
    rrq_button_font = pygame.font.SysFont('Helvetica', 30)
    font1 = pygame.font.SysFont(None, 25)
    font2 = pygame.font.SysFont(None, 25)
    pygame.display.set_caption('Sudoku')

    # creates a copy of the sudoku board to keep track of numbers
    board_copy = [row[:] for row in board]
    # sets the background COLOR
    game_window.fill(BG_COLOR)

    # creates the lines for the grid
    # the thickness for the outer lines and the lines around the 3x3 will be thicker than the rest of the lines
    i = 0
    while i < 10:
        if not i % 3 != 0:
            thickness = 5
        else:
            thickness = 2
        pygame.draw.line(game_window, (0, 0, 0), (50 * (i + 1), 50), (50 * (i + 1), 500), thickness)
        pygame.draw.line(game_window, (0, 0, 0), (50, 50 * (i + 1)), (500, 50 * (i + 1)), thickness)

        i += 1


    # sets up the exit button
    quit_font = rrq_button_font.render("Exit", 0, (255, 255, 255))
    quit_dimensions = pygame.Surface((quit_font.get_size()[0] + 20, quit_font.get_size()[1] + 20))
    quit_dimensions.fill(LINE_COLOR)
    quit_box = quit_dimensions.get_rect(center=(WIDTH // 2 + 130, 545))

    # sets up the reset button
    reset_text = rrq_button_font.render("Reset", 0, (255, 255, 255))
    reset_dimensions = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_dimensions.fill(LINE_COLOR)
    reset_rectangle = reset_dimensions.get_rect(center=(WIDTH // 2 - 15, 545))

    # sets up the restart button
    restart_display = rrq_button_font.render("Restart", 0, (255, 255, 255))
    restart_dimensions = pygame.Surface((restart_display.get_size()[0] + 20, restart_display.get_size()[1] + 20))
    restart_dimensions.fill(LINE_COLOR)
    restart_box = restart_dimensions.get_rect(center=(125, 545))

    # displays to the window
    quit_dimensions.blit(quit_font, (10, 10))
    game_window.blit(quit_dimensions, quit_box)
    reset_dimensions.blit(reset_text, (10, 10))
    game_window.blit(reset_dimensions, reset_rectangle)
    restart_dimensions.blit(restart_display, (10, 10))
    game_window.blit(restart_dimensions, restart_box)
    pygame.display.update()

    # iterates over every cell in the board and draws
    i = 0
    while i < len(board):
        j = 0
        while j < len(board):
            if 0 < board[i][j] <= 9:
                temp = num_font.render(str(board[i][j]), True, (0, 0, 0))
                game_window.blit(temp, (50 * j + 62, i * 50 + 62))
            j += 1
        i += 1

    pygame.display.update()  # updates screen
    coordinate = [0, 0]
    num_rows = 9
    num_columns = 9
    outline = [[' ' for j in range(num_columns)] for i in range(num_rows)]

    # adds the new element to the outline list
    rect_down = False
    while True:
        if iteration == num:
            for i in range(9):
                for j in range(9):
                    if not checks_validity(board_copy, i, j, board_copy[i][j]):
                        return 3
            return True

        for event in pygame.event.get():
            # checks if the user closed the game window
            if event.type == pygame.QUIT:
                pygame.quit() # exits the program
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # gets the current position of the mouse cursor
                if quit_box.collidepoint(mouse_pos):  # if the cursor is inside the quit button it exits the game
                    sys.exit()
                elif reset_rectangle.collidepoint(mouse_pos):
                    # if the cursor is inside the reset button, it resets to the original board
                    game(board, game_window, num)
                elif restart_box.collidepoint(mouse_pos):
                    # if the cursor is inside the restart button and resets the game
                    return 2
                if 50 < event.pos[0] < 500 and 50 < event.pos[1] < 500:
                    rect_down = True
                    pygame.display.update()
                    # draw the previously selected cell back to its original COLOR
                    pygame.draw.rect(game_window, (0, 0, 0), [coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)
                    # set the new selected cell coordinates and highlight it
                    coordinate = [event.pos[0] // 50 - 1, event.pos[1] // 50 - 1]
                    pygame.draw.rect(game_window, (255, 0, 0), [coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)

            # when key is pressed down
            elif event.type == pygame.KEYDOWN:
                # checks to see if the keys being pressed are 1-9
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,pygame.K_8, pygame.K_9]:
                    # retrieves the name of the key pressed
                    key_pressed = pygame.key.name(event.key)
                    # makes sure the cell is currently empty
                    if board_copy[coordinate[1]][coordinate[0]] == 0:
                        # calls the function new_num
                        new_num(key_pressed, game_window, outline, coordinate, font1, font2)

                def move_rect(direction, game_window, coordinate, rect_down):
                    if rect_down:
                        if direction == 'right':
                            if coordinate[0] < 8:
                                # draws a rectangle on the window
                                pygame.draw.rect(game_window, (0, 0, 0),[coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)

                                # moves the current position one unit to the right
                                coordinate = [coordinate[0] + 1, coordinate[1]]

                                # draws a red rectangle (for the user to know which box they are clicked on)
                                pygame.draw.rect(game_window, (255, 0, 0),[coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)
                                pygame.display.update()
                        elif direction == 'left':
                            if coordinate[0] > 0:
                                pygame.draw.rect(game_window, (0, 0, 0),[coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)
                                coordinate = [coordinate[0] - 1, coordinate[1]]
                                pygame.draw.rect(game_window, (255, 0, 0),[coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)
                                pygame.display.update()
                        elif direction == 'up':
                            if coordinate[1] > 0:
                                # draws a rectangle on the window
                                pygame.draw.rect(game_window, (0, 0, 0),[coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)
                                # moves the current position one unit to the left
                                coordinate = [coordinate[0], coordinate[1] - 1]
                                pygame.draw.rect(game_window, (255, 0, 0),[coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)
                                pygame.display.update()
                        elif direction == 'down':
                            if coordinate[1] < 8:
                                # draws a rectangle on the window
                                pygame.draw.rect(game_window, (0, 0, 0),[coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)
                                # moves the rectangle one row below
                                coordinate = [coordinate[0], coordinate[1] + 1]
                                pygame.draw.rect(game_window, (255, 0, 0),[coordinate[0] * 50 + 50, coordinate[1] * 50 + 50, 50, 50], 1)
                                pygame.display.update()
                    return coordinate

                if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                    if event.key == pygame.K_RIGHT:
                        # if the key that was pressed was the right key it moves the rectangle to the right
                        coordinate = move_rect('right', game_window, coordinate, rect_down)
                    elif event.key == pygame.K_LEFT:
                        # if the key that was pressed was the left key it moves the rectangle to the left
                        coordinate = move_rect('left', game_window, coordinate, rect_down)
                    elif event.key == pygame.K_UP:
                        # if the key that was pressed was the up key it moves the rectangle up one position
                        coordinate = move_rect('up', game_window, coordinate, rect_down)
                    elif event.key == pygame.K_DOWN:
                        # if the key that was pressed was the down key it moves the rectangle down one position
                        coordinate = move_rect('down', game_window, coordinate, rect_down)

                elif event.key == pygame.K_RETURN:
                    if outline[coordinate[1]][coordinate[0]] != '0':
                        # creates a blank background with the same size as the text
                        sample = font1.render(outline[coordinate[1]][coordinate[0]], 0, (255, 255, 255))
                        blank_background = pygame.Surface((sample.get_size()[0], sample.get_size()[1]))
                        blank_background.fill(BG_COLOR)
                        blank_box = blank_background.get_rect(center=(coordinate[0] * 50 + 60, coordinate[1] * 50 + 60))

                        # renders the texts with the given fonts and updates the board
                        x = num_font.render(outline[coordinate[1]][coordinate[0]], True, (0, 0, 0))
                        board_copy[coordinate[1]][coordinate[0]] = int(outline[coordinate[1]][coordinate[0]])
                        outline[coordinate[1]][coordinate[0]] = '0'
                        iteration += 1

                        # displays all changes to the screen
                        game_window.blit(blank_background, blank_box)
                        game_window.blit(blank_background, (coordinate[0] * 50 + 55, coordinate[1] * 50 + 55))
                        game_window.blit(x, (50 * coordinate[0] + 60, coordinate[1] * 50 + 60))
                        pygame.display.update()


def game_over_screen(screen):
    # creates display window with the given fonts and text sizes
    pygame.init()
    pygame.display.set_caption('Sudoku')
    screen.fill(BG_COLOR)
    display_font = pygame.font.SysFont('Helvetica', 60)
    button_font = pygame.font.SysFont('Helvetica', 40)

    #Renders the Game Over text with the dimensions
    title_display = display_font.render("Game Over :(", 0, LINE_COLOR)
    title_box = title_display.get_rect(center=(300, HEIGHT / 2 - 150))

    # creates a button to restart the game
    restart_display = button_font.render("Restart", 0, (255, 255, 255))
    restart_dimensions = pygame.Surface((restart_display.get_size()[0] + 20, restart_display.get_size()[1] + 20))
    restart_dimensions.fill(LINE_COLOR)
    restart_box = restart_dimensions.get_rect(center=(300, HEIGHT // 2 + 100))
    restart_dimensions.blit(restart_display, (10, 10))

    # displays everything to the game window
    screen.blit(title_display, title_box)
    screen.blit(restart_dimensions, restart_box)

    pygame.display.update()

    # checks for user input to either exit or restart the game
    continue_game = True
    while continue_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN and restart_box.collidepoint(event.pos):
                return


def main():
    # initalizes the window to be 600 by 600 pixels
    game_window = pygame.display.set_mode((600, 600))
    while True:
        board, num = game_start(game_window)
        number = game(board, game_window, num)
        if number == 0:  # win the game and the loop breaks
            break
        elif number == 2:  # game gets restarted so a new game begins
            game_start(game_window)
        elif number == 3:  # game was lost and the game over screen is displayed
            game_over_screen(game_window)
        elif number:  # player won the game and the win screen is displayed
            draw_win_screen(game_window)


if __name__ == '__main__':
    main()
