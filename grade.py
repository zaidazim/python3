score = input("Enter your score: ")
x = float(score)
if x > 1.0 or x < 0.0:
    print("Value out of range")
    quit()
else:
    if x>= 0.9:
        grade = "A"
    elif x>= 0.8:
        grade = "B"
    elif x>= 0.7:
        grade = "C"
    elif x>= 0.6:
        grade = "C"
    else:
        grade = "F"
print(grade)
