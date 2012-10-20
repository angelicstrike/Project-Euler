#For Problems 18 AND 67
def ReadFile(fileObject):
    fileObject.flush()
    triangle = list()
    listOfRows = list()
    finalSum = 0
    
    for line in fileObject.readlines():
        triangle.insert(0, line)
    for x in range(0, 100):
        tempList = list()
        for y in range(0, len(triangle[x]), 3):
            tempList.append(int(triangle[x][y:y+2]))
        listOfRows.append(list(tempList))

    for a in range(0,len(listOfRows)):
        for b in range(0, len(listOfRows[a])-1):
            if(listOfRows[a][b] > listOfRows[a][b+1]):
                listOfRows[a+1][b] = listOfRows[a][b]+listOfRows[a+1][b]
            else:
                listOfRows[a+1][b] = listOfRows[a][b+1]+listOfRows[a+1][b]
    finalSum = listOfRows[len(listOfRows)-1][0]
    return finalSum

if(__name__=='__main__'):
    reader = open("triangle.txt", "r")
    final = ReadFile(reader)
    print(final)
