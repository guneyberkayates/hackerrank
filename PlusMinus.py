#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n=len(arr)
    countPositive,countNegative,zero=0,0,0
    for i in range(0,len(arr)):
        if arr[i]>0:
            countPositive+=1
        elif arr[i]==0:
            zero+=1
        else:
            countNegative+=1
    print(countPositive/n)
    print(countNegative/n)
    print(zero/n)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

