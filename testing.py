import re

name = input("Enter a file")

if len(name) < 1:
    name = "regex_sum_1685344.txt"

numlist = list()

with open(name, 'r') as file:
    for line in file:
        y = re.findall('[0-9]+', line)
        if len(y) != 1:
            continue
        num = float(y[0])
        numlist.append(num)

print(numlist)
