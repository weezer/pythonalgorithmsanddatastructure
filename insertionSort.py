def insertionSort(alist):
    for i in range(len(alist)):
        position = i
        while position > 0 and alist[position] < alist[position-1]:
            temp = alist[position]
            alist[position] = alist[position-1]
            alist[position-1] = temp
            position -= 1
    print alist

alist = [12, 43, 152, 1, 2, 4, 11, 35, 22, 23, 5, 666]

insertionSort(alist)