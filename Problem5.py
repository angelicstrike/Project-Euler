#!/usr/bin/python3

import SieveOfAtkins
import factorize
import math

def lcm(numbers):
    primes = SieveOfAtkins.SieveOfAtkins(numbers[-1] + 10)
    primesCount = {}
    least = 1
    for w in primes:
        print(str(w))
        primesCount[w] = 0
            
    for x in numbers:
        factors = factorize.factor(x)
        for y in primes:
            if(factors.count(y) > primesCount[y]):
                primesCount[y] = factors.count(y)
    for z in primesCount.keys():
        least *= math.pow(z, primesCount[z])
    return least
if(__name__=="__main__"):
    nums = range(1,21)
    ans = lcm(nums)
    print(str(ans))
