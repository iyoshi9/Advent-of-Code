
# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
# What is the sum of the IDs of those games?
file = open("Day_2.txt",'r')
sum = 0
for entry in file:
    line = entry.strip().split()
    if "red" <= 12 and "green" <= 13 and "blue" <= 14 :
        continue
    sum = sum + int(line[1])
print(sum)