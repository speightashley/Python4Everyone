name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')

emails = {}

for line in handle:
    if line.startswith("From "):
        line = line.split()[1]

        emails[line] = emails.get(line, 0) + 1

bigsender = None
count = None

for key, value in emails.items():
    if bigsender is None or value > count:
        bigsender = key
        count = value

print(bigsender, count)



