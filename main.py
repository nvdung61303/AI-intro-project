import sys

import pyautogui
import keyboard


if __name__ == '__main__':
    # Get number of rows, columns and mines
    num_rows = int(sys.argv[1])
    num_cols = int(sys.argv[2])
    num_mines = int(sys.argv[3])

    # Get top left corner coordinates of the field by pressing 'enter'
    keyboard.wait('enter')
    left, top = pyautogui.position()
    
    # Get bottom right corner coordinates of the field by pressing 'enter'
    keyboard.wait()
    right, bottom = pyautogui.position()

    # Calculate width and height of a cell
    width = (right - left) / num_cols
    height = (bottom - top) / num_rows