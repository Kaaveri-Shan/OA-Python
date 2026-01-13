# # Compile time polymorphism (static polymorphism)
# # Method Overloading using default arguments

# # Python does not support traditional method overloading
# # So we simulate it using default parameters

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(10, 20))      # Uses default c = 0
print(obj.add(5, 6, 7))     # Uses all three arguments


# Runtime polymorphism (Method Overriding)


# Method overriding allows a child class to provide
# its own implementation of a method from the parent class

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    # Overriding the move method
    def move(self):
        return "Car is moving on roads"

class Bike(Vehicle):
    # Overriding and using super()
    def move(self):
        parent_move = super().move()   # Call parent method
        return f"{parent_move} with two wheels"

# Create objects
vehicle = Vehicle()
car = Car()
bike = Bike()

# Calling methods
print("Vehicle:", vehicle.move())
print("Car:", car.move())
print("Bike:", bike.move())
 