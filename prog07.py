""" Program 7 """
from collections import deque
def print_state(state):
    for i in range(0,9,3):
        print(state[i],state[i+1],state[i+2])
    print()
def get_neighbours(state):
    neighbours = []
    zero_idx = state.index(0)
    row = zero_idx // 3
    col = zero_idx % 3
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr,dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx],new_state[zero_idx]
            neighbours.append(tuple(new_state))
    return neighbours
def bfs_8_puzzle(start,goal):
    queue = deque()
    visited = set()
    queue.append((start,[start]))
    visited.add(start)
    while queue:
        current,path = queue.popleft()
        if current == goal:
            return path
        for nxt in get_neighbours(current):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt,path + [nxt]))
    return None
start_state = (
    1,2,3,
    4,0,6,
    7,5,8
)
goal_state =(
    1,2,3,
    4,5,6,
    7,8,0
)
solution_path = bfs_8_puzzle(start_state,goal_state)
if solution_path is None:
    print("No solution found")
else:
    print("solution found. Number of moves = ",len(solution_path)-1)
    print("\nSteps:")
    step_no = 0
    for state in solution_path:
        print("Step",step_no)
        print_state(state)
        step_no +=1
