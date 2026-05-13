 
def objective(x): 
    return -x**2 + 4*x   # Maximum at x = 2 
 
def hill_climbing(start, step_size=1): 
    current = start     
    while True: 
        neighbor1 = current + step_size         
        neighbor2 = current - step_size 
 
        # Choose the best neighbor         
        best_neighbor = current         
        if objective(neighbor1) > objective(best_neighbor): 
            best_neighbor = neighbor1         
        if objective(neighbor2) > objective(best_neighbor): 
            best_neighbor = neighbor2 
 
        # If no improvement, stop         
        if best_neighbor == current: 
            return current         
        current = best_neighbor 
        
start = 0 
solution = hill_climbing(start) 
print("Best solution x =", solution) 
print("Maximum value =", objective(solution))