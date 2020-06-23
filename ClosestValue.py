def getClosestValue(tree, target):
    node = tree
    closestValue = node.value
    while node is not None:
        if abs(target - node.value) < abs(target - closestValue):
            closestValue = node.value
        if target < node.value:
            node = node.left
        elif target > node.value:
            node = node.right
        else:
            break
    return closestValue