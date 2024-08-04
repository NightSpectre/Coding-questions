# Stacks - It is a data structure in which elements which are inserted at last are the ones to 
#          be rmoved first

# in python it can be achieved by deque

from collections import deque

l=deque([])
l.append(3)
l.append(5)
l.append(8)               # in deque we can use appendleft also
print(l)

l.pop()
print(l)