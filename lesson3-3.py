while True:
    grade = float(input("What is your grade? "))

    if grade > 1.0 or grade < 0.0:
        print("Enter a number between 0 and 1")
        continue
    if grade >= 0.9:
        print("A")
        break
    elif grade >= 0.8:
        print("B")
        break
    elif grade >= 0.7:
        print("C")
        break
    elif grade >= 0.6:
        print("D")
        break
    else:
        print("F")
        break


