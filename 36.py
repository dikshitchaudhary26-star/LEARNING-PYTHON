# MATCH - CASE (LIKE SWITCH CASE IN C/C++)

marks = float(input("ENTER MARKS :"))

match marks:

    case n if marks >= 90 and marks <= 100 :
        print("A")
    case n if marks >= 80 and marks < 90 :
        print("A-")
    case n if marks >= 70 and marks < 80 :
        print("B")
    case n if marks >= 60 and marks < 70 :
        print("B-")
    case n if marks >= 50 and marks < 60 :
        print("C")
    case n if marks >= 40 and marks < 50 :
        print("C-")
    case n if marks >= 0 and marks < 40 :
        print("FAIL")
    case _ :
        print("INVALID MARKS")
