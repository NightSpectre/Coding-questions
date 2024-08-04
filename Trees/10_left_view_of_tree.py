# left view of the tree

def leftSideView(self, root) -> List[int]:
    res=[]
    
    def leftside(root, max_height, level):
        if root is None:
            return
        if max_height[0]<level:
            max_height[0]=level
            res.append(root.data)
        leftside(root.left,max_height,level+1)
        leftside(root.right,max_height,level+1)
    max_height=[0]
    leftside(root,max_height,1)
    return res