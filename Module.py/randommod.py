import random

# Random number from 0.0 to 1.0
print(random.random())


# gives a random int number from the given value (a,b) 

print(random.randint(1, 20))
dice = random.randint(1, 6)
print("Dice Number:", dice)

# Generates a random number from a given range

print(random.randrange(1, 20, 2))

# Selects a random element from a list, tuple, or string

names = ["Kaaveri", "Praveen", "Barath","Sandhiya","BK"]
print(random.choice(names))

# Shuffles the elements of a list randomly

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

#Returns k unique random elements 

numbers = [10, 20, 30, 40, 50]
print(random.sample(numbers, 3))

#Generates a random float number between a and b 

print(random.uniform(1.5, 10.5))


