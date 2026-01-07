print("1.Decorator using @ symbol")
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()

print("2.Decorator using @ Passing Function as argument")
def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero")
        else:
            return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    print(a / b)

divide(10, 2)
divide(5, 0)


print("3.Real Time Example using decorator @")
def login_required(func):
    def wrapper(username, password):
        correct_username = "Kaaveri"
        correct_password = "Kaaveri@123"

        if username == "" or password == "":
            print("Username or password cannot be empty")
        elif username == correct_username and password == correct_password:
            func(username)
        else:
            print("Access denied")
    return wrapper


@login_required
def dashboard(username):
    print("Login successful")
    print("Welcome to dashboard,", username)


# User input
username = input("Enter username: ")
password = input("Enter password: ")

dashboard(username, password)



