import numpy as np

import pyautogui
import termcolor

colors = np.array([
    [189, 189, 189], # 0
    [0, 0, 255], # 1
    [0, 123, 0], # 2 
    [255, 0, 0], # 3
    [0, 0, 123], # 4
    [123, 0, 0], # 5
    [0, 123, 123], #6
    [255, 255, 255], # 7 covered
    [0, 0, 0] # 8 mine
])

colors_no0 = np.array([
    [1000, 1000, 1000], # not 0
    [0, 0, 255], # 1
    [0, 123, 0], # 2 
    [255, 0, 0], # 3
    [0, 0, 123], # 4
    [123, 0, 0], # 5
    [0, 123, 123], #6
    [255, 255, 255], # 7 covered
    [0, 0, 0] # 8 mine
])

colors_dict = {
    '0' : 'grey',
    '1' : 'blue',
    '2' : 'green',
    '3' : 'red',
    '4' : 'magenta',
    '5' : 'red',
    '6' : 'cyan',
    '.' : 'white',
    '*' : 'red',
    'F' : 'white'
} 


class Cell: 
    def __init__(self, r, c):
        ''' Initiatlize a cell with coordinates (r, c)
        '''
        self.r, self.c = r, c
        self.value = 7 # 0-6, covered 7, mine 8, flag 9


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

    def get_value(self, img, cell):
        ''' Get the current state of a cell from screenshot
        Return: cell value
        '''
        y_center = self.top + cell.r * self.height + 0.5 * self.height
        x_center = self.left + cell.c * self.width + 0.5 * self.width
        is_zero_cell = True
        lowest_error = 3000000

        # Check if value of a cell is zero. If it is not a zero cell, exit loop
        for y in range(int(y_center - 0.3 * self.height), int(y_center + 0.3 * self.height)):      
            color = np.array(img.getpixel((x_center, y)))
            error = np.sum(np.square(color - colors), axis = 1, keepdims = True)
            state = np.argmin(error)
            if state != 0:
                is_zero_cell = False
                break
            value = 0
        
        # Find value of a cell when already know it is not zero
        if not is_zero_cell:
            for y in range(int(y_center - 0.3 * self.height), int(y_center + 0.3 * self.height)):      
                color = np.array(img.getpixel((x_center, y)))
                error = np.sum(np.square(color - colors_no0), axis = 1, keepdims = True)
                state = np.argmin(error)  
                if np.min(error) < lowest_error:
                    lowest_error = np.min(error)
                    value = state

        # Zero cell and covered cell has same color. Check if it is a covered cell
        if is_zero_cell:
            for x in range(int(x_center - 0.5 * self.width), int(y_center - 0.3 * self.width)): 
                color = np.array(img.getpixel((x, y_center)))
                error = np.sum(np.square(color - colors), axis = 1, keepdims = True)
                state = np.argmin(error)      
                if state == 7:
                    value = 7
                    break

        return value          

    def print(self, img):
        ''' Print the field on the terminal, modify cells (except flag)
        '''
        for row in range(self.nrows):
            for col in range(self.ncols):
                cell = self.field[row, col]
                if cell.value == 9: # flag
                    res = 'F'
                else:
                    res = self.get_value(img, cell)
                    if res == 7: # covered
                        res = '.'
                    elif res == 8: # mine
                        cell.value = 8
                        res = '*'
                    else: # 0-6
                        cell.value = res
                print(termcolor.colored(res, colors_dict[str(res)]), end = ' ')
            print()
        print()
        print()

    def get_neighbors(self, cell):
        ''' Return an array of neighbor cells
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

    def get_border(self):
        ''' Return an array of cells adjacent to covered cells
        '''
        border = []

        for row in self.field:
            for cell in row:
                for neighbor in self.get_neighbors(cell):
                    if neighbor.value == 7:
                        border.append(cell)
                        break

        return np.array(border)
    
    def get_num_covered(self, cell):
        ''' Return: int(number of covered cells around a cell)
        '''
        count = 0

        for neighbor in self.get_neighbors(cell):
            if neighbor.value == 7:
                count += 1
        
        return count

    def get_num_flag(self, cell):
        ''' Return: int(number of flag cells around a cell)
        '''
        count = 0

        for neighbor in self.get_neighbors(cell):
            if neighbor.value == 9:
                count += 1

        return count
    
    def first_move(self):
        self.click(self.field[self.nrows // 2, self.ncols // 2], 'left')

    def method_naive(self):
        ''' Basic algorithm to solve minesweeper
        '''
        safe, mines = [], []

        for cell in self.get_border():
            if self.get_num_covered(cell) == cell.value:
                for neighbor in self.get_neighbors(cell):
                    if neighbor.value == 7:    
                        mines.append(neighbor)
            if self.get_num_flag(cell) == cell.value:
                for neighbor in self.get_neighbors(cell):
                    if neighbor.value == 7:
                        safe.append(neighbor)

        return safe, mines
    
    def solve(self):
        ''' Go through all methods, then open safe cells and flag mine cells
        '''
        methods = [self.method_naive]

        for method in methods:
            safe, mines = method()
            if safe or mines:
                break
        
        for cell in safe:
            self.click(cell, 'left')
        for cell in mines:
            self.click(cell, 'right')
            cell.value = 9

    def click(self, cell, button):
        y_center = self.top + cell.r * self.height + 0.5 * self.height
        x_center = self.left + cell.c * self.width + 0.5 * self.width
        pyautogui.click(x_center, y_center, button = button)