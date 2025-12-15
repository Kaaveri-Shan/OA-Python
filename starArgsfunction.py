def myfunction(a,b,c ,*num):
    print(a+b+c)
    print(num)

myfunction(2,5,3,6,7,54,754,24)

# **kwargs
def myfun1(Name,Email,Mobile,Qualification):
    print(Name,Email,Mobile,Qualification)
myfun1(Name = "Kaaveri", Email = "Kaaveri@gmail.com",Mobile = 9877654431,Qualification = "Engineering")

def myfun1(**data):
    print(data)
myfun1(Name = "Kaaveri", Email = "Kaaveri@gmail.com",Mobile = 9877654431,Qualification = "Engineering")

# Function Return Statement:
def addition(n1,n2):
    result = n1 + n2
    return result
print(addition(90,60))

# Local Scope:
def myFunction():
    Name = "KaaveriSankar"
    print(Name,"inside the function-Local Scope")
myFunction()
# print(name)

# Global Scope
Name = "Kaaveri"
def myFunction():
    print(Name,"inside the function-Global Scope")
myFunction()
print(Name,"Outside the function-Global Scope" )

# Modify the Global Scope
name = "Kaaveri"
def Func():
    name = "Barath"
    print(name,"inside the function")
Func()
print(name,"outside the function")

# Modified Global Scope
name = "Kaaveri"
def Func():
    global name
    name = "Barath"
    print(name,"inside the function")
Func()
print(name,"outside the function")