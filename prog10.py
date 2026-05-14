""" Program 10 """

monkey_position = "door" 
box_position = "window" 
banana_position = "center" 
monkey_on_box = False 
has_banana = False 
print("Initial State:") 
print("Monkey at -", monkey_position) 
print("Box at -", box_position) 
print("Banana at -", banana_position) 
print() 
 
# Step 1: Monkey goes to box 
monkey_position = "window" 
print("Monkey moves to window") 
 
# Step 2: Monkey pushes box to center 
box_position = "center" 
monkey_position = "center" 
print("Monkey pushes box to center") 
 
# Step 3: Monkey climbs the box 
monkey_on_box = True 
print("Monkey climbs the box") 
 
# Step 4: Monkey grabs banana 
if monkey_on_box and box_position == banana_position: 
    has_banana = True     
    print("Monkey grabs the banana 🍌") 
print()
print("goal state reached.")
print("Has banana:",has_banana)
