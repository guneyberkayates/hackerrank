#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    grid = [list(row) for row in grid] #iterate each row in array and turn 
to seperate chars
    
    rows = len(grid)
    columns = len(grid[0])
    
    for i in range(rows):
        grid[i].sort() #iterating in each row and sorting each row 
alphabetically
        
    #now each row of the grid is in order
    
    for i in range(1,rows):
        for j in range(columns):
            if not grid[i-1][j] <= grid[i][j]: 
            #compare grid vertically and see if sorting inside rows worked
                return "NO"
    return "YES"
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

