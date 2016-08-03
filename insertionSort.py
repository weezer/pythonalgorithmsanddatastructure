def insertionSort(alist):
    for i in range(len(alist)):
        position = i
        while position > 0 and alist[position] < alist[position-1]:
            temp = alist[position]
            alist[position] = alist[position-1]
            alist[position-1] = temp
    print alist

alist = [3]

insertionSort(alist)