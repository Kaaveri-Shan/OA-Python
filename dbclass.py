from bson import ObjectId
from pymongo import MongoClient

mongoURL = MongoClient("mongodb://localhost:27017")

myDB = mongoURL["GurudevProject"]

myCollection = myDB["userDetail"]

userData = {
    "name":"Ravi",
    "mobile":8435354353,
    "age":17,
    "address":"bbb street"
}

def createUser(user):
    data = myCollection.insert_one(user)
    print("user created successfully")


# createUser(userData)

students = [
    {
    "name":"Naren",
    "mobile":8435354353,
    "age":17,
    "address":"ccc street"
    },
    {
    "name":"Arul kevin",
    "mobile":8435354353,
    "age":17,
    "address":"ddd street"
    },
     {
    "name":"Sanjay",
    "mobile":485734534,
    "age":17,
    "address":"eee street"
    },

]

def createStudents(s):
    studentData = myCollection.insert_many(s)
    print("students created successfully")

# createStudents(students)

# get all data
def getAllData():
    userData = myCollection.find({})
    for i in userData:
        print(i)
# getAllData()

# get specific user data

def getSpecificUser(userId):
    try:
        checkuser = myCollection.find_one({"_id":ObjectId(userId)})
        if checkuser:
            print(checkuser)
        else:
            print("user is not found")
    except Exception as e:
        print("something went wrong",e)

# getSpecificUser("685b84e259eda586cdf1b24e")


# update a record

newValue = {
    "name":"Guru dev"

}
def updateUser(userId):
    try:
        checkUser = myCollection.find_one_and_update({"_id":ObjectId(userId)},{"$set":newValue})
        if checkUser :
            print("User data updated successfully")
        else:
            print("User not found")

    except Exception as e:
        print("something went wrong",e)

# updateUser("685b838646ea599b0b4bcc35")

# delete

def getDeleteUser(userId):
    try:
        checkuser = myCollection.find_one_and_delete({"_id":ObjectId(userId)})
        if checkuser:
            print("user data deleted")
        else:
            print("user is not found")
    except Exception as e:
        print("something went wrong",e)

# getDeleteUser("685b838646ea599b0b4bcc35")

def query():
    query={"age":{"$gte":17}}
    values=myCollection.find(query)
    for i in values:
        print(i)
    # values1=myCollection.find({}).limit(2)
    # for x in values1:
    #     print(x)
# query()

def sorting():
    data = myCollection.find().sort("name",-1)
    for i in data:
        print(i)
sorting()