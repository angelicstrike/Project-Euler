def Collatz(num):
    count = 0
    while(num > 1):
        if(num % 2 == 0):
            num /= 2
            count += 1
            continue
        if(num % 2 == 1):
            num = (3 * num) + 1
            count += 1
            continue
    return count

if(__name__=='__main__'):
    chains = dict()
    maxCount = 1
    ind = 1
    for x in range(3, 1000000, 2):
        chains[x] = Collatz(x)
        if(chains[x] > maxCount):
            maxCount = chains[x]
            ind = x
    print(str(ind))
