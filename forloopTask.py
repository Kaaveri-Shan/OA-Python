print("1. Print numbers from 1 to 10")
for i in range(1, 11):
    print(i)

print("2. Print even numbers from 1 to 20")
for i in range(2, 21, 2):
    print(i)

print("3. Print odd numbers from 1 to 20")
for i in range(1, 21, 2):
    print(i)

print("4. Print numbers from 10 to 1")
for i in range(10, 0, -1):
    print(i)

print("5. Print squares of numbers from 1 to 10")
for i in range(1, 11):
    print(i*i)

print("6. Print multiples of 5 up to 50")
for i in range(5, 51, 5):
    print(i)

print("7. Sum of numbers from 1 to 10")
s = 0
for i in range(1, 11):
    s = s + i
print(s)

print("8. Sum of even numbers from 1 to 20")
s = 0
for i in range(2, 21, 2):
    s = s + i
print(s)

print("9. Sum of odd numbers from 1 to 20")
s = 0
for i in range(1, 21, 2):
    s += i
print(s)

print("10. Multiplication table of 7")
for i in range(1, 11):
    print("7 x", i, "=", 7*i)

print("11. Numbers divisible by 3 from 1 to 30")
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

print("12. Factorial of 5")
fact = 1
for i in range(1, 6):
    fact =fact * i
print(fact)

print("13. Print numbers from 1 to n (n = 15)")
n = int(input("Enter the value of n : "))
for i in range(1, n):
    print(i)

print("14. Count digits of a number (54321)")
num = 54321
count = 0
for i in range(5):
    if num != 0:
        count = count + 1
print(count)

print("15. Reverse a number (1234 → 4321)")
num = 1234
rev = 0
for i in range(4):     
    if num != 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
print(rev)

print("16. To print the digits of a number (example: 987 → 9, 8, 7)")
num = "987"
for ch in num:
    if ch.isdigit():
        print(ch)

print("17.Sum of the digits of number")
num = int(input("Enter the digits to add : "))
total = 0
for i in range(num):
    total = total+ num % 10
    num //= 10
print("Sum of digits:", total)

print("18.Sum of the digits of number")
base = int(input("Enter base: "))
power = int(input("Enter power: "))
for i in range(power,power+1):
    result = base ** i
print("Result =", result)


print("19.Check number is prime or not")
num = int(input("Enter a number: "))
count = 0    

for i in range(2, num):
    if num % i == 0:
        count += 1     

if count == 0:
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")


print("20.Print star pattern")
for i in range (1,5):
    print("*" * i)

print("reverse print if star")
for i in range (1,5):
    print(" "*(5-i),"*" * i)
   
