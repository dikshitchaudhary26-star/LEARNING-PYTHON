#GRADE CALCULATOR

marks = float(input("ENTER MARKS :"))

if marks>100 or marks < 0:
    print("INVALID MARKS")
elif marks >= 90 and marks <= 100 :
    print("A")
elif marks >= 80 and marks < 90 :
    print("B")
elif marks >= 70 and marks < 80 :
    print("C")
elif marks >= 40 and marks < 70 :
    print("promoted")
else :
    print("FAILED")

