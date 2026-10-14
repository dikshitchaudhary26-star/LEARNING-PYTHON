
# ARMSTRONG NUMBER

num1 = int(input("ENTER A NUMBER: "))

total = 0
num2 = num1

while num2 > 0:
    digit = num2 % 10
    total = total + digit ** 3
    num2 = num2 // 10

if total == num1:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
