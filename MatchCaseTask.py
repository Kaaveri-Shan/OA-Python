#1.Find the greatest number of all

print("1.Find the greatest number of all")
number1 = int(input("Enter the value of Number 1 : "))
number2 = int(input("Enter the value of Number 2 : "))
number3 = int(input("Enter the value of Number 3 : "))

match True:
    case _ if number1 == number2 == number3:
        print("All the number are true")
    case _ if number1 > number2 and number1 >number3:
        print(number1,"is greater")
    case _ if number2 > number1 and number2 > number3:
        print(number2," is greater")
    case _ if number3 > number1 and number3 > number2:
        print(number3," is greater") 
    case _:
        print("Enter the valid number&do not leave keep values empty")


#2.Find the string is in uppercare or in lower case
        
print("2.Find the string is in uppercare or in lower case")        
String = (input("Enter the String to check str is in upper or lower case : "))

match True:
    case _ if String.islower():
        print(String,"is in Lower case")
    case _ if String.isupper():
        print(String,"is in Upper case")
    case _:
        print(String,"Contain both lower and upper case")

#3.Check if a number is divisible by both 2 & 3.
        
print("3.Check if a number is divisible by both 2 & 3.")
num =int(input("Enter the number to check it is divisible by both 2 and 3 : "))

match True:
    case _ if num%2 == 0 and num%3 == 0:
        print(num,"is divisible by both 2 & 3")
    case _ if num%2 == 0 and num%3 != 0:
        print(num,"is divisible by  2")
    case _ if num%2 != 0 and num%3 == 0:
        print(num,"is divisible by  3")
    case _:
        print(num,"is not divisible by both 2 & 3")


#4.Check if a number ranges between 10 to 20

print("4.Check if a number ranges between 1-10 or 11-20")
number = int(input("Enter the number to check it ranges btw 1-10 or 11-20 : "))

match True:
    case _ if number == 0:
        print("you have entered zero")
    case _ if number == " ":
        print("Is empty")
    case _ if number <= 10:
        print(number,"ranges from 1 to 10")
    case _ if number <= 20:
        print(number,"ranges from 11 to 20")
    case _:
        print(number,"ranges above 20")


#5.Check if it is a perfect square or not
        
print("5.Check if it is a perfect square or not")
numm = int(input("Enter the number to check if it is a perfect square or not : "))
NewNum = numm**0.5

match True:
    case _ if numm == " ":
        print("Is empty")
    case _ if int(NewNum)**2 == int(numm):
        print(numm,"is a perfect square")
    case _:
        print(numm,"is not a perfect square")


#6.Check if a number is a multiple of 7.

print("6.Check if a number is a multiple of 7.")
check1 = int(input("Enter the number to check it is multiple of 7 : "))

match True:
    case _ if check1 % 7 == 0:
        print("Yes",check1,"is a multiple of 7")
    case _ if check%7 != 0:
        print("No",check1,"is not a multiple of 7")
    case _ :
        print("Enter the valid number")
        

#.7.Check if it is greater than 100 and divisible by 5
        
print("7.Check if it is greater than 100 and divisible by 5")
Num_Ber = int(input("Enter the number to check if it is greater than 100 and divisible by 5 : "))

match True:
    case _ if Num_Ber%5 == 0 and Num_Ber > 100:
        print(Num_Ber,"is greater than 100 and divisible by 5")
    case _ if Num_Ber < 100 and Num_Ber%5 != 0:
        print(Num_Ber,"is lesser than 100 and not divisible by 5")
    case _ if Num_Ber > 100 and Num_Ber%5 != 0:
        print(Num_Ber,"is greater than 100 but not divisible by 5")
    case _:
        print(Num_Ber,"is lesser than 100 but divisible by 5")


    

        

