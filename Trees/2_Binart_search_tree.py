# Binary Search Tree

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
                
    def insert(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self._insert(self.root,data)

    def _insert(self,pre_node,data):
        new_node=node(data)
        
        cur_node=self.root
        if data<cur_node.data:
            if cur_node.left is None:
                cur_node.left=new_node
            else:
                self._insert(cur_node.left,data)
        else:
            if cur_node.right is None:
                cur_node.right=new_node
            else:
                self._insert(cur_node.right,data)
    

    def display(self):
        if self.root is None:
            return None
        else:
            self._display(self.root)


    def _display(self,pre_node):
        if pre_node is None:
            return
        self._display(pre_node.left)
        print(pre_node.data)
        self._display(pre_node.right)


object=BST()
object.insert(12)
object.insert(4)
object.insert(16)

object.display()
