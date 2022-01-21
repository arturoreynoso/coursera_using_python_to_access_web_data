import re 
file = open("regex_sum_1194078.txt", "r")

count = 0
for line in file: 
    y = re.findall("[0-9]+", line)
    y = [int(i) for i in y]
    count += sum(y)

print(count)

