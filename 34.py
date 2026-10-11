#FIND MAXIMUM NUMBER OUT OF THREE USING NESTED CONDITIONS

num1 = float(input("ENTER NUMBER 1 :"))
num2 = float(input("ENTER NUMBER 2 :"))
num3 = float(input("ENTER NUMBER 3 :"))

if num1 > num2:
    if(num2>num3):
        print("VALUE OF NUMBER 1 IS MAXIMUM")

if num2 > num3 :
    if num3 > num1 :
        print("VALUE OF NUMBER 2 IS MAXIMUM")

else:
    print("VALUE OF NUMBER 3 IS MAXIMUM")
    

