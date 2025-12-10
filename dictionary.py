mydict = {
    "name" : "Kaaveri",
    "email":"kaaveri0329@gmail.com",
    "mobile":8610440867,
    "age":25,
    "Qualification" : "B.Tech",
    "Marks" : [90,80,70,98,87]
}
print(mydict)
print(type(mydict))
print(len(mydict))
print(mydict["mobile"])

print(mydict.get("email"))

print(mydict.keys())
print(mydict.values())

mydict["email"] = "kaaveri@gmail.com"
myData = mydict.update({"name":"kaaveri"})
print(mydict)

mydict.pop("name")
print(mydict)

for i in mydict:
    print(i, mydict[i])

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(f"{key}: {value}")

print(mydict.values)

