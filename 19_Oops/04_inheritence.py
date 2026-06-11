# A child class (or subclass) inherits traits (attributes and methods) from its parents class (or super class).
class Animal:
    location = 'Australia'
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

# super(): Inside a child class, super() lets you call methods from the parent class.

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # we override the speak method
        super().speak()  # we are using the speak function of the parent class
        print('woof!')

class Cat(Animal):   # Cat also inherits from Animal
    def speak(self):
        print('Meow!')
        

a = Animal('Dog')
a.speak()

d = Dog('Bruno')
d.speak()
print(d.location) 