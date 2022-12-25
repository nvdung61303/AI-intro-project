import numpy as np
import pyautogui as pg
import keyboard
import keyboard
import sys
import math

colors = np.asarray([
            [1000, 10000, 1000], # 0
            [0, 0, 255], # 1
            [70, 147, 70], # 2 note: 0 123 0
            [255, 0, 0], # 3
            [0, 0, 123], # 4
            [123, 0, 0], # 5
            [0, 125, 125], #6
            [0, 0, 0], # 7
            [125, 125, 125], # 8
            [255, 255, 255] # white, for the left region of unclicked piece
        ])


# if __name__ == '__main__':
#     img = pg.screenshot()
#     rgb = np.asarray(img.getpixel(pg.position()))
#     err = np.sum(np.square(rgb - colors), axis = 1, keepdims = True)
#     res = np.argmin(err)
#     print(rgb)
#     # print(err)
#     print(res)

# class Game:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.create_field()

#     def create_field(self):
#         self.field = [1, 2, 3, 4, 5]
    
#     def print_field(self):
#         for num in self.field:
#             num = 1
#         print(self.field)

# game = Game(1, 2)
# game.print_field()

# for cell in cell_list:
#     self.click(cell, 'right')
#     cell.value = 9
# for cell in cell_list:
#     self.click(cell, 'left')