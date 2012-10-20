#!/usr/bin/python3

import math

def GeneratePhi():
#Returns the value of phi, the golden ratio
    phi = (1.0/2.0) * (1.0 + math.sqrt(5))
    return phi

def BinetFibonacci(n):
    phi = GeneratePhi()
    fibonacci = ((phi ** n) - ((phi * -1) ** (n * -1)))/(math.sqrt(5))
    return int(fibonacci)

if(__name__=='__main__'):
    test1 = GeneratePhi()
    test2 = BinetFibonacci(99)
    print(str(test1))
    print(str(test2))
