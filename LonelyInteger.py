#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    i = 0
    while i < len(a):
        anything = a[i]
        seen = 1
        j = i + 1
        while j < len(a):
            if a[j] == anything:
                seen += 1
                del a[j]
            else:
                j += 1
        if seen == 1:
            return anything
        i += 1
                
             
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
