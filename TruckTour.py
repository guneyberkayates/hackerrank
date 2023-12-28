explain in detail : #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    n = len(petrolpumps)
    start_index = 0
    total_petrol = 0
    total_distance = 0

    for i in range(n):
        petrol, distance = petrolpumps[i]

        total_petrol += petrol
        total_distance += distance

        if total_petrol < total_distance:
            # If the truck cannot reach the next petrol pump, update 
start_index
            start_index = i + 1
            total_petrol = 0
            total_distance = 0

    # Check if the total petrol is sufficient to cover the total distance
    if total_petrol >= total_distance:
        return start_index
    else:
        return -1  # No solution found 
            
        
                
            
                
            
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()

