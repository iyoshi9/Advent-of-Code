
# Part 1
file = open("Day_4.txt",'r')
points = 0
score = 0
for entry in file:
    line = entry.strip().split()
    for x in range(2,12):
        for y in range(13,38):
            if line[x] == line[y]:
                score = score + 1
    if score == 0:
        continue
    elif score == 1:
        points = points + 1
    elif score == 2:
        points = points + 2
    elif score > 2:
        points = points + pow(2,score-1)
    score = 0
print(points)    


# Part 2
file = open("Day_4.txt",'r')
scratch = 0
for entry in file:
    line = entry.strip().split()