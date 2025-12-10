print("1.Given two lists, return the set of common elements that appear more than once in both lists.")
set1 = set()
l1 = [1,2,2,3,3]
l2 = [2,2,3,4,4]
for x in l1:
    if l1.count(x) > 1 and x in l2 and l2.count(x) > 1:
        set1.add(x)
print(set1)

print("2.Create a set of unique words from a sentence, where words are separated by spaces and punctuation marks should be ignored.")
sentence = "Hello, world! Hello again."
clean = ""
for ch in sentence:
    if ch.isalnum() or ch == " ":
        clean += ch.lower()
words = clean.split()
set2 = set(words)
print(set2)

print("3.Write a function that takes a list of numbers and returns the largest subset such that the sum of the subset is even.")
nums = [1,2,3,4]
total = sum(nums)
if total % 2 == 0:
    set3 = set(nums)
else:
    smallest_odd = None
    for x in nums:
        if x % 2 == 1:
            if smallest_odd is None or x < smallest_odd:
                smallest_odd = x
    nums.remove(smallest_odd)
    set3 = set(nums)
print(set3)

print("4.Given a set of integers, write a function that returns a new set containing all subsets of the original set.")
s = {1,2,3}
s = list(s)
set4 = []
for mask in range(2 ** len(s)):
    subset = set()
    for i in range(len(s)):
        if mask & (1 << i):
            subset.add(s[i])
    set4.append(subset)
print(set4)

print("5.Check if two sets are equal, considering their elements but ignoring the order (i.e., set equality).")
a = {1,2,3}
b = {3,2,1}
set5 = (a == b)
print(set5)

print("6. Write a program that finds the intersection of multiple sets.")
sets = [{1,2,3},{2,3,4},{3,4,5}]
set6 = sets[0].copy()
for s in sets[1:]:
    set6 = set6.intersection(s)
print(set6)

print("7.Find the set difference of multiple sets.")
sets = [{1,2,3},{2},{3}]
set7 = sets[0].copy()
for s in sets[1:]:
    set7 = set7 - s
print(set7)

print("8.Given a list of sets, write a program to return the set containing elements that are present in every set in the list.")
sets = [{1,2,3},{1,3,5},{1,7,3}]
set8 = sets[0].copy()
for s in sets[1:]:
    set8 = set8.intersection(s)
print(set8)

print("9.Write a function that checks if a set of strings forms a palindrome when concatenated together.")
strings = {"a","b","a"}
text = ""
for s in strings:
    text += s
set9 = (text == text[::-1])
print(set9)

print("10.Count subsets with sum divisible by k")
s = {1,2,3}
s = list(s)
k = 2
set10 = 0
for mask in range(2 ** len(s)):
    total = 0
    for i in range(len(s)):
        if mask & (1 << i):
            total += s[i]
    if total % k == 0:
        set10 += 1
print(set10)

print("11.Longest consecutive sequence")
nums = [100,4,200,1,3,2]
s = set(nums)
set11 = 0

for num in s:
    if (num - 1) not in s:
        current = num
        length = 1
        while (current + 1) in s:
            current += 1
            length += 1
        if length > set11:
            set11 = length
print(set11)

print("12.Symmetric difference only for repeated elements")
a = {1,2,3}
b = {3,3,4,4}

sym = (a - b) | (b - a)
combined = list(a) + list(b)
set12 = set()
for x in sym:
    if combined.count(x) > 1:
        set12.add(x)
print(set12)

print("13.Pair that sums to target")
s = {1,2,3,4}
target = 5
set13 = False
for x in s:
    for y in s:
        if x != y and x + y == target:
            set13 = True
print(set13)

print("14.Proper Subset")
a = {1,2}
b = {1,2,3}

set14 = (a < b)
print(set14)

print("15.Elements only in first set")
first = {1,2,3}
others = [{2,4},{3,5}]
all_other = set()
for s in others:
    all_other = all_other.union(s)
set15 = first - all_other
print(set15)

print("16.Subsets whose sum is prime")
# s = {1,2,3}
# s = list(s)
# print(list(s))

print("17.Create a set of all permutations of a given list of characters.")
chars = ['a', 'b', 'c']
perms = [""]
for ch in chars:
    new = []
    for p in perms:
        for i in range(len(p) + 1):
            new += [p[:i] + ch + p[i:]]
    perms = new
print(perms)

print("18.Check if a set contains a subset")
s = {3, 4, 6, 7}
target = 10
found = False
nums = list(s)

for mask in range(1, 1 << len(nums)):
    total = 0
    for i in range(len(nums)):
        if mask & (1 << i):
            total = total + nums[i]
    if total == target:
        found = True

print(target)
































































