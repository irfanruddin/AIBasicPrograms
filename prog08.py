""" Program 8 """
from collections import deque
def print_path(parent, state): 
    path = []     
    while state in parent:         
        path.append(state)         
        state = parent[state]     
    path.append((0,0))    
    path.reverse() 
    for step in path:         
        print(step)
 
def water_jug_bfs(cap1, cap2, target): 
    visited = set()     
    queue = deque()     
    queue.append((0, 0))     
    visited.add((0, 0)) 
    parent = {} 
     
    while queue: 
        jug1, jug2 = queue.popleft() 
         
        if jug1 == target or jug2 == target:             
            print("Solution found:")             
            print_path(parent, (jug1, jug2))             
            return 
        next_states = [            
            (cap1, jug2),  # Fill jug1             
            (jug1, cap2),  # Fill jug2 
            (0, jug2),     # Empty jug1 
            (jug1, 0),     # Empty jug2 
            # Pour jug1 -> jug2             
            (jug1 - min(jug1, cap2 - jug2),              
            jug2 + min(jug1, cap2 - jug2)),             
            # Pour jug2 -> jug1             
            (jug1 + min(jug2, cap1 - jug1),              
            jug2 - min(jug2, cap1 - jug1)) 
        ] 
        for state in next_states:             
            if state not in visited:                 
                visited.add(state)                 
                queue.append(state)                 
                parent[state] = (jug1, jug2)     

    print("No solution possible.") 
water_jug_bfs(4, 3, 2) 
