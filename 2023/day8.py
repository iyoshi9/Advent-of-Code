

# Part 1
file = open('Day_8.txt', 'r')
### Get to ZZZ from AAA with left/right instructions
# Find string "AAA" afterwards doing either left or right with a tuple to then look for the next string. If no more instructions then repeat from the start with the instructions
start = "AAA"
L = (1,0)
R = (0,1)