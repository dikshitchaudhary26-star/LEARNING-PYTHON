#LIST METHODS

num = [2,1,4,5,3,6,7]

new_list = sorted(num) # RETURNS LIST IN A SORTED WAY

print(new_list)

a = [1,1,2,3,4,5,5,6,7]

print(a.count(9)) #COUNT RETURN THE FREQUENCY OF THE GIVEN ELEMENT

#extend()

a = [1,2,3,4]

b = [6,7]

a.extend(b)

print(a)

b.extend(a)

print(b)