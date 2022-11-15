import re

name = input("Enter a file name")
if len(name) < 1:
    name = "regex_sum_1685344.txt"

file = open(name, 'r')
y = list()
total = 0

for line in file:
    # print(line)
    x = re.findall('[0-9]+', line)
    y = y + x

for num in y:
    total += int(num)

print(total)
