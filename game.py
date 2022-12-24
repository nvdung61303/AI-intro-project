import numpy as np


class Cell: 
    def __init__(self, r, c):
        ''' Initiatlize a cell with coordinates (r, c) and a value
        '''
        self.r = r
        self.c = c
        self.value = 9 #num 0-8, covered 9, flag 10, explosion 11

    def get_coord(self):
        return self.r, self.c

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value


class Field:
    def __init__(self, num_rows, num_cols, num_mines, width, height):
        self.num_rows = num_rows 
        self.num_cols = num_cols
        self.num_mines = num_mines
        self.width = width
        self.height = height
        self.create_field()
    
    def create_field(self):
        ''' Initialize a field by adding cells to a two-dimensional array
        '''
        self.field = []
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                row.append(Cell(r, c))
            self.field.append(row)

    def get_neighbors(self, cell):
        ''' Return a list of neighbor cells
        '''
        row, col = cell.get_coord()
        neighbors = []
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if ((r != row or c != col) and
                    (0 <= r < self.num_rows) and
                    (0 <= c < self.num_cols)):
                    neighbors.append(self.field[r][c])
        return neighbors

    def get_state(self):
        pass

    def print_field(self):
        ''' Print the field on the terminal for debugging purpose
        '''
        pass

    def click_cell(self, cell):
        r, c = cell.get_coord()
        pass