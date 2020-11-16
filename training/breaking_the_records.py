#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minscore = maxscore = scores[0]
    
    bmin, bmax = 0, 0
    for score in scores[1:]:
        if score > maxscore:
            maxscore  = score
            bmax += 1
            
        elif score < minscore:
            minscore = score
            bmin += 1
            
    return bmax, bmin
    
if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)

