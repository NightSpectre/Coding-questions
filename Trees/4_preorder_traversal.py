# Preorder Traversal
# root -> left-> right

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorderTraversal(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorderTraversal(node.left)
    preorderTraversal(node.right)
    