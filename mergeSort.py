def mergeSort(alist):
    if len(alist) > 1:
        leftList = alist[:len(alist) // 2]
        rightList = alist[len(alist) // 2:]

        mergeSort(leftList)
        mergeSort(rightList)

        i = 0
        j = 0
        k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] > rightList[j]:
                alist[k] = leftList[i]
                i += 1
            else:
                alist[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):
            alist[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            alist[k] = rightList[j]
            j += 1
            k += 1
    print("merging" + str(alist))

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


