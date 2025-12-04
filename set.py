#Set is denites in {}
#Key characteristics # unordered, not allow duplicated, unindexed

#Creation of set
print("1.Creation of set")
My_Set = {"aaa","bbb","ccc","ddd"}
print(My_Set)

#Creation of set using Constructor
print("2.Creation of set using constructor")
MySet1 = set((10,20,30,40,50,60,70))
print(type(MySet1))
print(MySet1)

print("3.Add an element to the set")
MySet1.add(80)
print(MySet1,"Added 80")

print("4.update - Add an Multiple element to the set")
MyList1 =["Kaaveri",8610440867,24,"B.Tech"]
MySet1.update(MyList1)
print(MySet1,"updated")

print("5.Remove - Delete an element in the set, throw keyError if value is not present")
MySet1.remove(10)
print(MySet1,"Remove 10 from set")

print("6.Discard - Delete an element in the set,not throw keyError if value is not present")
MySet1.discard(1000)
print(MySet1,"Discard is given")

print("7.Clear the entire set")
My_Set.clear()
print(My_Set)

print("8.Pop - Deletes a random element in the set")
MySet1.pop()
print(MySet1)

#union() - Returns all elements from both sets.
print("9.Union")
set1 = {8,6,1,0,4,7}
set2 = {8,7,5,4,3,6,9,0}
print(set1.union(set2))

# intersection() - returns the commom data from both sets
print("10.Intersection")
print(set1.intersection(set2))

# difference() - Elements in the first set but not in the second.
print("11.Difference")
print(set1.difference(set2))

# symmetric_difference() - Elements in either set but not both.
print("12.Symmentric Difference")
print(set1.symmetric_difference(set2))


# Relationship Test Methods

# issubset() - Checks subset
print("13.IsSubset")
print({1,2,3}.issubset({1, 2, 3}))

# issuperset()
print("14.IsSuperSet")
print({10,20,30,40}.issuperset({20,30,10}))

# isdisjoint() Returns True if no elements are common.
print("15.IsDisjoint")
print({"a","b","c"}.isdisjoint({"d","e","f"}))
