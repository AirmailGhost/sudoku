import numpy as np

class Grid:

    def __init__(self, grid_array):
        self.grid = grid

    def print_grid(self):
        return print_nicely(self.grid)

def nice_row(row):
    first_bit = str(row[0:3]).replace("0","x")
    second_bit = str(row[3:6]).replace("0","x")
    third_bit = str(row[6:9]).replace("0","x")
    print(first_bit + second_bit + third_bit)
    return
def print_dashes():
    print("---------------------")
    return

def print_nicely(grid):
    nice_row(grid[0])
    nice_row(grid[1])
    nice_row(grid[2])
    print_dashes()
    nice_row(grid[3])
    nice_row(grid[4])
    nice_row(grid[5])
    print_dashes()
    nice_row(grid[6])
    nice_row(grid[7])
    nice_row(grid[8])
    return

grid = np.array([[8,2,6,4,7,3,5,1,9],
                     [7,4,1,5,2,9,8,3,6],
                     [9,5,3,6,1,8,4,2,7],
                     [4,1,5,9,3,6,2,7,8],
                     [2,8,7,1,4,5,6,9,3],
                     [3,6,9,7,8,2,1,5,4],
                     [6,9,8,3,5,1,7,4,2],
                     [1,3,4,2,6,7,9,8,5],
                     [5,7,2,8,9,4,3,6,0]])

class_grid = Grid(grid)

class_grid.print_grid()
