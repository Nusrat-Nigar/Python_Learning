class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f'Name: {self.name} and age: {self.age}')


person = Person('Rahul', 35)
print(person.name, person.age)

person.details()



