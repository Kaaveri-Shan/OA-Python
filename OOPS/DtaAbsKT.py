from abc import ABC, abstractmethod

class Animal(ABC):            # Abstract class
    
    @abstractmethod
    def sound(self):          # Abstract method
        print("Cat Meows")
    
class Dog(Animal):
    
    def sound(self):
        super().sound()
        return "Dog barks"

d = Dog()
print(d.sound())


# class ATM(ABC):                      # Abstract class (ATM interface)
    
#     @abstractmethod
#     def withdraw(self, amount):      # What ATM can do
#         pass                         # How it is done is hidden

# class BankATM(ATM):                  # Bank implements ATM
    
#     def withdraw(self, amount):      # Actual implementation
#         print("Please collect cash:", amount)



