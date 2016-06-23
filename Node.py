class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, item):
        self.data = item

    def setNext(self, newnext):
        self.next = newnext
