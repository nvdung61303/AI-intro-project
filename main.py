import sys
import time

import pyautogui
import keyboard

from game import Game


if __name__ == '__main__':
    # Get number of rows, columns
    mode = sys.argv[1]
    if mode == 'beginner':
        nrows, ncols = 9, 9
    elif mode == 'intermediate':
        nrows, ncols = 16, 16
    elif mode == 'expert':
        nrows, ncols = 16, 30
    else:
        pass
    
    # Get top left corner coordinates of the field by pressing 'enter'
    # keyboard.wait('enter')
    # left, top = pyautogui.position()
    
    # Get bottom right corner coordinates of the field by pressing 'enter'
    # keyboard.wait('enter')
    # right, bottom = pyautogui.position()

    left, top = 409, 666
    right, bottom = 889, 924
    # Calculate width and height of a cell
    width, height = (right - left) / ncols, (bottom - top) / nrows

    # Play the game
    game = Game(nrows, ncols, width, height, left, top)
    for i in range(90):
        img = pyautogui.screenshot()
        game.print(img)
        game.solve()