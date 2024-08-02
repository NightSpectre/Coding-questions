# Queue - It is a data structure in which elements which are inserted at first are the ones to 
#          be removed first

# in python it can be achieved by deque

l=deque([])
l.append(3)
l.append(5)
l.append(8)
print(l)

l.popleft()
print(l)