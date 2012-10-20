def SumOfSquares(SquaresCount):
    SumSquares = 0
    for x in range(1, SquaresCount+1):
        SumSquares += (x*x)
    return SumSquares

def SquareOfSums(SumCount):
    SquaresSum = 0
    temp = 0
    for y in range(1, SumCount + 1):
        temp += y
    SquaresSum = temp * temp
    return SquaresSum

ans = SquareOfSums(100) - SumOfSquares(100)
print(str(ans))
