# Postorder Traversal
# left-> right -> root

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorderTraversal(node):
    if node is None:
        return
    postorderTraversal(node.left)
    postorderTraversal(node.right)
    print(node.data, end=' ')