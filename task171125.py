
#1.Check if a number is a valid 4-digit PIN (1000–9999

print("1.Check if a number is a valid 4-digit PIN (1000–9999)")
n = int(input("Enter the 4 pin number : "))
if n >= 1000:
    if n <= 9999:
        print("Valid 4-digit PIN")
    else:
        print("is greater than 9999.It has five digit")
else:
    print("Lesser than 1000.It is 3 digit number ")


#2.Check if a number is single-digit, double-digit, or more
        
print("2.Check if a number is single-digit, double-digit, or more")
n1 = int(input("Enter the number to check : "))
if n1 >= 0:
    if n1 <= 9:
        print("Single digit")
    else:
        if n1 <= 99:
            print("Double digit")
        else:
            print("More than two digits")



#3.Compare three numbers and check if all are equal

print("3.Compare three numbers and check if all are equal")
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

if a != " " and b != " " and c != " ":
    if a== b and b == c and c==a:
        print("All are equal")
    else:
        print ("All are not equal")
else:
    print("do not leave any value null or empty")


#4.Check if a number is divisible by 5 AND also divisible by 10

print("4.Check if a number is divisible by 5 AND also divisible by 10") 
n2 = int(input("Enter the number : "))
if n2 % 5 == 0:
    if n2 % 10 == 0:
        print("Divisible by both 5 and 10")
else:
    print("Not divisible by both")


#5.Check if a number is a 3-digit number (100–999)

print("5.Check if a number is a 3-digit number (100–999)")
n3 = int(input("Enter the number : "))

if n3 >= 100:
    if n3 <= 999:
        print("It is a 3-digit number")
else:
    print("It is not a 3 digit number")
    

