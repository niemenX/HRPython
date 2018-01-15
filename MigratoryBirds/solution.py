#!/bin/python3
from collections import defaultdict
import sys

def migratoryBirds(n, ar):
    d = defaultdict(int)
    for i in ar:
        d[i] += 1
    return max(d.items(), key=lambda x: x[1])[0]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
