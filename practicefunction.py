print("Implementing conditional statement inside the Function")
print("1.To find odd ar even ___IF STATEMENT IS USED_____")
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
print(evenOdd(16))
print(evenOdd(7))

print("2.To Find leap year or not___IF STATEMENT IS USED_____")
def LeapYear(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(year,"is a leap year")
    else:
        print(year,"is not leap year")
LeapYear(2004)

print("3.To check if a number is divisible by 3 and 5___IF STATEMENT IS USED_____")
def NumCheck(a):
    if a %3 == 0 and a %5 == 0:
        print("Yes Number is divisible by both")
    else:
        print("Not Divisibly by both the number")
NumCheck(15)

print("4.Check the number is prime or not___IF STATEMENT IS USED_____")
def CheckPrime(num):
    if num > 1 and num % 2 != 0 and num % 3 != 0:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
CheckPrime(7)

print("5.Find the smallest number of 3 numbers___IF STATEMENT IS USED_____")
def FindSmallNum(a,b,c):
    if a<b and a<c:
        print(a,"is lesser than ",b,c)
    elif b<a and b<c:
        print(b,"is lesser than ",a,c)
    else:
        print(c,"is lesser than ",a,b)
FindSmallNum(3,6,9)

print("Implementing For Loop Inside the Function")
print("1.Square number 1 to 5 ____FOR LOOP IS USED_____")
def Square():
    for i in range(1,6):
        print(i,"-",i*i)
Square()

print("2.Print star pattern____FOR LOOP IS USED_____")
def StarPattern():
    for i in range (1,5):
        print("*" * i)
StarPattern()
# print star pattern in  reverse

def RevStar():
    for i in range (1,5):
        print(" "*(5-i),"*" * i)
RevStar()

print("3.Multiplication table of 7____FOR LOOP IS USED_____")
def Multiplication():
    for i in range(1, 11):
        print("7 x", i, "=", 7*i)
Multiplication()

print("4. Factorial of a number____FOR LOOP IS USED_____")
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)
factorial(5)

print("5. Sum of odd numbers from 1 to 20____FOR LOOP IS USED_____")
def sumofoddnum():
    s = 0
    for i in range(1, 21, 2):
        s += i
    print(s)
sumofoddnum()




