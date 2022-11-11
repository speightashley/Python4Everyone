# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, "r")
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        if line.startswith("X-DSPAM-Confidence:"):
            pos = line.find(" ")
            trimmed = line[pos:]
            clean = trimmed.strip()
            total = total + float(clean)
            count = count + 1
            
print("Average Spam Confidence: ", + total / count)