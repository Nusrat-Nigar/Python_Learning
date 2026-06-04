# 1. Positional arguments
def add(a,b):
    return a+b

print(add(4,5))


# 2. Default arguments
def greet(name = 'guest'):
    return f"Hello, {name}!"

print(greet())


# 3. Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age = 25, name = 'Nusrat')