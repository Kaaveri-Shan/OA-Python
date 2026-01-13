# class MyClass:
#     username = "Kaaveri"
#     Age = 24

#     def Function1(self):
#         print("Working")

# objf1 = MyClass()
# print(objf1.username)
# print(objf1.Age)
# objf1.Function1()

class Dog:
    def __init__(self, name, age):  
        self.name = name 
        self.age = age

    def bark(self): 
        print(f"{self.name} is barking!")

# Creating an instance of Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Mojo", 3.5)
dog3 = Dog("Coco", 4)
dog1.bark() 
dog2.bark()
dog3.bark()