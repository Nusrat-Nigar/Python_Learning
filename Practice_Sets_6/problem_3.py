class Animal:
    def sound(self):
        print('Some Sound....')

class Dog(Animal):
    def sound(self):
        print('Bark!')

animal = Animal()
animal.sound()

pug = Dog()
pug.sound()