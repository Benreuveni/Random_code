#!/usr/bin/env python

'''
This is a simple script that showcases backtracking by providing all possible valid solutions to a sudoku puzzle.
'''

__author__ = "Ben Reuveni"
__date__ = "02_16_2020"

import numpy as np

# initialize a numpy matrix to represent the sudoku table
# this particular one is from the NYT Sudoku Feb 16th 2020


puzzle_1 = [[0,0,6,0,0,0,0,0,0],
         [0,0,0,8,9,0,0,0,0],
         [0,4,1,0,0,3,0,0,0],
         [0,8,0,0,0,5,1,0,7],
         [3,6,0,0,7,0,0,0,0],
         [0,0,0,0,0,0,2,0,0],
         [0,0,0,3,0,1,0,2,0],
         [0,7,0,0,8,2,4,1,3],
         [0,0,0,0,0,0,8,0,0]]

# print the sudoku grid
# print(np.asmatrix(puzzle_1))

def is_valid(row, column, candidate, data):

    # check whether the candidate value is in the row
    for r in range(len(data[row])):
        if data[row][r] == candidate:
            return False
    # check whether the candidate value is in the column
    for c in range(len(data[row])):
        if data[c][column] == candidate:
            return False

    # find which of the 9 boxes we are in
    lower_box_row = (row // 3) * 3
    lower_box_col = (column // 3) * 3

    # check whether the candidate value is in the box
    for box_row in range(3):
        for box_col in range(3):
            if data[lower_box_row + box_row][lower_box_col + box_col] == candidate:
                return False
    return True

def solver(data):
    for row in range(9):
        for col in range(9):
            if data[row][col] == 0:
                for candidate in range(1, 10):
                    '''
                    This is where the 'magic' happens.
                    Once we've identified a square that needs a value (i.e. == 0) we start going number by number.
                    If the number is valid for the square, we assign it. We then repeat the process looking for
                    the next square that needs a solution through recursion.
                    
                    If we run into a situation where we have a square that needs a value, but there are no valid
                    solutions, we know our solution up until this point is bad. We then assign that initial square
                    back to 0 and start the process over with the next possible answer for that initial square.
                    
                    Concrete example:
                    * Find empty square
                    * try 1
                    ** 1 is not valid
                    *try 2
                    ** 2 is valid.
                    *** assign 2 to square
                    *** look for next empty square
                    *** try 1
                    **** 1 is not valid
                    *** try ... 9
                    **** no values are valid. # this implies that 2 was not an appropriate solution, earlier
                    ** set square from 2 to 0
                    * try 3
                    ...
                    '''
                    if is_valid(row, col, candidate, data):
                        data[row][col] = candidate
                        solver(data)
                        data[row][col] = 0
                return
    print(np.matrix(data))

solver(puzzle_1)