#!/bin/python3

import sys

def miniMaxSum(arr):
    s = sum(arr)
    res = str(s-max(arr))
    res += " "
    res += str(s-min(arr))

    print(res)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
