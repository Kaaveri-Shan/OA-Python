def myFunction(x,*numbers):
    print(numbers)
    print(x)

myFunction(2,5,1,5,8.30,2)

def addition(a,b,c = 25):
    z = a + b + c
    print(z) 

addition(10,20,15)


# kwargs

# def f2(name,email):
#     print(name,email)

# f2(name = "aaa", email = "aaa@gmail.com")

def f2(**data):
    # print(name,email)
    print(data)

f2(name = "aaa", email = "aaa@gmail.com")

# function return

# def f3():
#     print("demo")
#     return "working"
#     print("demo")

# print(f3())

def f3(n1,n2):
    print("demo")
    return n1 + n2
    

print(f3(2,5))


# scope

# local scope
# def f4():
#     idNumber = "ST001"
#     print(idNumber,"inside the function")

# f4()
# print(idNumber,"outside the function")


# global scope

# idNumber = "ST 001"
# def f4():
    
#     print(idNumber,"inside the function")

# f4()
# print(idNumber,"outside the function")


# idNumber = "ST 001"
# def f4():

#     idNumber = "EMP 001"
    
#     print(idNumber,"inside the function")

# f4()
# print(idNumber,"outside the function")





# The global keyword is required if you want to modify or create a global variable from inside a function's local scope.

x = 10 # Global variable

def modify_global():
  global x # Declare intent to modify the global variable
  x = 20   # This modifies the global x

modify_global()
print(x) # Output: 20