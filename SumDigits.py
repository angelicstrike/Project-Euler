#!/usr/bin/python3
def SumDigitsAsNum(num):
    length = len(str(num))
    total = 0
    for x in range(0, length):
        #Number Mod 10 returns the value of the digit in the ones place
        total += (num % 10)
        # the //= 10 cuts of the digit in the ones place 
        num //= 10
    return total

if(__name__ == '__main__'):
    ans = SumDigitsAsNum(2**1000)
    print(ans)
