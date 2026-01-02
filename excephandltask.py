print("try - except - else - finally using function")

def demo():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))

        print(c)   # NameError (c is not defined)

        result = a / b

    except NameError:
        print("Name error: variable not defined__NameError_Block")

    except ZeroDivisionError:
        print("Cannot divide by zero__ZeroDivisibleError-Block")

    except ValueError:
        print("Invalid input Except__ValueError-Block")

    else:
        print("Result:", result,"Else-Block")

    finally:
        print("Function execution completed Finally-Block")

demo()
