import math, random


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells

        # initalizing the board
        board = []
        for i in range(row_length):
            box = []
            for j in range(row_length):
                box.append(0)
            board.append(box)

        self.board = board
        self.box_length = 3

    # returns the board (list of numbers that represent the board)
    def get_board(self):
        return self.board

    # prints the board row by row (each nested list on its own line)
    def print_board(self):
        for row in range(9):
            for column in range(9):
                message = ""
                if column != 0:
                    message += " "
                message += str(self.board[row][column])
                print(message, end="")
            print("\n")

    # checks if a number is in the row by checking if it is in nested list
    # returns false if it is in the row, and true if it is not
    def valid_in_row(self, row, num):
        if num not in self.board[row]:
            return True
        return False

    # checks if the number is in the columnumn by adding the xth number of each nested list into another list
    # if the number is found in the list then it returns False, otherwise returns True
    def valid_in_column(self, column, num):
        columnumn = [self.board[i][column] for i in range(len(self.board))]
        if num not in columnumn:
            return True
        else:
            return False

    # checks if number is in a contained box, checks row and column start, checks if a number is valid in the 3x3 box
    def valid_in_box(self, row_start, column_start, num):
        square = [self.board[row_start + i][column_start + j] for i in range(3) for j in range(3)]
        if num in square:
            return False
        return True

    # checks if a number is valid to be put in the given row and columnumn
    def is_valid(self, row, column, num):
        if self.valid_in_row(row, num) is True:
            if self.valid_in_column(column, num) is True:
                row_start = math.floor(row / 3) * 3
                column_start = math.floor(column / 3) * 3

                if self.valid_in_box(row_start, column_start, num) is True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    # randomly fills each cell of the board with numbers from 1-9
    def fill_box(self, row_start, column_start):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(arr)
        iterate = 0
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][column_start + j] = arr[iterate]
                iterate += 1

    # fills the diagonal boxes using the fill_box function
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    # recursively fills the rest with the empty cells with valid numbers
    def fill_remaining(self, row, column):
        if column >= self.row_length and row < self.row_length - 1:
            row += 1
            column = 0
        if row >= self.row_length and column >= self.row_length:
            return True
        if row < self.box_length:
            if column < self.box_length:
                column = self.box_length
        elif row < self.row_length - self.box_length:
            if column == int(row // self.box_length * self.box_length):
                column += self.box_length
        else:
            if column == self.row_length - self.box_length:
                row += 1
                column = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, column, num):
                self.board[row][column] = num
                if self.fill_remaining(row, column + 1):
                    return True
                self.board[row][column] = 0
        return False

    # makes a solved sudoku using the fill diagonal and the fill remaining functions
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # removes the number of cells specified from the board
    def remove_cells(self):
        empty_cells = self.removed_cells
        indices = random.sample(range(81), empty_cells)
        for index in sorted(indices, reverse = True):
            row = index // 9
            column = index % 9
            self.board[row][column] = 0

# creates a board with the specified size and number of cells based on how many it must remove
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
