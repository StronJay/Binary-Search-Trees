array1 = [10, 15, 8, 12, 94, 81, 5, 2, 10]
array2 = [10, 8, 5, 15, 2, 10, 12, 94, 81]

def sameBst(array1, array2):
    return sameBstRecursiveHelper(array1, array2, 0, 0, float("-inf"), float("inf"))

def sameBstRecursiveHelper(array1, array2, rootIdx1, rootIdx2, minValue, maxValue):
    print("ROOTS:", rootIdx1, rootIdx2)
    if rootIdx1 == -1 or rootIdx2 == -1:
        return rootIdx2 == rootIdx1
    if array1[rootIdx1] != array2[rootIdx2]:
        return False

    leftR1 = getFirstSmallerIndex(array1, rootIdx1, minValue)
    leftR2 = getFirstSmallerIndex(array2, rootIdx2, minValue)
    rightR1 = getFirstBiggerIndex(array1, rootIdx1, maxValue)
    rightR2 = getFirstBiggerIndex(array2, rootIdx2, maxValue)
    print("LEFT AND RIGHT INDICES:", leftR1, leftR2, rightR1, rightR2,)

    cVal = array1[rootIdx1]
    sameLeft = sameBstRecursiveHelper(array1, array2, leftR1, leftR2, minValue, cVal)
    sameRight = sameBstRecursiveHelper(array1, array2, rightR1, rightR2, cVal, maxValue)
    print("SAME LEFT AND RIGHT:", sameLeft, sameRight)
    return sameLeft and sameRight


def getFirstSmallerIndex(array, startIdx, minValue):
    for i in range(startIdx + 1, len(array)):
        #print("SMALL:", i, array[i], array[startIdx])
        if array[i] < array[startIdx] and array[i] >=minValue:
            print("Small moves on to next round:", i)
            return i
    return -1

def getFirstBiggerIndex(array, startIdx, maxValue):
    for i in range(startIdx + 1, len(array)):
        #print("BIG:", i, array[i], array[startIdx])
        if array[i] >= array[startIdx] and array[i] < maxValue:
            print("Big moves on to next round:", i)
            return i
    return -1

print(sameBst(array1, array2))