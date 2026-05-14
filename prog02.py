
""" program 2 """

from collections import deque 
  
def bfs(graph, start_node): 
    visited = set()               
    queue = deque([start_node])  
    visited.add(start_node) 
     
    while queue: 
        node = queue.popleft()           
        print(node, end=" ") 
                 
        for neighbour in graph[node]:             
            if neighbour not in visited:                 
                visited.add(neighbour) 
                queue.append(neighbour) 
 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'],
    'D': [], 
    'E': ['F'], 
    'F': [] 
    
} 
 
print("BFS Traversal:")
bfs(graph, 'A') 
