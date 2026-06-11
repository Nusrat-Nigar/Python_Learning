# Class: Class is a blueprint or template.Eg: Form for an exam that contains name, age, electives, father's name etc.

# Object: Specific instance created from the template (class). Eg: form which contains the data for the John Doe

class Employee:
    company = "HP"

    def getSalary(self):  # self is a way to reference the object of the class which is being created.
        return 34000
    
e = Employee()  # object creation of class Employee
print(e.getSalary()) # Employee e's getSalary method is called
print(e.company)