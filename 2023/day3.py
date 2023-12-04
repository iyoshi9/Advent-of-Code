
# Part 1
file = open("Day_3.txt",'r')
sum = 0

for entry in file:
    line = entry.strip().split() # Not sure if necessary
    # if number is adjacent to a symbol (that is not .) then put it in sum
    sum = sum + "number"
print(sum)