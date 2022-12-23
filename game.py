import numpy as np


class Cell:
    ''' A cell represents a location in a two-dimensional field, where
    coordinates are given by (x, y)
    '''

    def __init__(self, x, y):
        ''' Initiatlize a cell with coordinates (x, y)
        '''
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y


class Field:
    ''' A field is a rectangular region containing all cells, implemented 
    by a two-dimensional array
    '''

    def __init__(self, num_rows, num_cols, num_mines, width, height):
        ''' Set the field
        '''
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
        '''
        Get the neighbors list of a given cell

        cell: a Cell object
        
        Return: list of neighbor cells
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
    
    def print_field(self):
        ''' Print the field on the terminal for debugging purpose

        img: pyautogui image
        '''
        # TODO: your code here
        pass

    def click_cell(self):
        # TODO: your code here
        pass