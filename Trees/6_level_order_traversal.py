# level order traversal

# There are 2 ways to implement this
# 1) Take a queue, do preorder traversal and add each elements to queue and print first element
# 2) Find the height of the tree, print nodes in each level

def levelOrder(root) -> List[List[int]]:
        queue=[root]
        res=[]
        if root is None:
            return []
        while queue:
            l=len(queue)
            t=[]
            while l!=0:
                elem=queue.pop(0)
                t.append(elem.val)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
                l-=1
            res.append(t)
        return res