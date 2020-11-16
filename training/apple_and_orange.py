#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    num_a, num_o = 0,0 
    
    # get the landing of for both apples and oranges
    land_a = [l + a for l in apples]
    land_o = [l + b for l in oranges]
        
    # check if they are in range of house, if so increment count by 1
    for pos in land_a:
        if pos <= t and pos >= s:
            num_a +=1
            
    for pos in land_o:
        if pos <= t and pos >= s:
            num_o +=1
    
    print(num_a)
    print(num_o)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
