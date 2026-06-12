class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        f =  self.name.split(' ') # it will return the list
        print(f)
        return f[0]
    
    @first_name.setter
    def first_name(self, first):
        f = self.name.split(' ')
        new_name = f'{first} {f[1]}'
        self.name = new_name

e = Employee('Jack Doe', 23890)
# print(e.first_name())
# e.set_first_name('John')
# print(e.name)

print(e.first_name)  # first_name is a function but it looks like a property because we are using a property decorator
e.first_name = 'John'
print(e.name)
# e.project = 6
# print(e.project)