# Simple Forward Chaining Implementation  
# Knowledge Base (Rules) # Format: (conditions, conclusion) 

rules = [ 
    (["A", "B"], "C"), 
    (["C"], "D"), 
    (["D"], "E") 
]

# Initial Facts 

facts = ["A", "B"] 
def forward_chaining(rules, facts): 
    inferred = True 
    while inferred:         
        inferred = False         
        for conditions, conclusion in rules:             
            # Check if all conditions are in facts             
            if all(condition in facts for condition in conditions):                 
                if conclusion not in facts:                     
                    facts.append(conclusion)                     
                    print("Inferred:", conclusion)                     
                    inferred = True 
 
    return facts 
 
print("Initial Facts:", facts) 
final_facts = forward_chaining(rules, facts) 
print("Final Facts:", final_facts) 
