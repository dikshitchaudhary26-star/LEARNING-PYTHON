# PROBLEM - COUNT TOTAL NUMBER OF DUPLICATES
num = [1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 6]

count = 0

for i in range(len(num)):
    val = num[i]

    for j in range(i + 1, len(num)):
        if val == num[j]:
            count = count + 1

print(f"TOTAL DUPLICATE OCCURRENCES ARE {count}")
