
# LIST COMPREHENSION
# PRINT FIZZ / BUZZ / FIZZBUZZ

l1 = ["FIZZBUZZ" if i % 3 == 0 and i % 5 == 0 else "FIZZ" if i % 3 == 0 else "BUZZ" if i % 5 == 0 else i for i in range(1, 21)]

print(l1)
