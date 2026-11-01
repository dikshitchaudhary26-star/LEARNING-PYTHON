#ARGS
#KWARGS

#def add(a,b,c):
  #  return a+b+c


#a,b,c = 1,2,3

#print(add(a,b,c))

# but if we want to add 1,2,3,4,5,6,7
#THEN WE  HAVE TO MAKE ANOTHER FUNCTION TAKING 7 ARGUMENTS OR NEED TO MODIFY THE PRESENT FUNCTION
# WHAT WE CAN DO IS WE CAN DEFINE FUNCTION LIKE THIS AND CAN TAKE AS MANY ARGUMENTS WE NEED

def add(*args): # this will store elements in tuple 

    sum = 0
    for ele in args:
        sum = sum + ele

    return sum

print(add(3,4,5,6,7,8,9))

#tuples are faster and more memory efficient as compared to lists 
import sys

my_tuple = (10, 20, 30, 40, 50)
my_list = [10, 20, 30, 40, 50]

print("Tuple memory:", sys.getsizeof(my_tuple))
print("List memory:", sys.getsizeof(my_list))

#A. No modification operations

#Tuples cannot be resized or have their elements replaced. Python doesn't need to support these operations on tuples.

#B. Simpler memory management

#Since tuples have a fixed size, Python can manage their storage more simply.

#C. Less overhead

#Their implementation has fewer requirements associated with resizing and modifying elements.

#this can make tuple operations slightly faster in many situations.

#KWARGS -> same idea as that of args we can pass multiple parameters

def intro(**kwargs): #--> create dictionary
    return kwargs

def intro(**kwargs): #--> create dictionary

    for values in kwargs.values():
        print(values)



print(intro(name = "raja" , age = "45"))

#The second function will run, because in Python, when you define another function with the same name, the previous function binding is replaced by the new one.

#Yes! If we save another reference to it before redefining the name.

def intro():
    print("Hello")

old_intro = intro

def intro():
    print("Good morning")

old_intro()
intro()

#Here, * tells Python:

#"Accept any number of positional arguments and collect them into one tuple."

#What does ** do in **kwargs?
#It collects multiple keyword arguments and packs them into a dictionary.

#unpacking at the call site 

def add(a,b,c):
    return a + b + c


nums = [1,2,3]
print(add(*nums)) # ** also do the same

#print() uses this 