class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def validateBST(tree):
    return recursiveHelper(tree, float("-inf"), float("inf"))


def recursiveHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value > maxValue:
        return False
    validateLeftBranch = recursiveHelper(tree, minValue, tree.value)
    validateRightBranch = recursiveHelper(tree, tree.value, maxValue)
    return validateLeftBranch and validateRightBranch