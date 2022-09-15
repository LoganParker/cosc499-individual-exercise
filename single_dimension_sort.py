import sys


def single_sort(array):
    sortedArray = []
    while array:
        mini = sys.maxsize
        for value in array:
            if value < mini:
                mini = value
        sortedArray.append(mini)
        array.remove(mini)
    return sortedArray
