import pyautogui
import random
import time
# a = [0,0,0,0]
# def Try(i):
# 	for j in ['covered', 'flag']:
# 		a[i] = j
# 		if i == 3:
# 			print(a)
# 		else:
# 			Try(i + 1)
# Try(0)
# print(a)
# pyautogui.displayMousePosition()
pyautogui.mouseInfo()

# mines = [1, 2, 3, 4, 5, 6, 7, 8]
# safe = []
# start = time.time()
# for button, coord_list in zip(("right", "left"), (mines, safe)):
#     if not coord_list:
#         continue
#     for coord in coord_list:
#         left, top, right, bottom = 100, 100, 200, 200
#         x = (left + right) // 2
#         y = (top + bottom) // 2
#         pyautogui.click(x, y, button = button)
# end = time.time()
# print(end - start)