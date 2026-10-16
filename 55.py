#PROBLEM - FIND SUM AND AVERAGE OF MARKS
marks = [91,92,93,94,95]
sum = 0
for i in range (0,len(marks)):
    sum = sum + marks[i]

average = sum/len(marks)

print(f"SUM OF ALL MARKS :{sum}")
print(f"AVERAGE :{average}")