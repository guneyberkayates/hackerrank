#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alphabet='abcdefghijklmnopqrstuvwxyz'
    l=len(alphabet)
    new_s=''
    for char in s:
        if char.isupper():
            if alphabet.index(char.lower())+k>=l:
                
new_s+=alphabet[alphabet.index(char.lower())+k%l-l].upper()
            else:
                new_s+=alphabet[alphabet.index(char.lower())+k].upper()
        elif char.islower():
            if alphabet.index(char)+k>=l:
                new_s+=alphabet[alphabet.index(char)+k%l-l]
            else:
                new_s+=alphabet[alphabet.index(char)+k]
        else:
            new_s+=char
    return new_s  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

