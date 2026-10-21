#dictionary , CRUD , LOOPING

person = dict([("raju",8),("ballu",9)])

print(type(person))

print(person)

person = dict(name = "raju" , city = "indore")
print(person)

print(person["name"]) #if key is not present it will give error

print(person.get("name")) #if key is not present it will not give error(gives 'none')
print(person.get("average","not found")) #if not found it will print "not found"

person.pop("city")

print(person)




d1 =    {
            "name" : "raju",
            "roll_no" : 1,
            "age" : 19
        }

print(d1.keys())
print(d1.values())


for ele in d1.keys():
    print(ele)

for ele in d1.values():
    print(ele)

print(d1.items())

for k,e in d1.items():
    print(f"{k} : {e}")
