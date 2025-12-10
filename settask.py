print("1.Create a set from a list of integers.")
my_list = [1, 2, 3, 2, 4]
my_set = set(my_list)
print(my_set)

print("2.Check if an element exists in a set.")
my_set = {1, 2, 3}
print(2 in my_set)


print("3.Add an element to a set.")
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)


print("4.Remove an element from a set.")
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)


print("5.Use discard() to remove an element, without throwing an error if it does not exist.")
my_set = {1, 2, 3}
my_set.discard(5)  
print(my_set)


print("6.Find the union of two sets.")
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))


print("7.Find the intersection of two sets.")
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))


print("8.Find the difference of two sets.")
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))


print("9.Find the symmetric difference of two sets.")
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))


print("10.Find the subset relationship between two sets.")
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))


print("11.Find the superset relationship between two sets.")
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))

# Remove all elements from a set.
print("12.Remove all elements from a set.")
my_set = {1, 2, 3}
my_set.clear()
print(my_set)

# Iterate through a set
print("13.Iterate through a set")
my_set = {1, 2, 3}
for x in my_set:
    print(x)

# Convert a set into a list.
print("14.Convert a set into a list.")
my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)

# Check if two sets are disjoint (no common elements)
print("15.Check if two sets are disjoint (no common elements).")
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))

# Create a set from a string (unique characters).
print("16.Create a set from a string (unique characters).")
s = "banana"
char_set = set(s)
print(char_set)


# Find the length of a set.
print("17. Find the length of a set.")
my_set = {1, 2, 3}
print(len(my_set))


# Use set comprehension to create a set of squares of numbers from 1 to 5
print("18.Use set comprehension to create a set of squares of numbers from 1 to 5.")
squares = {x*x for x in range(1, 6)}
print(squares)


# Check if a set is empty.
print("19.Check if a set is empty.")
my_set = set()
print(len(my_set) == 0)


# Find the unique elements from two lists using sets.
print("20.Find the unique elements from two lists using sets.")
list1 = [1, 2, 3]
list2 = [2, 3, 4]
unique = set(list1) | set(list2)
print(unique)
