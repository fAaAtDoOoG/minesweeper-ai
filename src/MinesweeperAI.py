# import some basic libraries and the Minesweeper game
from MinesweeperGame import *
import numpy as np

# Generates a game field that records all the revealed numbers.
# Basically generates a -1 matrix with the same shape as the minefield, which
# is not shown to the player.
# Since all the block are not revealed at the start of the game, they are
# labeled -1 not 0.
def generate_game_field(field):
    # get the shape of the existing minefield to generate another matrix with
    # the same shape
    shape = np.shape(field)
    # return a zero matrix with the same shape
    return np.negative(np.ones(shape))

# Returns an 8-dimension vector consists of the input value, which includes
# the mine number around one block.
# Note that the top left corner of the field is (1, 1).
def input_vector(row, column, game_field):
    # check all the surrounding positions of the block (row, column)
    in_vector = np.zeros(8)
    in_vector[0] = game_field[row-1][column]
    in_vector[1] = game_field[row+1][column]
    in_vector[2] = game_field[row][column-1]
    in_vector[3] = game_field[row][column+1]
    in_vector[4] = game_field[row-1][column-1]
    in_vector[5] = game_field[row-1][column+1]
    in_vector[6] = game_field[row+1][column-1]
    in_vector[7] = game_field[row+1][column+1]
    return in_vector

# run the minesweeper game for iterations times
def run(iterations):
    for i in range(iterations):
        # initialize the game
        field = generate_field(10, 10)
        game_field = generate_game_field(field)
        flag_list = []
        mine_list = place_mine(field)
