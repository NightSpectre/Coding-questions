# height of tree

# do post order traversal, keep saving each variable in counter

def maxDepth(node):
    if node is None:
        return 0
        
    lDepth = maxDepth(node.left)
    rDepth = maxDepth(node.right)

    if (lDepth > rDepth):
        return lDepth+1
    else:
        return rDepth+1