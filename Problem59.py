import csv
import operator

#space -- 32
#t -- 116
#h -- 104
#e -- 101

def LetterFrequencies(numbers):
    freqList = dict()
    for x in range(0, len(numbers)):
        freqList[int(numbers[x])] = freqList.get(int(numbers[x]), 1) + 1
    for k in freqList.keys():
        print(str(k) + ' ===> ' + str(freqList[k]))
    return freqList

def BruteForcer(encrypted):
    unencrypted = list()

    for one in range(97, 123):
        for two in range(97, 123):
            for three in range(97, 123):
                unencrypted = list()
                key = [one, two, three]
                for x in range(0, len(encrypted)):
                    unencrypted.append(operator.xor(int(encrypted[x]), key[(x % 3)]))
                for x in range(0, len(unencrypted)-5):
                    if(unencrypted[x] == 32 and unencrypted[x+1] == 116 and unencrypted[x+2] == 104 and unencrypted[x+3] == 101 and unencrypted[x+4] == 32):
                        print(str(one))
                        print(str(two))
                        print(str(three))
                        return unencrypted
            del unencrypted
    return encrypted
    
if(__name__=='__main__'):
    csvFile = open("cipher2.csv", "r")
    csvReader = csv.reader(csvFile)
    listy = csvReader.__next__()
    texty = BruteForcer(listy)

    writer = open("decrypt.txt", "w")
    for x in range(0, len(texty)):
        writer.write(chr(texty[x]))
    writer.close()
    x = sum(texty)
    print(str(x))
