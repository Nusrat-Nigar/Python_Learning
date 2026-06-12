# Dunder (Double underscore) Methods. (eg: __init__, __str__, __add__)
# These methods allow you to define how your objects interact with built-in python operators, functions and language constructs.
# Provide a way to implement operator overloading.

class Employee:
    company = 'HP'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'The name is {self.name} and the salary is {self.salary}'

    def __repr__(self):
        return f'name: {self.name}\nsalary: {self.salary}'
    
    def __len__(self):
        return len(self.name)

e = Employee('Nusrat', 23000)
print(e.name, e.salary)

print(str(e))  # mostly used by user
print(repr(e)) # mostly used by developer who is using to debug the code 

print(len(e))