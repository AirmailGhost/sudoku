import numpy as np

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

def check_value(grid, value, row, col):
    grid[row,col]=56
    col_check = value not in grid[:,col]
    row_check = value not in grid[row]
    big_row=(row//3)*3
    big_col=(col//3)*3
    grid_check=value not in grid[big_row:big_row+3,big_col:big_col+3]
    check=col_check & row_check & grid_check
    grid[row,col] = value

    return check

def check_grid(grid):
    if 0 in grid:
        print("please complete")
        return False
    for row_index in range(9):
        for column_index in range(9):
            value = grid[row_index,column_index]
            if check_value(grid, value, row_index, column_index) is False:
                print("that is incorrect")
                print(f"there is an error with the value {value} ,in row {row_index} and in collum {column_index}")
                return False
    print("well done. Thats correct!")
    return True

def value_testing():
    test_val = int(input("give value to check:"))
    test_row = int(input("in which row")) - 1
    test_col = int(input("in which colums")) - 1

    allowed = check_value(test_grid, test_val, test_row, test_col)
    print("allowed") if allowed else print("not allowed")
    return 0

def update_grid(grid):
    new_val = int(input("what value are you entering:"))
    new_row = int(input("in which row")) - 1
    new_col = int(input("in which colums")) - 1
    grid[new_row,new_col]=new_val
    return




test_grid = np.array([[8,0,0,0,0,3,5,1,9],
                     [0,4,1,5,2,0,8,3,6],
                     [0,5,3,6,1,8,4,0,0],
                     [4,1,5,0,3,6,0,7,0],
                     [2,0,0,0,4,5,6,9,0],
                     [0,0,9,7,8,0,0,5,4],
                     [6,0,8,0,5,0,0,4,2],
                     [1,3,4,2,6,0,9,0,5],
                     [0,0,0,8,0,0,3,6,1]])

test_soln = np.array([[8,2,6,4,7,3,5,1,9],
                     [7,4,1,5,2,9,8,3,6],
                     [9,5,3,6,1,8,4,2,7],
                     [4,1,5,9,3,6,2,7,8],
                     [2,8,7,1,4,5,6,9,3],
                     [3,6,9,7,8,2,1,5,4],
                     [6,9,8,3,5,1,7,4,2],
                     [1,3,4,2,6,7,9,8,5],
                     [5,7,2,8,9,4,3,6,1]])

grid = np.array([[8,2,6,4,7,3,5,1,9],
                     [7,4,1,5,2,9,8,3,6],
                     [9,5,3,6,1,8,4,2,7],
                     [4,1,5,9,3,6,2,7,8],
                     [2,8,7,1,4,5,6,9,3],
                     [3,6,9,7,8,2,1,5,4],
                     [6,9,8,3,5,1,7,4,2],
                     [1,3,4,2,6,7,9,8,5],
                     [5,7,2,8,9,4,3,6,0]])


# print_nicely(test_grid)



# while 0 in grid:
#     update_grid(grid)
#     print_nicely(grid)
#
# grid_correct = False
# while grid_correct is False:
#     finished = input("Are you finished (y/n):")
#     if finished == "y":
#         grid_correct = check_grid(grid)
#         if grid_correct is True:
#             break
#         else:
#             print("please continue")
#             update_grid(grid)
#     else:
#         print("please continue")
#         update_grid(grid)
