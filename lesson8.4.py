fname = input("Enter file name: ")
fh = open(fname, 'r')
lst = list()

for line in fh:
    line = line.split()
    for word in line:
        if word in lst:
            continue
        else:
            lst.append(word)



print(sorted(lst))

