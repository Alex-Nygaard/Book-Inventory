# CodinGamePuzzles solutions

## "Onboarding" Puzzle
```.py
# game loop
while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print

    # Enter the code here
    
    
    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)
```


## "Descent" Puzzle
```.py
import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    mountain_h = []
    for i in range(8):
        mountain_h.append(int(input()))  # represents the height of one mountain.
        
    # The index of the mountain to fire on.
    
    print(f"{mountain_h.index(max(mountain_h))}")
```


## "Power of Thor Episode 1" Puzzle
```.py
# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

current_x, current_y = initial_tx, initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    move_string = ""
    
    # Checks Y values
    if light_y > current_y:
        move_string = "S"
        current_y += 1
    elif light_y < current_y:
        move_string = "N"
        current_y -= 1
        
    # Checks X values
    if light_x > current_x:
        move_string += "E"
        current_x += 1
    elif light_x < current_x:
        move_string += "W"
        current_x -= 1

    # Prints the direction
    print(move_string)
```


## "There is no spoon - Episode 1" Puzzle
```.py
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

lines = []
for i in range(height):
    lines.append(input())  # width characters, each either 0 or .

#print(lines)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for line_index in range(height): # Vertical line index
    for node_index in range(width): # Horizontal position index
        
        # Default values, if no neighbors are found
        x2 = -1
        y2 = -1
        
        x3 = -1
        y3 = -1
        
        # Checks the current node
        if lines[line_index][node_index] == "0":
            
            # Coordinates of that node
            x1 = node_index
            y1 = line_index
            
            # Finds nearest horizontal neighbor 
            # (checks from the next neighbor of the node until the width)
            for i in range(node_index+1, width):
                if lines[line_index][i] == "0":
                    x2 = i
                    y2 = line_index
                    break
            
            # Finds nearest vertical neighbor 
            # (checks from the next neighbor of the node until the height)
            for i in range(line_index+1, height):
                if lines[i][node_index] == "0":
                    x3 = node_index
                    y3 = i
                    break
                    
            # Prints all coordinates
            print(x1, y1, x2, y2, x3, y3)
```
