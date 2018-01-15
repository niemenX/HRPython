#!/bin/python3

import sys

def staircase(n):
    for i in range(1, n+1):
        print(("#"*i).rjust(n))
    return

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
