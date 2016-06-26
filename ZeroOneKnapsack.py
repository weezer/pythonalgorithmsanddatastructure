valueList = [10, 9, 6, 1, 4, 1, 9, 20, 6, 20, 4, 10, 6, 3, 5, 4, 6]
weightList = [5, 4, 3, 5, 2, 5, 4, 4, 3, 4, 2, 5, 2, 2, 6, 5, 4]
bagSize = 10
DPMatrix = [[0 for x in range(bagSize + 1)] for y in range(len(valueList) + 1)]


def maxWeight():
    for i in range(len(weightList) + 1):
        for j in range(bagSize + 1):
            DPMatrix[i][j] = (0, DPMatrix[i-1][j])[i != 0]
            if i > 0 and j >= weightList[i - 1]:
                DPMatrix[i][j] = DPMatrix[i][j] if DPMatrix[i][j] > (DPMatrix[i-1][j-weightList[i-1]] + valueList[
                    i-1]) else (DPMatrix[i-1][j-weightList[i-1]] + valueList[i-1])
    print DPMatrix[len(weightList)][bagSize]


def whichGem():
    selectGem = [0 for x in range(len(valueList))]
    Column = bagSize
    for i in reversed(range(len(valueList)+1)):
        if DPMatrix[i][Column] > DPMatrix[i-1][Column]:
            selectGem[i-1] = 1
            Column -= weightList[i-1]
    print selectGem

maxWeight()
whichGem()




