from collections import deque # Check if state is valid 
def is_valid(m_left, c_left, m_right, c_right):     
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0): 
        return False     
    if (m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3): 
        return False     
    if (m_left > 0 and m_left < c_left): 
        return False     
    if (m_right > 0 and m_right < c_right): 
        return False     
    return True 
def bfs(): 
    # (m_left, c_left, boat, m_right, c_right)     
    start = (3, 3, 0, 0, 0)     
    goal = (0, 0, 1, 3, 3) 
 
    queue = deque([(start, [])])     
    visited = set() 
 
    while queue: 
        (state, path) = queue.popleft()         
        m_left, c_left, boat, m_right, c_right = state 
 
        if state in visited:             
            continue         
        visited.add(state)         
        if state == goal: 
            return path + [state] 
 
        # Possible moves         
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)] 
 
        for m, c in moves: 
            if boat == 0:  # Boat on left                 
                new_state = (m_left-m, c_left-c, 1,                              
                            m_right+m, c_right+c)             
            else:  # Boat on right                 
                new_state = (m_left+m, c_left+c, 0,                              
                             m_right-m, c_right-c) 
 
            if is_valid(*new_state[:2], *new_state[3:]):                 
                queue.append((new_state, path + [state])) 
 
    return None 
solution = bfs() 
print("Solution Steps:") 
for step in solution: 
    print(step)
