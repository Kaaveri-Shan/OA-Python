#to check eligibility to vote

YourAge = int(input("Enter your age : "))
if YourAge>=18:
    print("You are Eligible to vote")
else:
    print("You are Not Eligible to vote")

    

#to check the given number is +ve or -ve
    
Number = int(input("Enter any number : "))
if Number == 0:
    print("You have entered Zero")
elif Number > 0:
    print(Number ,"is positive +ve")
else:
    print(Number,"is negative -ve")




#to check the given numbe is odd or even

num = int(input("Enter the number : "))
if num%2 == 0:
    print(num, "is a even number")
elif num%2 != 0:
    print(num,"is a odd number ")
else:
    print("Enter the valid number")
