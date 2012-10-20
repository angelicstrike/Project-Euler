import math
import operator
import time

def SieveOfAtkins(limit):
    primes = [2, 3]
    isPrime = [False]*(limit)
    root = int(math.sqrt(limit))

    for x in range(1, root):
        for y in range(1, root):
            an = (4*x*x) + (y*y)
            if(an <= limit and ((an % 12 == 1) or (an % 12 == 5))):
                isPrime[an] = operator.xor(isPrime[an], True)

            bn = (3*x*x) + (y*y)
            if(bn <= limit and bn % 12 == 7):
                isPrime[bn] = operator.xor(isPrime[bn], True)

            cn = (3*x*x) - (y*y)
            if(x > y and cn <= limit and cn % 12 == 11):
                isPrime[cn] = operator.xor(isPrime[cn], True)
    for z in range(5, root):
        if(isPrime[z] == True):
            s = z*z
            for a in range(s, limit, s):
                isPrime[a] = False
    for b in range(5, limit, 2):
        if(isPrime[b] == True):
            primes.append(b)

    return primes

if(__name__=='__main__'):
    limit = input('Enter an Upper Limit: ')
    prime = SieveOfAtkins(int(limit)+1)
    for x in prime:
        print(x)
