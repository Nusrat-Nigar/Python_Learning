# map, filter and reduce are higher-order functions in python that operate on iterables (lists, tuples, etc.)

numbers = [1,2,4,6,8,9,0]

# def square(x):
#     return x*x

# map always returns a map object so we need to typecast it into list
new = list(map(lambda x: x*x, numbers))
print(new)