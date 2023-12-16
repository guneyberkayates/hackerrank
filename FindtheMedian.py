#!/bin/python3

import math
import os
import random
import re
import sys

def findMedian(arr):
    arr.sort()
    n = len(arr) 
    if len(arr) % 2 != 0:
        return arr[n // 2]
    else:
        return (arr[(n // 2) - 1] + arr[n // 2]) // 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

