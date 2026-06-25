from functools import reduce
numbers = [1, 2, 3, 4, 5]

def prod(a, b):
    return a*b

res = reduce(prod, numbers)
print(res)