#NAMED TUPLE
# here we give name to elements instead of index 

from collections import namedtuple

Employee = namedtuple('Employee',['id','name','salary'])

s1 = Employee(1,"raju",45000)

print(type(s1))
print(type(s1[0])) # can also access through index
print(type(s1.name))
print(type(s1.salary))

l2 = [2,"raj",12345]

s2 = Employee._make(l2)

print(s2[0])

s2._asdict
print(s2)

new_s2 = s2._replace(s2)