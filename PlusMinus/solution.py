#!/bin/python3

import sys

def plusMinus(arr):
    l = len(arr)
    p, z, n = 0,0,0
    for i in range(l):
        p += (1 if arr[i] > 0 else 0)
        z += (1 if arr[i] == 0  else 0)
        n += (1 if arr[i] < 0  else 0)
    
    print(p/l)
    print(n/l)
    print(z/l)
    
    return

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
