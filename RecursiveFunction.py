print("1.Factorial using Recursive Function ")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

print("2.Fibbonaci using Recursive Function ")
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

print("3.Sum of Natural using Recursive Function ")
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)

print(sum_n(5))

print("4.Reverse a string using Recursive Function ")
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))

print("5. Power of a number using Recursive Number")
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n-1)

print(power(2, 5))
