class BinaryHeap(object):
    def __init__(self):
        self._heap = [0]
        self._size = 0

    def _percup(self, pos):
        while pos // 2 > 0:
            if self.heap[pos] < self.heap[pos // 2]:
                tmp = self.heap[pos]
                self.heap[pos] = self.heap[pos // 2]
                self.heap[pos // 2] = tmp
            pos = pos // 2

    def insert(self, num):
        self.heap.append(num)
        self.size += 1
        self._percup(self.size)

    def delmin(self):
        min = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self._percdown(1)
        return min

    def _percdown(self, pos):
        while pos * 2 <= self.size:
            mc = self._minchild(pos)
            if self.heap[pos] > self.heap[mc]:
                tmp = self.heap[mc]
                self.heap[mc] = self.heap[pos]
                self.heap[pos] = tmp
            pos = mc

    def _minchild(self, pos):
        if pos * 2 + 1 >= self.size:
            return pos * 2
        else:
            return (pos * 2, pos * 2 + 1)[self.heap[pos * 2 + 1] < self.heap[pos * 2]]

    def buildheap(self, alist):
        i = len(alist) // 2
        self.heap = [0] + alist[:]
        self.size = len(alist)
        while i > 0:
            self._percdown(i)
            i -= 1


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def heap(self):
        """I'm the 'heap' property."""
        return self._heap

    @heap.setter
    def heap(self, value):
        self._heap = value

if __name__ == "__main__":
    bh = BinaryHeap()
    bh.buildheap([9, 5, 6, 2, 3])
    print bh.heap
    print(bh.delmin())
    print(bh.delmin())
    print(bh.delmin())
    print(bh.delmin())
    print(bh.delmin())