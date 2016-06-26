def DpmakeChage(coinValue, change):
    changeArray = [x for x in range(change + 1)]

    for i in range(len(changeArray)):
        for c in [x for x in coinValue if i > x]:
            changeArray[i] = (changeArray[i], changeArray[i - c] + 1)[changeArray[i] > changeArray[i-c] + 1]

    print changeArray


DpmakeChage([1,5,10,25], 63)