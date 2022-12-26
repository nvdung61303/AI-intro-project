import sys

import pyautogui
import keyboard

from game import Game


if __name__ == '__main__':
    # Get number of rows, columns and mines
    nrows, ncols, nmines = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    # Get top left corner coordinates of the field by pressing 'enter'
    keyboard.wait('enter')
    left, top = pyautogui.position()
    
    # Get bottom right corner coordinates of the field by pressing 'enter'
    keyboard.wait('enter')
    right, bottom = pyautogui.position()
    
    # Calculate width and height of a cell
    width, height = (right - left) / ncols, (bottom - top) / nrows

    # Play the game
    game = Game(nrows, ncols, nmines, width, height, left, top)
    game.first_move()
    for i in range(1):
        img = pyautogui.screenshot()
        game.print(img)
        # break condition