import re

# Part 1
# Two ideas that both not really working
list_of_lines = open('Day_1.txt', 'r')
#pattern = re.compile('[a-z]')
#data_list = []
#for entry in list_of_lines:
#    number = pattern.split(entry)
#    data_list.append(number)
#print(data_list)    
pattern = re.compile(".*[0-9]")
for entry in list_of_lines:
    number = pattern.match(entry).group()
    print(number)

        
# Need to get my code to look at the first and last number and put them together. Lastly get the sum of all numbers.