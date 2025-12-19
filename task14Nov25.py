#1.to check the given number is +ve or -ve
    
Number = int(input("Enter any number : "))
if Number == 0:
    print("You have entered Zero")
elif Number > 0:
    print(Number ,"is positive +ve")
else:
    print(Number,"is negative -ve")


    
#2.to check the given numbe is odd or even

num = int(input("Enter the number : "))
if num%2 == 0:
    print(num, "is a even number")
elif num%2 != 0:
    print(num,"is a odd number ")
else:
    print("Enter the valid number")



#3.Find the largest of three number.

num1 = int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))
num3 = int(input("Enter the number3 : "))

if num1==num2==num3:
    print("all the number are equal")
elif num1>num2<num3:
    print(num1,"is greatest of all")
elif num2<num1>num3:
    print(num2,"is greatest of all")
elif num3>num1<num2:
    print(num3,"is greatest of all")
elif num1 == num2<num3:
    print(num3,"is the greatest of all")
elif num2 == num3<num1:
    print(num1,"is the greatest of all")
elif num1 == num3<num2:
    print(num2,"is the greatest of all")
else:
    print("error : Please enter valid number")



#4.To check whether the given year is leap year or not.

year = int(input("Enter the year to check is it a leap year or not : "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(year,"is a leap year")
else:
    print(year,"is not leap year")
    


#5.To check if a number is divisible by 3 and 5

NumberDivisibleBy3and5 = int(input("Enter any number to check is it divisible by 3 and 5 : "))
if NumberDivisibleBy3and5 % 5 ==0 and NumberDivisibleBy3and5 % 3 == 0:
    print(NumberDivisibleBy3and5,"is divisible by both 3 and 5")
else:
    print(NumberDivisibleBy3and5,"is not divisible by 5 and 3")



#6.Check if a number is Prime number or not

CheckPrime = int(input("Enter the number to check if it is prime or not : "))
if CheckPrime > 1 and CheckPrime % 2 != 0 and CheckPrime % 3 != 0:
    print(CheckPrime,"is a prime number")
else:
    print(CheckPrime,"is not a prime number")



#7.To check if the char is vowel or consonant
    
char = input("Enter the Char to check whether it is vowel or consonant : ")
Lowercase_char = char.lower()
if Lowercase_char == "a":
    print(char,"is a vowel")
elif Lowercase_char == "e":
    print(char,"is a vowel")
elif Lowercase_char == "i":
    print(char,"is a vowel")
elif Lowercase_char == "o":
    print(char,"is a vowel")
elif Lowercase_char == "u":
    print(char,"is a vowel")
else:
    print(char,"is a consonant")



#8.To check the given number is between 10 and 20

num_check = int(input("Enter the number to check it lies btw 10 and 20 : "))
if num_check >= 10 and num_check <=20:
    print(num_check,"lies between 10 to 20")
else:
    print(num_check,"does not lies btw 10 and 20")



#9.Check if a number multiple of another number

number1 = int(input("Enter the number to check if a number is a multiple of another number : "))
number2 = int(input("Enter the number to check if a number is a multiple of number1 : "))
if number1 % number2 == 0:
    print(number1,"is divisible by",number2)
else:
    print(number1,"is not divisible by",number2)



#10.Find the smallest number of 3 numbers

a=int(input("Enter the value of a to find smaller of 3 value : "))
b=int(input("Enter the value of b to find smaller of 3 value : "))
c=int(input("Enter the value of c to find smaller of 3 value : "))
if a<b and a<c:
    print(a,"is lesser than ",b,c)
elif b<a and b<c:
    print(b,"is lesser than ",a,c)
else:
    print(c,"is lesser than ",a,b)




#11.Check if the number is a perfect square

numm = int(input("Enter the number to check if it is a perfect square or not : "))
NewNum = numm**0.5
if int(NewNum)**2 == int(numm):
    print(numm,"is a perfect square")
else:
    print(numm,"is not a perfect square")



#12.Check if a string contains a specific word

Sentence = "Hi,I am kaaveri from Pondicherry"
word = str(input("Enter a word to check if it is present in Sentence : "))
if word in Sentence:
    print("The word is present")
else:
    print("The word is not in the sentence")



#13.Check if a number is multiple of 7

check1 = int(input("Enter the number to check it is multiple of 7 : "))
if check1 % 7 == 0:
    print("Yes",check1,"is a multiple of 7")
else:
    print("No",check1,"is not a multiple of 7")


    
#14.To check if 2 number are equal

Number_One = int(input("Enter the number 1 to compare : "))
Number_Two = int(input("Enter the number 2 to compare : "))
if(Number_One == Number_Two):
    print("Both",Number_One,"and",Number_Two,"are equal")
else:
    print("Both",Number_One,"and",Number_Two,"are not equal")



#15.Check if a string starts with a specific character

str_name = "Kaaveri"
str_check = str(input("Enter the first letter of the str : "))
if str_name[0] == str_check:
    print("Yes,The string is",str_name,"it starts with'K'")
else:
    print("No the string starts with'K'")



#16.Check if a number is a multiple of 2,3 or both

numb = int(input("Enter the number to check it is multiple of 2 or 3 or both : "))
if numb%2 == 0 and numb%3 == 0:
    print(numb,"is multiple by both 2 and 3")
elif numb%2 ==0 and numb%3 !=0:
    print(numb,"is only multiple of 2")
elif numb%2 !=0 and numb%3 ==0:    
    print(numb,"is only multiple of 3")
else:
    print(numb," is Not a multiple of both 2 and 3")



#17.Check if a number is divisible by 4 and not by 6

test = int(input("Enter the number to check if it is divisible by 4 and not by 6 : "))
if test%4 == 0 and test%6 != 0:
    print("Yes",test,"is divible by 4 and not divisible by 6")
elif test%4 == 0 and test%6 == 0:
    print("No",test,"is divible by both 4 and 6")
else:
    print(test,"Is divisible by both 4 and not divisible by 6")



#18.Check if a string is uppercase or in lowercase

check_str = str(input("Enter the string"))
if check_str.islower():
    print(check_str,"is in the lower case")
elif check_str.isupper():
    print(check_str,"is in the UPPERCASE")
else:
    print(check_str,"is a combination of lowercase and UPPERCASE")




#19.Check if a number is divisible by 2 and 3
NumberDivisibleBy3and2 = int(input("Enter any number to check is it divisible by 3 and 2 : "))
if NumberDivisibleBy3and2 % 2 ==0 and NumberDivisibleBy3and2 % 3 == 0:
    print(NumberDivisibleBy3and2,"is divisible by both 3 and 2")
else:
    print(NumberDivisibleBy3and2,"is not divisible by 2 and 3")



#20.Check if a number is greater than 100 and divisible by 5

Num_Ber = int(input("Enter the number to check if it is greater than 100 and divisible by 5 : "))
if Num_Ber%5 == 0 and Num_Ber > 100:
    print(Num_Ber,"is greater than 100 and divisible by 5")
elif Num_Ber > 100 and Num_Ber%5 != 0:
    print(Num_Ber,"is greater than 100 but not divisible by 5")
else:
    print(Num_Ber,"is greater than 100 but divisible by 5")



#21.Check if a number ranges betwwn 50 to 150

num_ber = int(input("enter the number to check whether it ranges btw 50 to 150: "))
if num_ber >=50 and num_ber<=150:
    print(num_ber,"ranges between 50 to 150")
else:
    print(num_ber,"does not ranges between 50 to 150")



#22.Check if number is divisible by 2 and not by 4

test1 = int(input("Enter the number to check if it is divisible by 2 and not by 4 : "))
if test1%2 == 0 and test1%4 != 0:
    print("Yes",test1,"is divible by 2 and not divisible by 4")
elif test1%2 == 0 and test1%4 == 0:
    print("No",test1,"is divible by both 2 and 4")
else:
    print(test1,"divisible by either 1 num or not divisible by both")



#23.Palindrome
Palindrome = str(input("Enter the palindrome : "))
if Palindrome[::-1] == Palindrome:
    print("given string is a palindrome")
else:
    print("not a palindrome")



#24.Check whether two digit number (10 to -99 or -10 to -99)

nummm = int(input("Enter the number to check it is a 2 digit number or not : "))
if(nummm>=10 and nummm<=99) or (nummm <= -10 and nummm >= -99):
    print(nummm,"is a two digit number")
else:
    print(nummm,"the number is not two digit number")



#25.Check if a number is greater than or equal to 0 but less than 100

last = int(input("Enter the number to check it is greater than or equal to 0 but less than 100 : "))
if last >=0 and last < 100:
    print(last,"ranges btw 0 to 100")
else:
    print(last,"does not ranges between 0 to 100")





    

    



                       

    






                
    















