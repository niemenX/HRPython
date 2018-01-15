#!/bin/python3

import sys

def timeConversion(s):
    x = s[-2:].lower()
    sx = s[:2]
    s = s[:-2]
    
    if x == "pm" :
        s = s[2:]
        s = str((12 if int(sx) == 12 else int(sx) + 12)) + s
    else:
         if sx == "12":
            s = s[2:]
            s = "00" + s
    return s

s = input().strip()
result = timeConversion(s)
print(result)
