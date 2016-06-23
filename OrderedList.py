from Node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    #eg, head -> 1, 2, 3, 4
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and stop is False:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setNext(current)

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() != item:
                current = current.getNext()
            else:
                return True

        return False

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.getNext()
        return size

    # assuming the item is present in the list
    def remove(self, item):
        current = self.head
        previous = None
        while True:
            if current.getData() != item:
                previous = current
                current = current.getNext()
            else:
                break
        if previous is None:
            self.head = None
        else:
            previous.setNext(current.getNext())

    # assuming the item is present in the list
    def index(self, item):
        position = 0
        current = self.head
        while True:
            if current.getData() == item:
                return position
            else:
                current = current.getNext()
                position += 1

    #pop the last item from the list
    def pop(self):
        current = self.head
        previous = None
        while current is not None:
            if current.getNext() is None and previous is not None:
                previous.setnext(current.getNext())
            if current.getNext() is None and previous is None:
                self.head = None
            previous = current
            current = current.getNext()
        return previous.getData()

    #pop the iteam on the position, assuming the position number is less than the list size
    def pop(self, pos):
        current = self.head
        previous = None
        position = 0
        if pos == 0:
            self.head = current.getNext()
            return current.getData()
        while position < pos:
            previous = current
            current = current.getNext()
        previous.setNext(current.getNext())
        return current.getData()

