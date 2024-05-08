#!/bin/python3

import math
import os
from heapq import heapify, heappush, heappop, _heapify_max


#
# Complete the 'minSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY num
#  2. INTEGER k
#

def minSum(num, k):
    if num is None or len(num) == 0:
        return 0
    res = 0
    counter = 0
    if k == 0:
        for j in num:
            res+=j
        return res


    while counter < k:
        _heapify_max(num)
        val = heappop(num)
        print(val)
        op=math.ceil(val/2)
        heappush(num, op)

        counter = counter+1

    for j in num:
        res+=j

    return res

if __name__ == '__main__':
    l = [7,20,10]
    print(minSum(l, 4))