#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Convert the string n to a list of integers
    n = [int(digit) for digit in n]
    
    # Calculate the super digit of the sum of n multiplied by k
    result = super_digit_recursive(sum(n) * k)
    
    return result

def super_digit_recursive(num):
    # If the number is a single digit, return it
    if num < 10:
        return num
    
    # Otherwise, calculate the super digit of the sum of its digits
    return super_digit_recursive(sum([int(digit) for digit in str(num)]))

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

