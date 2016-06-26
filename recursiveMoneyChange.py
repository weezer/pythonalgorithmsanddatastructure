def recMC(coinValue, change):
    minCoins = change
    if change in coinValue:
        return 1
    else:
        for i in [c for c in coinValue if c <= change]:
            coinNum = 1 + recMC(coinValue, change - i)
            if coinNum < minCoins:
                minCoins = coinNum

    return minCoins

print(recMC([1,5,10,25],63))
