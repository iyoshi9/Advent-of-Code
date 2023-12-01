

list_of_lines = open('Day_1.txt', 'r')
list_of_lines = list_of_lines.readlines()
data_list = []
for entry in list_of_lines:
    line_cleaned = entry.strip().split()
    if len(line_cleaned) == 0 or line_cleaned[0] == '%':
        continue
    entry.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvxyz'})
    data_list.append(entry)
print(data_list)