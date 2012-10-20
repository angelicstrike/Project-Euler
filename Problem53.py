#Problem 53 Project Euler
#Set of n, choose k

import math

def binomial(n, k):
  nt = 1
  for t in range(min(k, n-k)):
      nt = nt*(n-t)//(t+1)
  return nt

if(__name__=='__main__'):
    qualifiers = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            result = binomial(n,r)
            if(result > 1000000):
                qualifiers = qualifiers + 1
    print(str(qualifiers))
