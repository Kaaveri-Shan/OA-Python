#1. Write a Python program to print all elements of a list using a loop.

print("1. To print all elements of a list using a loop.")
Name = ["Kaaveri","Bavani","Sankar","Praveen","Sadhana"]
for i in Name:
        print(i)

#2. Write a Python program to print only the even numbers from a list.

print("2. To print only the even numbers from a list.")
NumberList = [12,33,44,53,65,35,90,134,532]
for i in NumberList:
        if i%2 == 0:
                print(i)

#3. Write a Python program to print only the odd numbers from a list.

print("3. To print only the odd numbers from a list.")
NumberList1 = [1213,2434,436,754,345,346,5432,99,77,987]
for i in NumberList1:
        if i%2 != 0:
                print(i)

#4. Write a Python program to find the sum of all numbers in a list.

print("4. To find the sum of all numbers in a list.")
sumList = [10,20,30,40,50,60,70,80,90,100]
count = 0
for i in sumList:
        count += i
print(count)

#5. Write a Python program to find the largest number in a list using a loop.

print("5. To find the largest number in a list using a loop.")
NumberList2 = [3845,35,654,5347,986,537]
greaterthan = NumberList2[0]
for i in NumberList2:
    if i > greaterthan:
        greaterthan = i
print(greaterthan)

#6. Write a Python program to find the smallest number in a list using a loop

print("6. To find the smallest number in a list using a loop")
lessList = [90,2,75,837,937,998,367,12]
lesserthan = lessList[0]
for i in lessList:
       if i < lesserthan:
              lesserthan = i
print(lesserthan)


#7. Write a Python program to count how many positive numbers are in a list.

print("7. To count how many positive numbers are in a list.")
positiveList = [-9,9,6,8,34,3,-7,-2]
count = 0
for i in positiveList:
       if i > 0:
              count = count + 1
print(count)


#8. Write a Python program to count how many negative numbers are in a list.

print("8.To count how many negative numbers are in a list.")
negativeList = [-9,-7,-5,8,-6,5,-4,-3,-1,4]
count = 0
for i in negativeList:
       if i < 0:
              count += 1
print(count)


#9.  Write a Python program to reverse a list without using the .reverse() method.

print("9. To reverse a list without using the .reverse() method.")
list = ["apple","banana","cherry","dragonfruit"] 
reverse_list = list[::-1]
print(reverse_list)


#10 .Write a Python program to count how many even and odd numbers are present in a list.

print("10. To count how many even and odd numbers are present in a list.")
new_list = [21,34,569,437,7593,8323,95766,35687,598]
oddcount = 0
evencount = 0
for i in new_list:
    if i%2 == 0:
        evencount += 1
    elif i%2 != 0:
        oddcount += 1
print("The count of odd is",oddcount)
print("The count of even is",evencount)


#11. Write a Python program to find and print the index of a specific value in a list.

print("11. To find and print the index of a specific value in a list")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers)
value = int(input("Enter the value to find: "))
print(numbers.index(value))


#12.Write a Python program to replace all negative numbers in a list with 0.

print("12. To replace all negative numbers in a list with 0.")
number1 = [-7,5,-5,2,-3,-10,-77,6,-4]
for i in range(len(number1)):
    if number1[i] < 0:
        number1[i] = 0
print(number1)


#13.Write a Python program to print all numbers greater than 50 from a list.

print("13. To print all numbers greater than 50 from a list.")
number2 = [10,20,30,40,50,60,70,80,90,100,110]
for i in range(len(number2)):
    if number2[i] > 50:
        print(number2[i])


#14. Write a Python program to create a new list containing the squares of each element

print("14. To create a new list containing the squares of each element")
number3 = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(number3)):
    number3[i] = number3[i] * number3[i]
print(number3)


#15. Write a Python program to print all duplicate values in a list.

print("15. To print all duplicate values in a list.")
nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]


for i in range(len(nums)):
    if nums.count(nums[i]) > 1 and nums.index(nums[i]) == i:
        print(nums[i])


#16.  Write a Python program to print list elements until the number 50 appears (stop when found).

print("16. To print list elements until the number 50 appears (stop when found)") 
nums = [10, 20, 30, 40, 50, 60, 70]
for n in nums:
    if n == 50:
        break
    print(n)


#17.  Write a Python program to count how many numbers in a list are divisible by 5.

print("17. To count how many numbers in a list are divisible by 5.")
number4 = [10, 23, 45, 50, 12, 75, 8]
count = 0
for n in number4:
    if n % 5 == 0:
        count = count + 1

print("Count of numbers divisible by 5:", count)


#18. Write a Python program to find the second largest number in a list using loops.

print("18. To find the second largest number in a list using loops.")
number5 = [10, 25, 3, 99, 75, 40]
largest = 0
second = 0
for n in number5:
    if n > largest:
        largest = n
for n in number5:
    if n > second and n != largest:
        second = n
print("Second largest number:", second)


#19. Write a Python program to check whether a list is sorted in ascending order.

print("19. To check whether a list is sorted in ascending order.")
number6 = [10, 20, 30, 40, 50]

for i in range(len(number6)-1):
    if number6[i] > number6[i+1]:
        print("List is not sorted")
        break
else:
    print("List is sorted")

#20. Write a Python program to find the sum of only the even numbers in a list.

print("20.To find the sum of only the even numbers in a list.")
nums = [10, 23, 8, 14, 7, 30]
sum_even = 0
for n in nums:
    if n % 2 == 0:
        sum_even = sum_even + n
print("Sum of even numbers:", sum_even)
 

