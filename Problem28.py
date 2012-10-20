lowerLeft = 0
upperRight = 0
for x in range(2, 1415, 2):
    upperRight += (x+1)*(x+1)
    lowerLeft += (x)*(x)+1


sumLR = 3
sumUL = 7

for y in range(2, 1415):
    lowerRight = 3
    lowerRight = lowerRight + (8*(y-1)) + 2
    sumLR += lowerRight
    
    upperLeft = 7
    upperLeft = upperLeft + (8*(y-1)) + 6
    sumUL += upperLeft

total = lowerLeft + upperRight + sumLR + sumUL + 1

print(str(total))
