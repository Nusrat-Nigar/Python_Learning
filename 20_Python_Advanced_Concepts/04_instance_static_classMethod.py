class Employee:
    company = 'HP'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    # instance method
    def print_info(self):
        print (f'The name is {self.name} and the salary is {self.salary}')

    #static method: it doesn't required self. It doesn't use instance attribute or the instance of the object on which they are being called.
    @staticmethod
    def sum(a, b):
        return a+b
    
    # Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)


    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee('Jack', 23000)
e2 = Employee('Jill', 45000)
print(Employee.company)

e1.print_info()
e2.print_info()

print(e2.sum(5, 9))

e1.print_company()
e1.change_company('Dell')
e1.print_company()

print(Employee.company)
e1.change_company('Honda')
print(Employee.company)

