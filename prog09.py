"""  Program 9 """
import itertools 
 
def travelling_salesman_problem(cost_matrix, start): 
    n = len(cost_matrix)  #total cities     
    vertices = list(range(n))     
    vertices.remove(start) 
 
    min_path = float('inf')     
    best_route = [] 
 
    # Generate all possible permutations of cities     
    for perm in itertools.permutations(vertices): 
        current_cost = 0         
        k = start 
 
        # Calculate cost of current permutation         
        for j in perm: 
            current_cost += cost_matrix [k][j] 
            k = j 
 
        # Add cost to return to starting city         
        current_cost += cost_matrix [k][start] 
 
        # Update minimum cost         
        if current_cost < min_path:             
            min_path = current_cost 
            best_route = (start,) + perm + (start,) 
 
    return min_path, best_route 
 
 
# Example 
cost_matrix = [     [0, 10, 15, 20], 
    [10, 0, 35, 25], 
    [15, 35, 0, 30], 
    [20, 25, 30, 0] 
] 
 
start_city = 0
min_cost, route = travelling_salesman_problem(cost_matrix, start_city) 
print("Minimum Cost:", min_cost) 
print("Best Route:", route) 
 
