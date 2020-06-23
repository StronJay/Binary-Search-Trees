# #O(n^2) T O(n) S
# def rightSmallerThan(array):
#     smallerArray = []
#     for i in range(len(array)):
#         count = 0
#         for j in range(i + 1, len(array)):
#             if array[j] < array[i]:
#                 count += 1
#         smallerArray.append(count)
#     print(smallerArray)


# def test(array):
#     if len(array) == 0:
#         return []

#     endIdx = len(array) - 1
#     bst = SpecialBST(array[endIdx], endIdx, 0)
#     for i in reversed(range(len(array) - 1)):
#         bst.insert(array[i], i, 0)

#     countArray = array[:]
#     rSCs = getRSCs(bst, countArray)
#     return countArray

# def getRSCs(bst, array):
#     if bst is None:
#         return
#     array[bst.idx] = bst.numSmallerAtInsertionTime
#     getRSCs(bst.left, array)
#     getRSCs(bst.right, array)




# class SpecialBST:
#     def __init__(self, value, idx, numSmallerAtInsertionTime):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.leftSubtreeSize = 0
#         self.idx = idx
#         self.numSmallerAtInsertionTime = numSmallerAtInsertionTime
    
#     def insert(self, value, idx, numSmallerAtInsertionTime=0):
#         if value < self.value:
#             self.leftSubtreeSize += 1
#             if self.left is None:
#                 self.left = SpecialBST(value, idx, numSmallerAtInsertionTime)
#             else:
#                 self.left.insert(value, idx, numSmallerAtInsertionTime)
#         else:
#             numSmallerAtInsertionTime += self.leftSubtreeSize
#             if value > self.value:
#                 numSmallerAtInsertionTime += 1
#             if self.right is None:
#                 self.right = SpecialBST(value, idx, numSmallerAtInsertionTime)
#             else:
#                 self.right.insert(value, idx, numSmallerAtInsertionTime)






def rightSmallerThan(array):
    if len(array) == 0:
        return []

    smallerThanRightArray = array[:]
    endIdx = len(array) - 1
    bst = BST(array[endIdx])
    smallerThanRightArray[endIdx] = 0
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i, smallerThanRightArray)

    return smallerThanRightArray

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.leftSubtreeSize = 0

    def insert(self, value, idx, smallerThanRightArray, numSmallerAtInsertionTime=0):
        if value < self.value:
            self.leftSubtreeSize += 1
            if self.left is None:
                self.left = BST(value)
                smallerThanRightArray[idx] = numSmallerAtInsertionTime
            else:
                self.left.insert(value, idx, smallerThanRightArray, numSmallerAtInsertionTime)
        else:
            numSmallerAtInsertionTime += self.leftSubtreeSize
            if value > self.value:
                numSmallerAtInsertionTime += 1
            if self.right is None:
                self.right = BST(value)
                smallerThanRightArray[idx] = numSmallerAtInsertionTime
            else:
                self.right.insert(value, idx, smallerThanRightArray, numSmallerAtInsertionTime)


array = [8, 5, 11, -1, 3, 4, 2]
gg = [
    991,
    -731,
    -882,
    100,
    280,
    -43,
    432,
    771,
    -581,
    180,
    -382,
    -998,
    847,
    80,
    -220,
    680,
    769,
    -75,
    -817,
    366,
    956,
    749,
    471,
    228,
    -435,
    -269,
    652,
    -331,
    -387,
    -657,
    -255,
    382,
    -216,
    -6,
    -163,
    -681,
    980,
    913,
    -169,
    972,
    -523,
    354,
    747,
    805,
    382,
    -827,
    -796,
    372,
    753,
    519,
    906
  ]
