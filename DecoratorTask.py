print("\n")
print("1.Passing Func as a Parameter")
def message():
    print("Learning Python\n")

def execute(func):
    func()

execute(message)

print("2.Decorator using @")
def check(display):
    def wrapper():
        print("Start")
        display()
        print("End\n")
    return wrapper

@check
def display():
    print("Welcome")

display()

print("3.Without using @")
def validate(show):
    def wrapper():
        print("Validating...")
        show()
    return wrapper

def show():
    print("Data displayed\n")

show = validate(show)
show()

print("4.Chaining Decorator")
def decor_a(func):
    def wrapper():
        print("Decorator A")
        func()
    return wrapper

def decor_b(task):
    def wrapper():
        print("Decorator B")
        task()
    return wrapper

@decor_a
@decor_b
def task():
    print("Task executed\n")

task()

print("5.Example of decoration in real time attendance calculator")
def attendance_check(func):
    def wrapper(days):
        try:
            if days < 0:
                raise ValueError("Invalid days")

            for i in range(1, 4):
                print("Verifying record", i)

            if days >= 75:
                func(days)
            else:
                print("Not eligible due to low attendance")

        except ValueError as e:
            print("Error:", e)

        else:
            print("Verification completed")

        finally:
            print("Attendance process closed")

    return wrapper


@attendance_check
def allow_exam(days):
    print("Allowed to write exam. Attendance:", days, "%")


allow_exam(80)
print()
allow_exam(60)
print()
allow_exam(-5)


