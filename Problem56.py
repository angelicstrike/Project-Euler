#!/usr/bin/python3

import SumDigits

current = 0
maximum = 0

for x in range(100):
    for y in range(100):
        current = SumDigits.SumDigitsAsNum(x**y)
        if(current > maximum):
            maximum = current
print(str(maximum))
