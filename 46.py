#LISTS
#ELEMENTS ARE STORED IN ORDERED WAY

a = [1,2,3]
b = a 
b.append(4)
print(a)
print(b)



# why both lists have same elements if we appended element in b only ?

""" 
THIS HAPPENS BECAUSE "a" IS STORING ADDRESS OF THE LIST AND WHEN WE DO "b = a" 
THE ADDRESS OF "a" IS PASSED TO "b" AND WHEN WE DO "b.append()" BOTH  
GETS UPDATED
"""