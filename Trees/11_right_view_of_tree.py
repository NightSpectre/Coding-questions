# right view of the tree
def rightSideView(self, root) -> List[int]:
    res=[]
    
    def rightside(root, max_height, level):
        if root is None:
            return
        if max_height[0]<level:
            max_height[0]=level
            res.append(root.data)
        rightside(root.right,max_height,level+1)
        rightside(root.left,max_height,level+1)
    max_height=[0]
    rightside(root,max_height,1)
    return res