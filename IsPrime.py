import sys
import math
import time

def GeneratePrimesFinite(MaxCount):
    count = 2
    isPrime = 0
    numToCheck = 5
    primes = [2, 3]
    while (count < MaxCount): 
       for x in primes:
            if( (numToCheck % x) == 0):
                isPrime = 0
                break
            isPrime = 1
       if(isPrime == 1):
           primes.append(numToCheck)
           count += 1
       numToCheck += 2
    return primes

def IsPrime(number):
    a = int(math.sqrt(number))+1
    divisor = 3

    if((number % 2) == 0):
        return False

    while(divisor < a):
        if((number % divisor) == 0):
            return False
        divisor += 2
    return True

def GeneratePrimesBelow(Ceiling):
    primes = [2, 3]
    for x in range(3, Ceiling, 2):
        if(IsPrime(x) == True):
            primes.append(x)
    return primes

if (__name__ == '__main__'):
    start = time.time()
    GeneratePrimesBelow(2000000)
    print(time.time() - start)
