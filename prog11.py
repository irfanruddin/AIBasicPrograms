import math 
 
# Alpha-Beta function 
def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta): 
 
    # If leaf node reached     
    if depth == 3: 
        return values[nodeIndex] 
 
    if maximizingPlayer:         
        maxEval = -math.inf         
        for i in range(2): 
            eval = alphabeta(depth + 1, nodeIndex * 2 + i,False, values, alpha, beta)             
            maxEval = max(maxEval, eval)             
            alpha = max(alpha, eval) 
 
            # Beta Cut-off             
            if beta <= alpha: 
                break         
            return maxEval 
    else: 
        minEval = math.inf         
        for i in range(2): 
            eval = alphabeta(depth + 1, nodeIndex * 2 + i,True, values, alpha, beta)             
            minEval = min(minEval, eval)             
            beta = min(beta, eval) 
 
            # Alpha Cut-off             
            if beta <= alpha: 
                break         
            return minEval 
 
 
# Leaf node values (example game tree) 
values = [3, 5, 6, 9, 1, 2, 0, -1] 
 
result = alphabeta(0, 0, True, values, -math.inf, math.inf) 
print("Optimal value:", result) 
 
