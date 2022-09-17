import sys


def multi_sort(array):
    original = array
    individualArrayLength = len(array[0])
    totalArrayCount = len(array)
    newArray = [[] for i in range(totalArrayCount)]
    pointerX, pointerY = 0, 0
    # find the minimum value from all the arrays, and move it into a new array
    while len(newArray[totalArrayCount-1]) < individualArrayLength:
        currentMin = sys.maxsize
        arrayIndexMin = -1
        for index, individualArray in enumerate(original):
            if not individualArray:
                continue
            arrayMin = min(individualArray)
            if arrayMin < currentMin:
                currentMin = arrayMin
                arrayIndexMin = index
        original[arrayIndexMin].remove(currentMin)
        if pointerX == individualArrayLength:
            pointerX = 0
            pointerY += 1

        newArray[pointerY].append(currentMin)
        pointerX += 1
    return newArray