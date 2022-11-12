name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')

emptydict = {}

for line in handle:
    if line.startswith("From "):
        line = line.split()
        numbers = line[5].split(":")
        tup = numbers[0]
        emptydict[tup] = emptydict.get(tup, 0) + 1

newlist = list()

for k, v in emptydict.items():
    newtup = (k, v)
    newlist.append(newtup)

newlist = sorted(newlist)

for val, key in newlist:
    print(val, key)
