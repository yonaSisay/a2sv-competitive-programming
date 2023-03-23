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
    ans  = list(map(int , str(n)))
    ans = sum(ans) * k
    def fun():
        nonlocal ans
        nonlocal k
        
        if len(str(ans)) == 1:
            return 
        
        ans = sum(list(map(int , str(ans))))
        
        fun()
    fun()
    return ans
        
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
