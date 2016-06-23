from Node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def addNode(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        size = 1
        if self.isEmpty() is True:
            return 0
        else:
            while current.getNext() is not None:
                size += 1
                current = current.getNext()

        return size

    def search(self, data):
        current = self.head
        while current.getNext() is not None:
            if data == current.getData():
                return True
            else:
                current = current.getNext()
        return False

    def remove(self, data):
        previous = self.head
        if data == self.head.getData():
            self.head = self.head.getNext()
            return
        current = previous.getNext()
        while current.getNext is not None:
            if current.getData() != data:
                previous = current
                current = current.getNext()
            else:
                previous.setNext(current.getNext())
                return


if __name__ == "__main__":
    ulist = UnorderedList()
    print ulist.isEmpty()
    ulist.addNode(1)
    print ulist.isEmpty()
    print ulist.size()
    ulist.addNode(2)
    print ulist.size()
    ulist.remove(1)
    ulist.addNode(1)
    print ulist.size()
    print ulist.search(1)
    ulist.remove(1)
    print ulist.search(1)
    print ulist.size()

