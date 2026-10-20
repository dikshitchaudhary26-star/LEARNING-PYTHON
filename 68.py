#SET COMPREHENSION 

s1 = {i*i for i in range (1,11)}

print(s1)

#DICTIONARY COMPREHENSION 

nums = {1,2,3,4,5}

d1 = {ele : ele*ele for ele in nums }

print(d1)