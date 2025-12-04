##implicit
x = 10
y = 12.8
print(x+y)
print(type(x+y))

##explicit
##str to int
value1 = input("Enther the value1 : ")
value2 = input("Enther the value2 : ")
ChangeValue1 = int(value1)
ChangeValue2 = int(value2)
print(type(ChangeValue1),type(ChangeValue2))
print(ChangeValue1+ChangeValue2)
##int to str
number = 9998
print("number datatype is :",(type(number)),"it has been changed to",(type(str(number))))

##bool to str
isLightOn = True
changeisLightOnTo = str(isLightOn)
print("isLightOn datatype is: ",(type(isLightOn)),"it has been changed to",(type(changeisLightOnTo)))

##bool to int
bool_int = int(isLightOn)
print(bool_int)
print("the datatype is :",(type(isLightOn)),"it has been changed to",(type(bool_int)))

##set to tuple
MySet = {"Kaaveri","Sankar","Praveen","Bavany"}
print(MySet)
ChangedMySet = tuple(MySet)
print("THE CHANGED SET : ",ChangedMySet)
print("the datatype is :",(type(MySet)),"it has been changed to",(type(ChangedMySet)))

##set to list
ChangedMySet1 = list(MySet)
print("THE CHANGED SET : ",ChangedMySet1)
print("the datatype is :",(type(MySet)),"it has been changed to",(type(ChangedMySet1)))

##Tuple to List
MyTuple = ("KAAVERI",24,"KAA@2025")
print(MyTuple)
ChangedMyTuple = list(MyTuple)
print("The Changed tuple is",ChangedMyTuple)
print("the datatype is :",(type(MyTuple)),"it has been changed to",(type(ChangedMyTuple)))

##Tuple to Set
ChangedMyTuple1 = set(MyTuple)
print("The Changed tuple is",ChangedMyTuple1)
print("the datatype is :",(type(MyTuple)),"it has been changed to",(type(ChangedMyTuple1)))

##List to Tuple
MyList = ["a","b","c","d"]
ChangedMyList = tuple(MyList)
print("The Changed list is",ChangedMyList)
print("the datatype is :",(type(MyList)),"it has been changed to",(type(ChangedMyList)))

##List to Set
ChangedMyList1 = set(MyList)
print("The Changed list is",ChangedMyList1)
print("the datatype is :",(type(MyList)),"it has been changed to",(type(ChangedMyList1)))





                                                                






























