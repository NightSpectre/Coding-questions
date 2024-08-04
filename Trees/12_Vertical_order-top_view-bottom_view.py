# Vertical Order traversal
# Top view 
# Bottom view

# We can do this using hashing and level order traversal
# 1. To maintain a hash for the branch of each node.
# 2. Traverse the tree in level order fashion.
# 3. In level order traversal, maintain a queue which holds, node and its Horizontal Distance (HD).
# * pop from queue.
# * add this node’s HD as key and data as value in the hash.
# * if this node hash left child, insert it into the queue with HD as HD – 1.
# * if this node hash right child, insert it into the queue with HD as HD + 1
# 4. Finally traverse

def get_order(root, hd, m, min_hd, max_hd):
    if root is None:
        return

    if hd not in m:
        m[hd] = []
    m[hd].append(root.key)

    min_hd[0] = min(min_hd[0], hd)
    max_hd[0] = max(max_hd[0], hd)

    get_order(root.left, hd - 1, m, min_hd, max_hd)

    get_order(root.right, hd + 1, m, min_hd, max_hd)

def print_order(root):
    m = {}
    min_hd = [0]
    max_hd = [0]

    get_order(root, 0, m, min_hd, max_hd)
