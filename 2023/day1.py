import re
file = open("Day_1.txt",'r')
pattern = re.compile('[a-z]')
for line in file.readlines():
    if pattern.match(line):
        sub = pattern.sub("",line)
        print(sub)           
for line in sub:
    