def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        overtime = h - 40
        overtimerate = r * 1.5
        overtimetotal = overtime * overtimerate
        total = 40 * r + overtimetotal
        return total


def computepayalt(h, r):
    FLATRATE = 40
    if h <= FLATRATE:
        return h * r
    else:
        overtime = h % FLATRATE * 1.5
        return (overtime * r) + (FLATRATE * r)



print(45 % 40)
hrs = float(input("Enter Hours:"))
rate = float(input("what is your rate? "))
p = computepayalt(hrs, rate)
print("Pay", p)

