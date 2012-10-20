import csv

def readFile(reader):
    strMatrix = list()
    intMatrix = list()
    
    for line in reader.readlines():
        strMatrix.insert(0, line)

    for x in range(0, len(strMatrix)):
        temp = list()
        for y in range(0, len(strMatrix)):
            temp.append(int(strMatrix[x][y]))
        intMatrix.append(temp)
        del temp
    return matrix


def Grid(matrix):
    #test = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
    running = test[4][4]
    count = 0
    x = 4
    y = 4
    tempX = x - 1
    tempY = y - 1
    while(count <= (len(test)-1) * 2):
        if(matrix[x][tempY] > matrix[tempX][y]):
            running += matrix[tempX][y]
            x = tempX
            if(tempX == 0):
                tempX = 0
            else:
                tempX -= 1
        elif(matrix[x][tempY] < matrix[tempX][y]):
            running += test[x][tempY]
            y = tempY
            if(tempY == 0):
                tempY = 0
            else:
                tempY -= 1
        count += 1
    return running

if(__name__=='__main__'):
    readerObject = csv.reader(open("matrix.txt", "r"))
    answer = readFile(readerObject)
    final = Grid(answer)
    print(str(final))
    print("Done!")
