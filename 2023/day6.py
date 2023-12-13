

# Part 1
file = open('Day_6.txt', 'r')
hold_b = 0
time = 0 # maximum time
if hold_b == 0:
    dist = 0
elif hold_b == time:
    dist = 0
else:
    dist = (hold_b * time) - hold_b
# Afterwards check if it is better than the record distance
# race_1 * race_2 * race_3 * race_4