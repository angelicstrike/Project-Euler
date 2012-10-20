#!/usr/bin/python3

import IsPrime 
import SieveOfAtkins
import math

def factor(number):
    factors = list()
    numToFactor = number
    primes = SieveOfAtkins.SieveOfAtkins(number)

    primality = IsPrime.IsPrime(numToFactor)
    while(primality == False):
        for x in primes:
            if((numToFactor % x) == 0):
                factors.append(x)
                numToFactor = numToFactor/x
                primality = IsPrime.IsPrime(int(numToFactor))
                break
    if(numToFactor != 1):
        factors.append(int(numToFactor))
    return factors


if(__name__=='__main__'):
    y = input("Enter in a number to factor: ")
    print('Factoring ' + y)
    y = int(y)
    factors = factor(y)
    for x in factors:
        print(x)
