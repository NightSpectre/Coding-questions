# Circular doubly lined list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class cir_doubly_ll:
    def __init__(self):
        self.head=None

    def add_node(self,data):
        if self.head is None:
            self.head=node(data)
            (self.head).next=self.head
            (self.head).prev=self.head
            return
        new_node=node(data)
        first=self.head
        sec=first.next
        while sec is not self.head:
            first=sec
            sec=sec.next
        first.next=new_node
        new_node.prev=first
        new_node.next=self.head
        (self.head).prev=new_node

    def remove_node(self):
        lis=[]
        if self.head is None or (self.head).next is self.head:
            return lis
        first=self.head
        sec=(self.head).next
        while sec.next is not self.head:
            first=sec
            sec=sec.next
        first.next=self.head
        (self.head).prev=first

    def display(self):
        lis=[]
        if self.head is None:
            return lis
        if (self.head).next is self.head:
            lis.append((self.head).data)
            return lis
        first=self.head
        sec=(self.head).next
        lis.append(first.data)
        lis.append(sec.data)
        while sec.next is not self.head:
            first=sec
            sec=sec.next
            lis.append(sec.data)
        return lis

obj=cir_doubly_ll()

obj.add_node(14)
obj.add_node(9)
print(obj.display())

obj.add_node(78)
obj.add_node(3)
print(obj.display())

obj.remove_node()
obj.display()
        