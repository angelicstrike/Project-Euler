#!/usr/bin/python3

reader = open('FiftyNumbers.txt').read().split()
total = sum( [int(x[:11]) for x in reader] )
print(str(total))
