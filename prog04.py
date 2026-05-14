""" program 4 """   
import heapq  
def a_star(graph, start, goal, heuristic):     
    open_list = []     
    heapq.heappush(open_list, (0, start)) 
    g_cost = {start: 0} 
    parent = {start: None} 
     
    while open_list: 
        current_f, current_node = heapq.heappop(open_list) 
        if current_node == goal:            
            path = []             
            while current_node: 
                path.append(current_node)                 
                current_node = parent[current_node] 
            return path[::-1] ,g_cost[goal]  
         
        for neighbour, cost in graph[current_node]:             
            new_g = g_cost[current_node] + cost 
            if neighbour not in g_cost or new_g < g_cost[neighbour]: 
                g_cost[neighbour] = new_g                 
                f_value = new_g + heuristic[neighbour]                 
                heapq.heappush(open_list, (f_value, neighbour))                 
                parent[neighbour] = current_node 
    return None 
graph = { 
    'A': [('B', 1), ('C', 3)], 
    'B': [('D', 3), ('E', 1)], 
    'C': [('F', 5)], 
    'D': [], 
    'E': [('F', 2)], 
    'F': [] 
}
heuristic = { 
    'A': 5, 
    'B': 3,     
    'C': 4, 
    'D': 2, 
    'E': 1, 
    'F': 0 
} 
start_node = 'A' 
goal_node = 'F' 
path,cost = a_star(graph, start_node, goal_node, heuristic) 
print("Shortest Path:", " -> ".join(path)) 
print("Total cost :",cost)
