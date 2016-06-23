import aQueue


def potatoGame(alist, base):
    nameQueue = aQueue.aQueue()
    for i in alist:
        nameQueue.enQueue(i)
    while nameQueue.size() > 1:
        for num in range(base - 1):
            nameQueue.enQueue(nameQueue.deQueue())
        nameQueue.deQueue()
    return nameQueue.deQueue()

if __name__ == "__main__":
    print(potatoGame(['1', '2', '3', '4', '5potatoGame.py:16', '6', '7'], 2))