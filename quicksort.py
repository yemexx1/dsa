"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):

    pivot = len(array) - 1
    i = 0

    while pivot != i:
        if array[i] > array[pivot]:
            temp = array[i]
            array[i] = array[pivot - 1]
            array[pivot - 1] = array[pivot]
            array[pivot] = temp
            pivot -= 1
            i = 0
        else:
            i += 1

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)