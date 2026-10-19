#DICTIONARY
# b = set() #empty set 
#d1 =    {

            #key : value

 #       } #blank dictionary

# searching -> O(1)
# example a phone number book and you have to find number of someone (possible due to hashing)

d1 = {
        "Name" : "Dikshit Chaudhary",
        "roll no" : 1025170353,
        2  :  67,
        (5,7) : "hello"

     }



print(type(d1))
print(type(d1["Name"]))
print(type(d1["roll no"]))
print(d1["Name"])
print(d1["roll no"])
print(type(d1[2]))
print(type(d1[(5,7)]))

#HASHABLE(have keys)  -->  int ,float,none,boolean,string

#UNHASHABLE-->  list,tuple

#hashing ->

#is a process in which a hash function takes an input and generate a fixed value for that input

# "name" -> hash() -> 345463
# "roll no" -> hash() -> 564732
