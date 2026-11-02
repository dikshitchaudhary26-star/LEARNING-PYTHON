#lambda function
#laxography -> sort on the basis of dictionary 

student = [("amit",85),("neha",92),("ravi",78),("laxmi",25)]

student.sort() #sort on the basis of first item

student.sort(key = lambda s : s[1]) #sort on the basis of second item,and see how lambda function implemented without any prior function definition

#implementation

"""
what lambda function did 
85->("amit",85)
92->("neha",92)
78->("ravi",78)
25->("laxmi",25)

then sort function sorts the 85,92,78,25

"""

print(student)


#map()

#       map(function,collection)--> call function for each element in collection
#                                   we can use list comprehension for the same purpose but sometimes it becomes very complex

nums = [1,2,3,4,5]

key = list(map(lambda n : n**2,nums))

print(key)

#filter()

#       filter(function,collection)-->call function(here function return boolean value if value is true then it gets stored) for each element in collection 

num = [1,1,2,2,3,3,4,4,54,5]

val = list(filter(lambda n : n%2==0,num))

print(val)

#reduce()

#       reduce(function,collection)->repeatedly combines everything into single number

from functools import reduce # we need to call it from here

numbers = [1,2,3,4,5]

prod = reduce(lambda a,b : a*b , nums)

print(prod)