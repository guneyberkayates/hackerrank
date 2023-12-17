#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonalSum1,diagonalSum2=0,0
    rows = len(arr)
    i=0
    while i < rows:
        diagonalSum1 += arr[i][i]
        i+=1
        
    j = 0
    k = rows - 1 
    while k >= 0:
        diagonalSum2 += arr[j][k]
        j += 1
        k -= 1
        
        
    ans = abs(diagonalSum2 - diagonalSum1)
    return ans
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

