# # 1. Single Inheritance
#     # One child class inherits from one parent class.

print("1.Single Inheritance")
class Parent:
    def __init__(self, name):
        self.name = name

    def show_parent(self):
        print("Parent name:", self.name)


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # calling Parent __init__
        self.age = age

    def show_child(self):
        print("Child age:", self.age)


obj = Child("Ravi", 10)
obj.show_parent()
obj.show_child()

# 2. Multiple Inheritance
    # A child class inherits from more than one parent class.

# print("2.Multiple Inheritance")
# class Father:
#     def __init__(self, fname):
#         self.fname = fname

#     def show_father(self):
#         print("Father name:", self.fname)


# class Mother:
#     def __init__(self, mname):
#         self.mname = mname

#     def show_mother(self):
#         print("Mother name:", self.mname)


# class Child(Father, Mother):
#     def __init__(self, fname, mname, cname):
#         Father.__init__(self, fname)
#         Mother.__init__(self, mname)
#         self.cname = cname

#     def show_child(self):
#         print("Child name:", self.cname)


# obj = Child("Ramesh", "Sita", "Amit")
# obj.show_father()
# obj.show_mother()
# obj.show_child()


# 3. Multilevel Inheritance
    # A class is derived from another derived class

# print("3.MultiLevel Inheritance")
# class Grandparent:
#     def __init__(self, gname):
#         self.gname = gname

#     def show_grandparent(self):
#         print("Grandparent name:", self.gname)


# class Parent(Grandparent):
#     def __init__(self, gname, pname):
#         super().__init__(gname)
#         self.pname = pname

#     def show_parent(self):
#         print("Parent name:", self.pname)


# class Child(Parent):
#     def __init__(self, gname, pname, cname):
#         super().__init__(gname, pname)
#         self.cname = cname

#     def show_child(self):
#         print("Child name:", self.cname)


# obj = Child("Krishna", "Arjun", "Abhi")
# obj.show_grandparent()
# obj.show_parent()
# obj.show_child()


# 4. Hierarchical Inheritance
    # Multiple child classes inherit from one parent class

# print("4.Hierarchical Inheritance")
# class Parent:
#     def __init__(self, pname):
#         self.pname = pname

#     def show_parent(self):
#         print("Parent name:", self.pname)


# class Child1(Parent):
#     def __init__(self, pname, c1name):
#         super().__init__(pname)
#         self.c1name = c1name

#     def show_child1(self):
#         print("Child1 name:", self.c1name)


# class Child2(Parent):
#     def __init__(self, pname, c2name):
#         super().__init__(pname)
#         self.c2name = c2name

#     def show_child2(self):
#         print("Child2 name:", self.c2name)


# obj1 = Child1("Suresh", "Ravi")
# obj2 = Child2("Suresh", "Anu")

# obj1.show_parent()
# obj1.show_child1()

# obj2.show_parent()
# obj2.show_child2()

# 5.Hybrid Inheritance (Simple Example)
    # Hybrid inheritance = Combination of Multilevel + Multiple inheritance
# print("5.Hybrid Inheritance")
# class A:
#     def show_a(self):
#         print("This is class A")


# class B(A):
#     def show_b(self):
#         print("This is class B")


# class C(A):
#     def show_c(self):
#         print("This is class C")


# class D(B, C):
#     def show_d(self):
#         print("This is class D")


# obj = D()

# obj.show_a()
# obj.show_b()
# obj.show_c()
# obj.show_d()
