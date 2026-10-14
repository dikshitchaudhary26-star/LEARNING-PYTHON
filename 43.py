# FIBONACCI SERIES

terms = int(input("ENTER THE NUMBER OF TERMS: "))

a = 0
b = 1

for i in range(terms):
    print(a)
    c = a + b
    a = b
    b = c
