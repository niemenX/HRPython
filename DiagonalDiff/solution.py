#!/bin/python3

import sys

def diagonalDifference(a):
    d1, d2 = 0, 0
    for i in range(len(a)):
        d1 += a[i][i]
        d2 += a[i][len(a)-i-1]
    
    return abs(d1 - d2)


if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
