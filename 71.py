
def f1(name): #--> user defined function
    """ RETURNING MINIMUM AND MAXIMUM VALUE"""
    max(name) #--> pre defined function
    min(name) #--> pre defined function
    

    return max(name),min(name)#--> return comma seperated  in tuple

# why in tuple ?

#--> because packing and unpacking will be easier
#--> Once created, a tuple's elements cannot be reassigned, added, or removed. This makes tuples useful for grouping related results that shouldn't be structurally modified.




m1,m2 = f1([1,2,3,4,56])

print(f"Max value is :{m1}")
print(f"Min value is :{m2}")

print(f1.__doc__)

#LEGB --> LOCAL--> ENCLOSING-->GLOBAL-->BUILT-IN (way in which functions search values of variables)


# """DOC STRING """
#PURPOSE--> string right under the def line that explains what the function does, it'show professionals document code 