# this file contains the code for a basic minesweeper game.
from pickletools import read_int4

# import necessary libs.
import numpy as np
import random

# Generates a basic minesweeper field with size of width * height.
# To benefit the calculations, the program will actually return a
# width+2 * height+2 matrix, with the outer layer of the matrix being unused.
# The default value of both width and height is 10.
def generate_field(height = 10, width = 10):
    '''
    expected width type: int
    expected height type: int
    return type: numpy.ndarray
    '''
    return np.zeros((height + 2, width + 2))

# Add mine_number mines into the field "field" at random positions.
def place_mine(field, mine_number):
    # generate two matrices, row and column, to help the program to choose
    # random positions.
    shape = np.shape(field)
    # since the outer layer of the matrix is unused, we need to make consider it

    row_matrix = []
    for i in range(shape[0] - 2):
        row_matrix.append(i)
    column_matrix = []
    for i in range(shape[0] - 2):
        column_matrix.append(row_matrix[:])
    # store all the coordinates of the mines in a separate variable
    mine_coordinates = []

    for i in range(mine_number):
        # choose one element from row_matrix.
        row = np.random.choice(row_matrix, 1)[0]
        # choose one element from column_matrix[row]
        column = np.random.choice(column_matrix[row], 1)[0]
        # delete that element from the column matrix
        column_matrix[row].remove(column)
        # check if that row is empty. delete the respecting row in the row_matrix
        # if the row is already empty.
        if len(column_matrix) == 0:
            row_matrix.remove(row)
        # place a mine at position (row, column) in the field.
        # map the row and column into the correct position

        field[row + 1][column + 1] = 1
        mine_coordinates.append([row + 1, column + 1])

    return (field, mine_coordinates)

# Return the amount of mines surrounding a specific position in the field.
# Assuming that the coordinate is within the correct range.
def mine_number(field, row, column):
    # set a counting variable
    mine_count = 0
    # check if the coordinate is on the edge of the field
    upmost = False
    downmost = False
    leftmost = False
    rightmost = False
    if row > 0:
        upmost = False
    if row < np.shape(field)[0]:
        downmost = False
    if column > 0:
        leftmost = False
    if column < np.shape(field)[1]:
        rightmost = False
    # check the number of mines
    if not upmost:
        if field[row - 1][column] == 1:
            mine_count += 1
        if not leftmost:
            if field[row - 1][column - 1] == 1:
                mine_count += 1
        if not rightmost:
            if field[row - 1][column + 1] == 1:
                mine_count += 1
    if not downmost:
        if field[row + 1][column] == 1:
            mine_count += 1
        if not leftmost:
            if field[row + 1][column - 1] == 1:
                mine_count += 1
        if not rightmost:
            if field[row + 1][column + 1] == 1:
                mine_count += 1
    if not leftmost:
        if field[row][column - 1] == 1:
            mine_count += 1
    if not rightmost:
        if field[row][column + 1] == 1:
            mine_count += 1
    return mine_count

# Flag a specific position and store this into the flag_list.
# Return the existing list when the position to be flagged is
# already existing in the flag_list; Return the flag_list with new
# elements added into the list when the flagging position does not exist
# in the list.
def flag(flag_list, row, column):
    if [row, column] not in flag_list:
        # return the new list when a new position is being flagged
        return flag_list.append([row,column])
    # return the existing list when the position is already flagged
    return flag_list

# Remove a position in the flag_list when it exists.
# When there are no such position in the list, return the existing list.
def unflag(flag_list, row, column):
    if [row, column] in flag_list:
        # return the new list with the position removed
        return flag_list.remove([row,column])
    # return the existing list if the position is not inside the list
    return flag_list

# Verify if the list of flagged elements matches the list of mines.
# In other words, check if the game is done.
def check_game(mine_list, flag_list):
    # first check if the flag_list have the same length as mine_list
    if len(mine_list) == len(flag_list):
        # check all the elements one by one
        for element in flag_list:
            if element not in mine_list:
                # return false if the flag list doesn't match
                return False
        # if everything matches then that is automatically true
        return True
    # if there are not enough elements in the flag list then just return false
    return False

# Reveals one position on the field. Return the number of mine surrounding it
# if this position does not have a mine; return False if that position is a mine.
# Assuming that the user input a data within the correct range.
def reveal(field, row, column, mine_list):
    # Check if the position to be revealed contains mine
    if [row, column] in mine_list:
        return False
    # now return the mine number of the revealing position
    return mine_number(field, row, column)

# Test the functions in the main function
def main():
    field = generate_field()
    mine_information = place_mine(field, 25)
    field = mine_information[0]
    mine_list = mine_information[1]
    print(field)
    print(mine_list)
if __name__ == '__main__':
    main()