# DFS- It can be implemented using recursion (but usually stacks)
from collections import defaultdict
from collections import deque

visited = []
def DFS(starting_node,graph):
    
    print(starting_node, end=" ")
    visited.append(starting_node)
    for i in graph[starting_node]:
        if i not in visited:
            DFS(i,graph)
    
graph=defaultdict(list)
graph[0].append(1)
graph[0].append(2)
graph[1].append(2)
graph[2].append(0)
graph[2].append(3)
graph[3].append(3)

DFS(2,graph)