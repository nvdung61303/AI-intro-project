import pyautogui
import keyboard

from game import Game


def main():
    # Get number of rows, columns and mines
    while True:
        mode = input('Choose mode(beginner, intermediate, expert): ').lower()
        if mode == 'beginner':
            nrows, ncols, nmines = 9, 9, 10
            break
        elif mode == 'intermediate':
            nrows, ncols, nmines = 16, 16, 40
            break
        elif mode == 'expert':
            nrows, ncols, nmines = 16, 30, 99
            break
        else:
            pass

    # Get top left corner coordinates of the field by pressing 'enter'
    keyboard.wait('enter')
    left, top = pyautogui.position()
    
    # Get bottom right corner coordinates of the field by pressing 'enter'
    keyboard.wait()
    right, bottom = pyautogui.position()

    # Calculate width and height of a cell
    width = (right - left) / ncols
    height = (bottom - top) / nrows

    # Play the game
    game = Game(nrows, ncols, nmines, width, height, left, top)
    while True:
        img = pyautogui.screenshot()
        game.print(img)
        game.solve(img)
        # break condition

if __name__ == '__main__':
    main()