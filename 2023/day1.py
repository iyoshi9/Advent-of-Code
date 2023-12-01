import re

list_of_lines = open('Day_1.txt', 'r')
list_of_lines = list_of_lines.readlines()
pattern = re.compile('[abcdefghijklmnopqrstuvwxyz]')
data_list = []
data_list2 = []
for entry in list_of_lines:
    line_cleaned = entry.strip().split()
    if len(line_cleaned) == 0 or line_cleaned[0] == '%':
        continue
    number = pattern.split(entry)
    data_list.append(number)
print(data_list)