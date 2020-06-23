class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTravese(tree, array):
    if tree is not None:
        postOrderTravese(tree.left, array)
        postOrderTravese(tree.right, array)
        array.append(tree.value)
    return array