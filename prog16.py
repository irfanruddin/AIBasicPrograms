
facts = { 
    "Man(Socrates)" 
} 
# Rule: If Man(X) then Mortal(X) 
def apply_rule(facts):     
    new_facts = set()     
    for fact in facts:         
        if fact.startswith("Man("):             
            person = fact[4:-1]  # Extract name inside Man()             
            new_facts.add(f"Mortal({person})")     
    return new_facts
 
print("Initial Facts:", facts) 
# Apply rule 
inferred = apply_rule(facts) 
facts.update(inferred) 
print("Inferred Facts:", inferred) 
print("Final Facts:", facts) 