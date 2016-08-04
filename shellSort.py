@TODO
def shellSort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for index in range(gap):
            while index < len(alist) and alist[index - gap] > alist[index]:
                temp = alist[index - gap]
                alist[index - gap] = alist[index]
                alist[index] = temp
        gap = gap // 2

