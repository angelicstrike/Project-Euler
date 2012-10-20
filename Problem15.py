#!/usr/bin/python3

import math

def Combinations(m, n):
#for an m x n grid
    total = math.factorial(m+n)/((math.factorial(m))*(math.factorial(n)))
    return total

if(__name__=='__main__'):
    answer = Combinations(20,20)
    print(str(answer))
