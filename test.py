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


if __name__ == '__main__':
    # rows, cols = int(sys.argv[1]), int(sys.argv[2])

    # keyboard.wait('enter')
    # left, top = pg.position()
    # keyboard.wait('enter')
    # right, bot = pg.position()

    # width = ((right - left) / cols)
    # height = ((bot - top) / rows)
    # x_center = left + 0 * width + 0.5 * width
    # y_center = top + 0 * height + 0.5 * height
    img = pg.screenshot()
    
    rgb = np.asarray(img.getpixel(pg.position()))
    err = np.sum(np.square(rgb - colors), axis = 1, keepdims = True)
    res = np.argmin(err)
    print(rgb)
    # print(err)
    print(res)