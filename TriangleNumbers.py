import SieveOfAtkins
import math

def TriangleNumbers(limit):
    total = 0
    for x in range(1,limit+1):
        total = total + x
    return total

if(__name__=='__main__'):
    fun = TriangleNumbers(15)
    print(fun)    
