import DeQueue
def palindromeChecker(alist):
    aQueue = DeQueue.DeQueue()

    for i in alist:
        aQueue.addRear(i)

    while aQueue.size() >= 2:
        if aQueue.removeFront() != aQueue.removeRear():
            return False

    return True

if __name__ == "__main__":
    print(palindromeChecker("abcba"))
    print(palindromeChecker("abba"))
    print(palindromeChecker("abca"))