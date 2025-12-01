user_name = "kaaveri"
password = "kaaveri@123"
Find_user = input("Enter the username : ")
Find_pass = input("Enter the password : ")
if Find_user != "" and Find_pass != "":
    if Find_user == user_name:
        if Find_pass == password:
            print("Log in successful")
        else:
            print("Invalid password")
    else:
        print("Invalid username")
else:
    print("Username and password should not be empty")
