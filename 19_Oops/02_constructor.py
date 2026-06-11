# A constructor is used to initialize the object

class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

    def getSalary(self):  # self is a way to reference the object of the class which is being created.
        return self.salary
    
    def getInfo(self):
        print(f'The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years')
    
e1 = Employee(34000, 'John Doe', 4)
print(e1.getSalary())
e1.getInfo()