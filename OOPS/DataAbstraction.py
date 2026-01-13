from abc import ABC,abstractmethod

class Animals(ABC):
   
    @abstractmethod
    def sound(self):
        return "Cat Meows"

class dog(Animals):
    def sound(self):
        return "Dog Barks"
d=dog()
print(d.sound())
