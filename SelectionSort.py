def selectionSort(alist):
    for i in range(len(alist)-1, 0, -1):
        maxposition = 0
        for j in range(1, i+1):
            maxposition = (maxposition, j)[alist[maxposition] < alist[j]]
        temp = alist[i]
        alist[i] = alist[maxposition]
        alist[maxposition] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print alist