# Linked List - It is a data structure which conists of nodes which are connected by pointers
# There are for types of Linked list
# 1) Singly slinked list
# 2) Circular Singly linked list
# 3) Doubly Linked List
# 4) Circular doubly linked list


# Implement Singly Linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def add_node(self, data):
        if self.head is None:
            self.head=node(data)
            return
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def remove_node(self):
        if (self.head).next==None:
            self.head=None
            return
        first=self.head
        sec=first.next
        while sec.next!=None:
            first=sec
            sec=sec.next
        first.next=None

    def length(self):
        total=0
        cur=self.head
        while cur.next!=None:
            total+=1
            cur=cur.next
            
        return total

    def display(self):
        lis=[]
        if self.head is None:
            return lis
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            lis.append(cur.data)         
        return lis

obj=linked_list()

obj.display()

obj.add_node(5)
obj.add_node(8)
obj.add_node(11)
print(obj.length())
print(obj.display())


obj.remove_node()
print(obj.display())
