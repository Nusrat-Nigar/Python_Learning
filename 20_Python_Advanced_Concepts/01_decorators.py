# Decorators in python allows you to modify  or enhance functions and methods in a clean and readable way.

# Decorators is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function

def decorator(func):
    def wrapper():
        print('I am about to execute a function...')
        func()
        print('I have executed this function...')

    return wrapper

@decorator
def say_hello():
    print('hello')

say_hello()
# f = decorator(say_hello)
# f()

'''
f will look something like this
def f():
    print('I am about to execute a function...')
    print('hello')
    print('I have executed this function...')

'''
