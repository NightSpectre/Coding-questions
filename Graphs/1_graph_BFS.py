# Graph - It is a data structure which consists of finite number of nodes which are connected 
#         with edges

# Graphs in python can be implemented using defaultdict
# BFS- It can be implemented using queue
from collections import defaultdict
from collections import deque

def BFS(starting_node,graph):
    visited = [False] * (len(graph.keys()))
    q=deque([])
    q.append(starting_node)
    visited[starting_node]=True
    while q:
        starting_node = q.popleft()
        print(starting_node, end=" ")
        for i in graph[starting_node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
        
    
graph=defaultdict(list)
graph[0].append(1)
graph[0].append(2)
graph[1].append(2)
graph[2].append(0)
graph[2].append(3)
graph[3].append(3)

BFS(2,graph)
