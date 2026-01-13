# single inheritance

# class Parent():
#     def f1(self):
#         print("method in parent class is working")

# class Child(Parent):
#     def f2(self):
#         print("method in child class is working")

# cObj = Child()
# cObj.f1()
# cObj.f2()


# multiple inheritance

# class Father():
#     def f1(self,name):
#         print("method in Father class is working",name)

# class Mother():
#     def f2(self):
#         print("method in Mother class is working")

# class Child(Father,Mother):
#     def f3(self):
#         print("method in Child class is working")

# myObject = Child()
# myObject.f1("aaaa")
# myObject.f2()



# multilevel inheritance

# class Grandparent:
#     def house(self):
#         print("Grandparent's house")

# class Parent(Grandparent):
#     pass

# class Child(Parent):
#     pass

# c = Child()
# c.house()



# Hierarchical Inheritance

# class parent():
#     motherName = "demo mother"

# class Child1(parent):
#     child1Name = "demo child1"

# class Child2(parent):
#     child2Name = "demo child 2"

# obj = Child1()
# obj2 = Child2()
# print(obj.motherName)
# print(obj2.child2Name)



# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     pass
#     # def speak(self):
#     #     print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# d = Dog()
# c = Cat()
# d.speak()
# c.speak()

# hybrid inheritance

class A:
    def method_a(self):
        print("A")

class B(A):
    def method_b(self):
        print("B")

class C(A):
    def method_c(self):
        print("C")

class D(B, C):
    pass

d = D()
d.method_a()