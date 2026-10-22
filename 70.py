#FUNCTIONS

#FUNCTION IS A NAMED LOGIC WHICH WE CAN RE-USE

def intro(name,age,profession): #--> formal parameter
    print(f"Name :{name}")
    print(f"Age :{age}")
    print(f"Profession :{profession}")


intro("raju" , 19 , "hacker")#--> actual parameter
intro("raju" , 19 , "hacker")#--> positional argument
intro(age = 19 , name = "raju" , profession = "hacker")#--> keyword argument


def intro(name,profession,age = 34): #--> default parameter
    print(f"Name :{name}")
    print(f"Age :{age}")
    print(f"Profession :{profession}")

intro("raj", "engineer")