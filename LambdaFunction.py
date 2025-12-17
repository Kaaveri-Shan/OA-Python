# Lambda Function
# Small,Anonymous(Nameless) in single Line
# Only one expression
# No return Keyword

# SYNTAX
# lambda arguments : Expression(or)Conditions

# Example

add = lambda x : x+20
print(add(10))

sub = lambda x : x-20
print(sub(90))

mul = lambda x : x * 2
print(mul(90))

div = lambda x : x/2
print(int(div(90)))

name = lambda fname,lname : fname+lname
print(name("Kaaveri","Sankar"))

# map() function
# Applies a function to each element of an iterable (list, tuple, etc.).

# SYNTAX
# map(function, iterable)

numbers = [1, 2, 3, 4,5]

result = map(lambda x: x*x, numbers)
print(list(result))


#filter()
# Selects elements from an iterable based on a condition

# SYNTAX
# filter(function, iterable)

nums = [37,53,63,23,66,68,88,23,34,77]

above50 = filter(lambda n : n>50, nums)
print(list(above50))

# reduce()
# Reduces all elements of an iterable to a single value.

# ⚠️ reduce() is in the functools module.

# SYNTAX
# from functools import reduce
# reduce(function, iterable)

from functools import reduce

numbers = [1, 2, 3, 4,5]

result = reduce(lambda x, y: x + y, numbers)
print(result)

