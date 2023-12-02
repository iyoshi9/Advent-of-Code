import re
file = open("Day_1.txt",'r')
pattern = re.compile('[a-z]')
for line in file.readlines():
    if pattern.match(line):
        sub = pattern.sub("",line)
        print(sub)           
for line in sub:
    pass
# Need to get my code to look at the first and last number and put them together. Lastly get the sum of all numbers.