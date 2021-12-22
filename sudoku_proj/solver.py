from sudoku_grid import check_value, print_nicely,check_grid
import numpy as np

def sudoku_single_iteration(grid):
    for row_index in range(9):
        for column_index in range(9):
            current_value = grid[row_index, column_index]
            if current_value == 0:
                allowed_values=[]
                for value in range(1,10):
                     if check_value(grid,value,row_index,column_index) is True:
                         allowed_values.append(value)
                if len(allowed_values)==1:
                    grid[row_index,column_index]=allowed_values[0]
                else:
                    grid[row_index,column_index] = 0

    return grid

test_grid = np.array([[8,0,0,0,0,3,5,1,9],
                     [0,4,1,5,2,0,8,3,6],
                     [0,5,3,6,1,8,4,0,0],
                     [4,1,5,0,3,6,0,7,0],
                     [2,0,0,0,4,5,6,9,0],
                     [0,0,9,7,8,0,0,5,4],
                     [6,0,8,0,5,0,0,4,2],
                     [1,3,4,2,6,0,9,0,5],
                     [0,0,0,8,0,0,3,6,1]])

print_nicely(test_grid)

iteration_num = 0
while 0 in test_grid:
    iteration_num += 1
    print(f"Iteration Number: {iteration_num}")
    test_grid = sudoku_single_iteration(test_grid)
    print_nicely(test_grid)

print("finished")
print_nicely(test_grid)

check_grid(test_grid)
