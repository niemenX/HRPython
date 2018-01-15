#!/bin/python3

import sys

def updateGrade(g):
    return g + (5 - g % 5 ) if g % 5 > 2 else g
    

def solve(grades):
    for i in range(len(grades)):
        if grades[i] < 38 : continue
        grades[i] = updateGrade(grades[i])

    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


