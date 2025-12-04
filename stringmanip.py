#1. Write a program to count the number of vowels in a given string.

print("1. A program to count the number of the vowels in the given string")
string1 = input("Enter the String : ")
count = 0
for i in string1:
        if i in "aeiouAEIOU":
            count += 1
print(count)


#2. Write a program to reverse a string using a loop (without using slicing).

print("2. To reverse a string using a loop (without using slicing).")

string2 = input("Enter the string : ")
reversedstring2 = string2[::-1]
print("The reversed string is : ",reversedstring2)


#3.Write a program to check if a string is a palindrome using a loop.

print("3. To check if a string is a palindrome using a loop.")
string3 = input("Enter the value of the String : ")
reversedstring3 = string3[::-1]
if string3 == reversedstring3:
      print(reversedstring3,"is a palindrome")
else:
      print(reversedstring3,"is not a palindrome")


#4.Write a program to count the number of uppercase and lowercase letters in a string.

print("4. To count the number of uppercase and lowercase letters in a string")
string4 = input("Enter the string : ")
Upper_case = 0
Lower_case = 0

for i in string4:
      if i.isupper():
            Upper_case += 1
      elif i.islower():
            Lower_case += 1
print("The count of uppercase is",Upper_case)
print("The count of lowercase is",Lower_case)

#5. Write a program to remove all spaces from a string without using built-in replace().

print("5. To remove all spaces from a string without using built-in replace().")
string5 = input("Enter the string with spaces : ")
spacelessstring5 =""

for i in string5:
      if i != " ":
            spacelessstring5 += i
print("The trimed string is",spacelessstring5)


#6.Write a program to find the frequency of each character in a string

print("6. To find the frequency of each character in a string")
string6 = input("Enter the string: ")
check = ""

for i in string6:
      if i not in check:
        count = 0
        for j in string6:
           if j == i:
                count += 1
        print(i,":", count)
        check += i

#7.Write a program to count how many digits are present in a string

print("7. To count how many digits are present in a string")
string7 = input("enter the string : ")
count = 0

for i in string7:      
      if i.isdigit():
            count += 1            
if count == 0:
           print("There is no digits in the string")
print("Number of digit present in the string is : ",count)


#8.Write a program to check if a string contains only alphabetic characters (without using isalpha())

print("8. To check if a string contains only alphabetic characters (without using isalpha())")
string8 = input("Enter the string : ")
only_alphabet = True

for i in string8:
        if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
                only_alphabet = False
                break
if only_alphabet:
        print("Has only alphabet")
else:
        print("Not only alphabet")

#9. Write a program to convert all lowercase letters in a string to uppercase manually using ASCII values.

print("9. To convert all lowercase letters in a string to uppercase manually using ASCII values.")
string9 = input("Enter the string : ")
result = ""

for i in string9:
    if i >= "a" and i <= "z":
        result += chr(ord(i) - 32)
    else:
        result += i
print(result)
        

#10.Write a program to print all characters located at even indices of a string.

print("10.To print all characters located at even indices of a string.")
string10 = input("Enter the string : ")
for i in range(len(string10)): 
    if i% 2 == 0:
         print(string10[i])


#11.Write a program to count the number of words in a string without using split().

print("11. To count the number of words in a string without using split()")          
string11 = input("Enter the sentence: ")
count = 1

for ch in string11:
    if ch == " ":
        count += 1
print("Words:", count)


#12.Write a program to replace all vowels in a string with * using a loop.

print("12. To replace all vowels in a string with * using a loop")
string12 = input("Enter the string: ")
result = ""

for ch in string12:
    if ch in "aeiouAEIOU":
        result += "*"
    else:
        result += ch
print(result)

#13.Write a program to find the longest word in a sentence
print("13. To find the longest word in a sentence")
string13 = input("Enter the sentence: ")
word = ""
longest = ""

for ch in string13 + " ":
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

print("Longest word:", longest)


#14.Write a program to check whether two strings are anagrams of each other using loops.
print("14. To check whether two strings are anagrams of each other using loops.")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagrams")
else:
    for ch in s1:
        if ch not in s2:
            print("Not Anagrams")
            break
    else:
        print("Anagrams")


#15.Write a program to count how many special characters are present in a string.

print("15. To count how many special characters are present in a string")
string15 = input("Enter the string: ")
count = 0

for ch in string15:
    if not ch.isalnum():
        count += 1
print("Special characters:", count)


#16. Write a program to print each character of a string a given number of times
print("16. To print each character of a string a given number of times")
string16 = input("Enter the string: ")
n = int(input("How many times? "))

for i in string16:
    print(i * n)


#17. Write a program to remove duplicate characters from a string using loops
print("17. To remove duplicate characters from a string using loops")
string17 = input("Enter the string: ")
result = ""

for ch in string17:
    if ch not in result:
        result += ch

print(result)

#18. Write a program to count the number of consonants in a given string.

print("18. To count the number of consonants in a given string.")
string18 = input("Enter the string: ")
count = 0

for ch in string18.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1
print("Consonants:", count)


#19.Write a program to capitalize the first letter of a string manually (without using capitalize())

print("19. To capitalize the first letter of a string manually (without using capitalize())")
string19 = input("Enter the string: ")

first = string19[0].upper()
print(first + string19[1:])

#20. Write a program to print characters of a string until a vowel is encountered.

print("20. To print characters of a string until a vowel is encountered.")
string20 = input("Enter the string: ")

for i in string20:
    if i in "aeiouAEIOU":
        break
    print(i)


