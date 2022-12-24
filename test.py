import numpy as np
class Piece:
    def __init__(self, row, col):
        self.row = row
        self.col = col
field = np.empty((2, 3), dtype='object')
for row in range(2):
    for col in range(3):
        field[row, col] = (row, col)
print(field[1, 2])

neighbor = []
for row in range(2):
    for col in range(3):
        neighbor.append(field[row, col])
print(np.array(neighbor))