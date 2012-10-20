#returns the factorial of a number
#!/usr/bin/python3
def factorial(number):
    if number <= 1:
        return 1  
    return number * factorial(number - 1)

if(__name__=='__main__'):
    fact = factorial(10)
    print(fact)
