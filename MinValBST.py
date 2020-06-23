# THIS ONLY WORKS WITH NON-EMPTY SORTED ARRAY OF DISTINCT!!!! INTEGERS

def minValBst(array):
    return construct(array, 0, len(array) - 1)


def construct(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = construct(array, startIdx, midIdx - 1)
    bst.right = construct(array, midIdx + 1, endIdx)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# def test(array):
#     return construct(array, None, 0, len(array) - 1)

# def construct1(array, tree, startIdx, endIdx):
#     if startIdx > endIdx:
#         return
#     midIdx = (startIdx + endIdx) // 2
#     addValue = array[midIdx]
#     if tree is None:
#         tree = BST(addValue)
#     else:
#         tree.insert(addValue)
#         construct1(array, tree, startIdx, midIdx - 1)
#         construct1(array, tree, midIdx + 1, endIdx)
#     return tree