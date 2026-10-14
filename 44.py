#CHECK A PRIME NUMBER (POSITIVE NUMBER > 2)

num = int(input("ENTER THE NUMBER :"))

a = 1 # IS PRIME

for i in range(2,num):

    if num%i == 0:
        a = 0
        break

    a = 1

if a == 1:
    print(f"{num} IS A PRIME NUMBER")

if a == 0:
    print(f"{num} IS NOT A PRIME NUMBER")