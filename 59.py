#SORT THE ELEMENTS OF LIST

num = [3,2,5,6,8]

for i in range (0,len(num)):

    for j in range ((i+1),len(num)):

        if num[j] < num[i]:

            temp = num[i]
            num[i] = num[j]
            num[j] = temp



print(num)