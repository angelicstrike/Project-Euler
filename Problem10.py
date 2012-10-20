import SieveOfAtkins
import time

start = time.time()
primes = SieveOfAtkins.SieveOfAtkins(2000000)
SumPrimes = sum(primes)
print(str(SumPrimes))
print('Done')
print(time.time() - start)
