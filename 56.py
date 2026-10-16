#PROBLEM - LARGEST ELEMENT IN THE LIST

marks = [1,2,3,4,5]
max = -1
for ele in marks:
    if ele > max:
        max = ele

print(f"LARGEST NUMBER IS :{max}")