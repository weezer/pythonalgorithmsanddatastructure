#TODO finish the shell sort
def shellsort(alist):
    sublistgap = len(alist) // 2
    while sublistgap >= 1:
        for i in range(0, sublistgap):
            insertion_sort(alist, i, sublistgap)
        sublistgap //= 2
        print alist


def insertion_sort(thelist, start, gap):
    listlen = len(thelist)
    for i in range(start, listlen, gap):
        position = i
        while position > 0 and thelist[position - gap] > thelist[position]:
            temp = thelist[position]
            thelist[position] = thelist[position - gap]
            thelist[position - gap] = temp
            position -= gap


xxx = [12, 43, 152, 1, 2, 4, 11, 35, 22, 23, 5, 666]


shellsort(xxx)
# print xxx