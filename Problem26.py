import GCD

def DecimalExpansion(n):
    for x in range(1, 2000):
        if((10**x) % n == 1 and GCD.gcd(10, n)):
            return x
    return -1    
if(__name__ == '__main__'):
    answer = 0
    for y in range(1,1000):
        temp = DecimalExpansion(y)
        if(temp > answer):
            answer = y
    print('The answer to Project Euler problem 26 is ' + str(answer))
    
