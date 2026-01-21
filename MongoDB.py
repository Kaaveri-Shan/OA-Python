from bson import ObjectId
from pymongo import MongoClient

mongoUrl = MongoClient("mongodb://localhost:27017")

myDB = mongoUrl["OA-Python"]

myCollection = myDB["PythonTasks"]

userData = {
    "name":"Kaaveri",
    "mobile":87534584353,
    "email":"kaveri@gmail.com",
    "address":"No:4, aaa street"
}

def createUser(user):
    print(user)
    data = myCollection.insert_one(user)
    print("Data created successfully")

# createUser(userData)

usersData = [
    {
        "name": "Barath",
        "mobile": "9876543210",
        "email": "barath@gmail.com",
        "address": "No:10, ABC Street"
    },
    {
        "name": "Praveen",
        "mobile": "9123456789",
        "email": "praveen@gmail.com",
        "address": "No:11, DEF Street"
    },
    {
        "name": "Sankar",
        "mobile": "9988776655",
        "email": "sankar@gmail.com",
        "address": "No:12, GHI Street"
    },
    {
        "name": "Bavany",
        "mobile": "9090909090",
        "email": "bavany@gmail.com",
        "address": "No:13, JKL Street"
    },
    {
        "name": "Sandhiya",
        "mobile": "9567891234",
        "email": "saandhiya@gmail.com",
        "address": "No:14, MNO Street"
    }
]

def createUsers(users):
    result = myCollection.insert_many(users)
    print("Users inserted successfully")
    # print("Inserted IDs:", result.inserted_ids)

# createUsers(usersData)
def getAllData():
    userData = myCollection.find({})
    for i in userData:
        print(i)
# getAllData()

def getSpecificUser(userId):
    try:
        checkuser = myCollection.find_one({"_id":ObjectId(userId)})
        if checkuser:
            print(checkuser)
        else:
            print("user is not found")
    except Exception as e:
        print("something went wrong",e)

# getSpecificUser("6965dbd52b59f48fc2db0986")

# update a record

newValue = {
    "name":"KaaveriSankar"

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

# updateUser("6965daf0dd4637e99df2862f")

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

# getDeleteUser("6965dbd52b59f48fc2db0987")

def query():
    query={"Age":{"$gt":25}}
    values=myCollection.find(query)
    for i in values:
        print(i)
    # values1=myCollection.find({}).limit(2)
    # for x in values1:
    #     print(x)
# query()

def sorting():
    data = myCollection.find().sort("name",1)
    for i in data:
        print(i)
sorting()