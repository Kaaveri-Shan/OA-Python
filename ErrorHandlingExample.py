class InvalidAgeError(Exception):
    # Custom exception for handling invalid age inputs
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

# Use the custom exception in a try-except block
try:
    check_age(-5)
except InvalidAgeError as e:
    print(e)


print("1. Exception")
try:
    raise Exception("Error")
except Exception:
    pass


print("\n2. StopIteration")
try:
    lst = [1]
    it = iter(lst)
    next(it)
    next(it)
except StopIteration:
    pass


print("\n3. ArithmeticError")
try:
    x = 10 / 0
except ArithmeticError:
    pass


print("\n4. OverflowError")
import math
try:
    math.exp(1000)
except OverflowError:
    pass


print("\n5. ZeroDivisionError")
try:
    x = 5 / 0
except ZeroDivisionError:
    pass


print("\n6. AssertionError")
try:
    x = 5
    assert x > 10
except AssertionError:
    pass


print("\n7. AttributeError")
try:
    x = 10
    x.append(5)
except AttributeError:
    pass


print("\n8. EOFError")
try:
    input()
except EOFError:
    pass


print("\n9. ImportError")
try:
    import abcde
except ImportError:
    pass


print("\n10. NameError")
try:
    print(a)
except NameError:
    pass


print("\n11. SyntaxError")
# if True
#     print("Hello")


print("\n12. IndentationError")
# def test():
# print("Hi")


print("\n13. TypeError")
try:
    x = 5 + "5"
except TypeError:
    pass


print("\n14. ValueError")
try:
    int("abc")
except ValueError:
    pass


print("\n15. RuntimeError")
try:
    def fun():
        fun()
    fun()
except RuntimeError:
    pass


print("\n16. NotImplementedError")
try:
    class A:
        def show(self):
            raise NotImplementedError
    A().show()
except NotImplementedError:
    pass
