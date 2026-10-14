# FACTORIAL OF THE NUMBER

num = int(input("ENTER THE NUMBER TO FIND IT'S FACTORIAL :"))

product = 1

for i in range (1,num+1):
    product = product*i

print(f"THE FACTORIAL OF {num} is : {product}")
