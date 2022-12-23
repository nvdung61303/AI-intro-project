import numpy as np


class Cell: #num 0-9, 
    def __init__(self, x, y):
        ''' Initiatlize a cell with coordinates (x, y)
        '''
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y


class Field:
    def __init__(self, num_rows, num_cols, num_mines, width, height):
        self.num_rows = num_rows 
        self.num_cols = num_cols
        self.num_mines = num_mines
        self.width = width
        self.height = height
    
        ''' Initialize a field by adding cells to a two-dimensional array
        '''
        self.field = []
        for y in range(self.num_rows):
            row = []
            for x in range(self.num_cols):
                row.append(Cell(x, y))
            self.field.append(row)

    def get_neighbors(self, cell):
        ''' Return a list of neighbor cells
        '''
        x, y = cell.get_coord()
        neighbors = []
        for row in range(y - 1, y + 2):
            for col in range(x - 1, x + 1):
                if ((row != y or col != x) and
                    (0 <= row < self.num_cols) and
                    (0 <= col < self.numcols)):
                    neighbors.append(self.field[row][col])
        return neighbors

    def update_field(self):
        pass

    def mark_safe(self): # may move to solver
        pass
    
    def mark_mine(self): # may move to solver
        pass

    def get_state(self):
        pass

    def print_field(self):
        ''' Print the field on the terminal for debugging purpose
        '''
        pass

    def click_cell(self):
        pass