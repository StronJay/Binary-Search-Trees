class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        node = self
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right

    def contains(self, value):
        node = self
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    def remove(self, value, pNode=None):
        node = self
        while node is not None:
            if value < node.value:
                pNode = node
                node = node.left
            elif value > node.value:
                pNode = node
                node = node.right
            else:
                if node.left is not None and node.right is not None:
                    node.value = node.right.getMinValue()
                    node.right.remove(node.value, node)
                elif pNode is None:
                    if node.left is not None:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right is not None:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:
                        pass
                elif pNode.left == node:
                    pNode.left = node.left if node.left is not None else node.right
                elif pNode.right == node:
                    pNode.right = node.left if node.left is not None else node.right
                break

    def getMinValue(self):
        node = self
        while node.left is not None:
            node = node.left
        return node.value