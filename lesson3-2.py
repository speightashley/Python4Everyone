hrs = input("Enter Hours: ")
h = float(hrs)

rph = input("What is your hourly rate? ")
r = float(rph)

OVERTIME = h - 40

print(OVERTIME)

if h <= 40:
    print("total pay = " + str(h * r))
elif h > 40:
    basic = r * 40
    overtime = (r * 1.5) * OVERTIME
    print("Total pay is " + str(overtime + basic))




