#Create a tuple that contains an integer, a string, and a float.
print("1. Create a tuple that contains an integer, a string, and a float.")
My_Tuple = ("Kaaveri",24,"Kaaveri@gmail.com",65.7)
print(My_Tuple)

# Access the second element of the tuple (5, 10, 15, 20).
print("2.Access the second element of the tuple (5, 10, 15, 20).")
My_Tuple2 = (5,10,15,20)
print(My_Tuple2[1])

# Slice the tuple (1, 2, 3, 4, 5) to get the last two elements.
print("3.Slice the tuple (1, 2, 3, 4, 5) to get the last two elements.")
My_Tuple3 = (1,2,3,4,5)
sliced_tuple = My_Tuple3[3:5]
print(sliced_tuple)

# Concatenate the tuples (1, 2) and (3, 4).
print("4.Concatenate the tuples (1, 2) and (3, 4).")
tuple1 = (1,2)
tuple2 = (3,4)
My_Tuple4 = tuple1 + tuple2
print(My_Tuple4)

# Repeat the tuple (7, 8) three times.
print("5.Repeat the tuple (7, 8) three times.")
My_Tuple5 = [7,8]
repeated_tuple = My_Tuple5 * 3
print(repeated_tuple)

# Check if 15 is present in the tuple (10, 20, 15, 25).
print("6.Check if 15 is present in the tuple (10, 20, 15, 25).")
My_Tuple6 = [10,20,15,25]
if 15 in My_Tuple6:
    print("15 is present in the tuple : ",My_Tuple6)

# Find the length of the tuple (3, 6, 9, 12).
print("7.Find the length of the tuple (3, 6, 9, 12).")
My_Tuple7 = (3, 6, 9, 12)
print(len(My_Tuple7))

#  Find the maximum and minimum values in the tuple (4, 1, 8, 3).
print("8. Find the maximum and minimum values in the tuple (4, 1, 8, 3).")
My_Tuple8 = (4,1,8,3)
print("Minimum value is : ",min(My_Tuple8))
print("Maximum value is : ",max(My_Tuple8))

# Convert the list [1, 2, 3, 4] into a tuple.
print("9.Convert the list [1, 2, 3, 4] into a tuple.")
My_List = [1,2,3,4]
ConvertedTuple = tuple(My_List)
print(ConvertedTuple,"Coverted to tuple")

# Convert the tuple (10, 20, 30) into a list.
print("10.Convert the tuple (10, 20, 30) into a list.")
My_Tuple10 = (10,20,30,40,50)
ConvertedList = list(My_Tuple10)
print(ConvertedList,"converted to list")

# Find the index of the element 30 in the tuple (10, 20, 30, 40).
print("11.Find the index of the element 30 in the tuple (10, 20, 30, 40)")
My_Tuple11 = (10, 20, 30, 40)
print(My_Tuple11.index(30))

# Count how many times 2 appears in the tuple (2, 3, 2, 4, 2).
print("12.Count how many times 2 appears in the tuple (2, 3, 2, 4, 2)")
My_Tuple12 = (2, 3, 2, 4, 2)
count = 0
for i in My_Tuple12:
    if i == 2:
        count +=1
print(count)

# Unpack the tuple (100, 200, 300) into three separate variables.
print("13.Unpack the tuple (100, 200, 300) into three separate variables.")
My_Tuple13 = (100,200,300)
print(My_Tuple13,"Packed Tuple")
(n1,n2,n3) = My_Tuple13
print(n1,"unpacked")
print(n2,"unpacked")
print(n3,"unpacked")

# Swap the values of two tuples (1, 2) and (3, 4)
print("14.Swap the values of two tuples (1, 2) and (3, 4)")
tuple11 = (1, 2)
tuple22 = (3, 4)
tuple11,tuple22 = tuple22,tuple11
print("tuple11:", tuple11)
print("tuple22:", tuple22)

#Create a tuple that contains two other tuples (1, 2) and (3, 4).
print("15.Create a tuple that contains two other tuples (1, 2) and (3, 4).") 
tup1 = (1,2)
tup2 = (3,4)
combinedtuple = (tup1) + (tup2) + (5,6)
print(combinedtuple,"Combined 2 tuple in another tuple")

# Access the number 4 from the nested tuple ((1, 2), (3, 4)).
print("16.Access the number 4 from the nested tuple ((1, 2), (3, 4))")
tuple16 = ((1, 2), (3, 4))
print(tuple16[1][1],"is being accessed")

# Find the sum of all numbers in the tuple (5, 10, 15).
print("17.Find the sum of all numbers in the tuple (5, 10, 15).")
tuple17 = (5, 10, 15)
total = 0
for i in tuple17:
    total += i
print(total)

# Sort the elements of the tuple (40, 10, 30, 20) in ascending order.
print("18. Sort the elements of the tuple (40, 10, 30, 20) in ascending order.")
tuple18 = (40, 10, 30, 20)
sorted18 = tuple(sorted(tuple18))
print(sorted18)

# Reverse the elements of the tuple (1, 2, 3, 4, 5).
print("19.Reverse the elements of the tuple (1, 2, 3, 4, 5).")
tuple19 = (1, 2, 3, 4, 5)
reverse19 = tuple19[::-1]
print(reverse19)

# Check if all elements in the tuple (5, 5, 5, 5) are identical.
print("20.Check if all elements in the tuple (5, 5, 5, 5) are identical.")
tuple20 = (5, 5, 5, 5)
print(len(set(tuple20)) == 1)
