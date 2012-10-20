def Problem2():
    import sys
    isPal = 0
    for w in range(998001, 9999, -1):
        v = str(w)
        for x in range(0, len(v)):
            if(v[x] == v[len(v) - 1 - x]):
                isPal = 1
            else:
                isPal = 0
                break
        if(isPal == 1):
            for y in range(999, 99, -1):
                if((w % y == 0) and (w/y >= 100) and (w/y <= 999)):
                    return w
    return -1

if(__name__=='__main__'):
    answer = Problem2()
    print(str(answer))
