class AOStar:     
    def __init__(self, graph, heuristic): 
        self.graph = graph          
        self.heuristic = heuristic
        self.solution = {}       
 
    def ao_star(self, node):                  
        if node not in self.graph or not self.graph[node]: 
            return self.heuristic[node] 
 
        min_cost = float('inf') 
        best_children = None 
          
        for group in self.graph[node]:             
            cost = 0             
            for child, weight in group: 
                cost += weight + self.ao_star(child) 
 
            if cost < min_cost:                 
                min_cost = cost 
                best_children = group 
 
        self.heuristic[node] = min_cost 
        self.solution[node] = best_children 
 
        return min_cost 
 
    def print_solution(self, node):         
        if node in self.solution:             
            for child, _ in self.solution[node]: 
                print(node, "->", child) 
                self.print_solution(child) 
 
 
graph = { 
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],  # A → (B AND C) OR D 
    'B': [[('E', 1)], [('F', 1)]], 
    'C': [[('G', 1)]], 
    'D': [], 
    'E': [], 
    'F': [], 
    'G': [] 
} 
 
heuristic = { 
    'A': 10, 
    'B': 4,     'C': 2, 
    'D': 3, 
    'E': 1, 
    'F': 2, 
    'G': 2 
} 
 
ao = AOStar(graph, heuristic) 
 
ao.ao_star('A') 
 
print("Solution Graph:") 
ao.print_solution('A') 
