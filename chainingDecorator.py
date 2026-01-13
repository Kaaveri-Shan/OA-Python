# def uppercase(func):
#     def wrapper(name):
#         return func(name).upper()
#     return wrapper

# def greet_prefix(func):
#     def wrapper(name):
#         return "Hello " + func(name)
#     return wrapper

# @uppercase
# @greet_prefix
# def greet(name):
#     return name

# print(greet("kaaveri"))




def decor1(func):                    # decorator function decor1 that takes a function as argument
    def wrapper():                   # wrapper function that adds extra behavior
        print("Before function")     # code executed before the actual function call
        func()                       # calls the function passed to the decorator
        print("After function")      # code executed after the function call
    return wrapper                   # returns wrapper, replacing the original function

def decor2(func):                    # second decorator function
    def wrapper():                   # wrapper function for decor2
        print("Starting execution")  # code executed before the function call
        func()                       # calls the function received by decor2
        print("Execution finished")  # code executed after the function call
    return wrapper                   # returns wrapper function

@decor1                              # applies decor1 (outer decorator)
@decor2                              # applies decor2 (inner decorator)
def display():                       # original function definition
    print("Hello World")             # actual function body

display()                            # calls the chained decorated function

# Execution order:
# decor1 → decor2 → display → decor2 → decor1

# output:
# Before function          # printed by decor1 before calling the inner function
# Starting execution       # printed by decor2 before calling display()
# Hello World              # printed by the original display() function
# Execution finished       # printed by decor2 after display() execution
# After function           # printed by decor1 after the inner function completes
