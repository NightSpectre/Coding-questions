# Inorder Traversal
# left -> root -> right

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraversal(node):
    if node is None:
        return
    inorderTraversal(node.left)
    print(node.data, end=' ')
    inorderTraversal(node.right)