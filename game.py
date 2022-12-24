import numpy as np

import pyautogui


class Cell: 
    def __init__(self, r, c):
        ''' Initiatlize a cell with coordinates (r, c)
        '''
        self.r, self.c = r, c
        self.value = 9 #num 0-8, covered 9, flag 10, explosion 11

class Game:
    ''' Game class hold information about the game current state,
    methods to solve the field from the current state
    '''
    def __init__(self, nrows, ncols, nmines, width, height, left, top):
        self.nrows, self.ncols = nrows, ncols
        self.nmines = nmines
        self.width, self.height = width, height
        self.left, self.top = left, top
        self.create_field()
    
    def create_field(self):
        ''' Initialize a field by adding cells to a two-dimensional array
        '''
        self.field = np.empty((self.nrows, self.ncols), dtype=object)
        for row in range(self.nrows):
            for col in range(self.ncols):
                self.field[row, col] = Cell(row, col)

    def get_neighbors(self, cell):
        ''' Return a list of neighbor cells
        '''
        r, c = cell.r, cell.c
        neighbors = []
        for row in range(r - 1, r + 2):
            for col in range(c - 1, c + 2):
                if ((row != r or col != c) and
                    (0 <= row < self.nrows) and
                    (0 <= col < self.ncols)):
                    neighbors.append(self.field[row, col])
        return np.array(neighbors)

    def get_state(self, img):
        ''' Get the current state of a cell from screenshot
        '''
        pass

    def print(self, img):
        ''' Print the field on the terminal for debugging purpose
        '''
        for row in range(self.nrows):
            for col in range(self.ncols):
                cell = self.field[row, col]
                if cell.value == 9:
                    pass
                    # TODO: your code here
                elif cell.value == 10:
                    pass
                    # TODO: your code here
                elif cell.value == 11:
                    pass
                    # TODO: your code here
                else:
                    pass
                    # TODO: your code here

    def click(self, cell, button):
        y = self.top + cell.r * self.height + 0.5 * self.height
        x = self.left + cell.c * self.width + 0.5 * self.width
        pyautogui.click(x, y, button = button)
    
    def solve(self, img):
        pass