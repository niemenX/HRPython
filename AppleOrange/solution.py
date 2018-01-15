#!/bin/python3

import sys

def appleAndOrange(s, t, a, b, apple, orange):
    return (sum([1 for x in apple if (x + a) >= s and (x + a) <= t]),sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))



