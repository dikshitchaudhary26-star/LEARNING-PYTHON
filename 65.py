#TUPLE 
#SETS

#list  -> mutable
#tuple -> immutable 

t1 = (1,2,3,4)

#t1[0] = 10 #immutable

print(t1)

t = (5)

print(type(t)) #--> will be int because single will be considered as int

t2 = (5,)
print(type(t2)) #--> now it is a tuple

t3 = ()
print(type(t3)) #--> it is a empty tuple so type: tuple

#TUPLE PACKING --> when elements are stored without parenthesis

t4 = 1,2,3,4,5

print(type(t4))

#TUPLE UNPACKING 

a,b,c,d,e = t4

print(a,b,c,d,e)

a,b,*rest = t4  #elements of rest are stored in list (python by default convert into list)

#but if you want to convert rest into tuple 

rest = tuple(rest)

print(a,b,*rest) 
print(type(rest))
print(type(a))
print(a,b,rest)

#LIST AND TUPLE ARE ORDERED , ALLOW DUPLICATES , LIST->MUTABLE , TUPLE->IMMUTABLE

#SET 

#SETS -> UNORDERED , UNIQUE ELEMENTS , CANNOT ACCESS ELEMENTS OF SETS USING INDEX(BECAUSE SET IS UNORDERED COLLECTION)

s = {1,2,3,4,4,4,4,4,5,67,87,76,45,45,45,4,5,45} #unordered means not the same order in which they are arranged in set

print(type(s))

print(s)

#CONVERT LIST TO SET 
l1 = [1,1,2,3,3,3,3,4,5]  

print(l1)

s1 = set(l1)

print(s1)

s99 = {1,2,3,4}

s99.add(69)
s99.remove(4)
s99.discard(3)
#s99.remove(100)#if element not presesnt gives error
s99.discard(1000)# if element is not present it do not gives error

print(s99)



#set -> mutable , frozenset -> immutable 
#set also perform  union(|) , intersection (&),difference(-) , symmetric(^)->(remove common elements) etc 

