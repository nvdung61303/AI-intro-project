import sys

import pyautogui
import keyboard


if __name__ == '__main__':
    # Get number of rows and columns from input
    num_rows, num_cols = int(sys.argv[1]), int(sys.argv[2])

    # Get number of mines

    # Get top left corner coordinates of the field by pressing 'enter'
    keyboard.wait('enter')
    left, top = pyautogui.position()
    
    # Get bottom right corner coordinates of the field by pressing 'enter'
    keyboard.wait()
    right, bottom = pyautogui.position()