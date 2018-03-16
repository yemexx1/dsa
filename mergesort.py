def mergeSort(alist):
    print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist) / 2
        left_list = alist[:mid]
        right_list = alist[mid:]

        mergeSort(left_list)
        mergeSort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                alist[k] = left_list[i]
                i += 1
            else:
                alist[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            alist[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            alist[k] = right_list[j]
            j += 1
            k += 1

    print("merging", alist)


alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)