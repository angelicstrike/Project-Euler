#!/usr/bin/python3

import math

def fibonacci(limit):
    a = 0
    b = 1
    Fib = 0
    
    numbers = [0]

    while(Fib <= limit):
#numbers.append(Fib)
        Fib = a + b
        a = b
        b = Fib
    return numbers

if(__name__=='__main__'):
    nums = fibonacci(10000000)
    for x in nums:
        print(x)
