fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname, 'r')
count = 0
emails = []

for line in fh:
    if line.startswith('From '):
        line = line.split()
        emails.append(line[1])
        count = count + 1
    else:
        continue

for email in emails:
    print(email)
    
print("There were", count, "lines in the file with From as the first word")
