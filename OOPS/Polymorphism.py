# # compile time poly or static poly
# # What is Method Overloading ?

# # Method overloading means having multiple methods with the same name but different parameters.

# # Why Python Doesn’t Support Traditional Overloading

# # In Python, if multiple methods with the same name are defined in a class, the last one overrides the previous ones.


# class Poly():
#     def f1(self,a,b,c=10):
#         return  a + b + c
#     # def f1(self,a,b,c):
#     #     return a + b + c

# obj = Poly()
# print(obj.f1(10,20))
# print(obj.f1(2,3,4))



# method overriding

# that allows a subclass to provide a specific implementation for a method that is already defined in its parent class.

class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    # Overriding the speak method
    def speak(self):
        return "Bark"

class Cat(Animal):
    # Overriding the speak method and using super()
    def speak(self):
        parent_sound = super().speak() # Call parent method
        return f"{parent_sound} followed by Meow"

# Create objects
generic_animal = Animal()
dog_instance = Dog()
cat_instance = Cat()

# Calling the methods demonstrates overriding
print(f"Generic Animal: {generic_animal.speak()}")
print(f"Dog: {dog_instance.speak()}")
print(f"Cat: {cat_instance.speak()}")