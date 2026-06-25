from time import time
def timer(func):
    def wrapper(n):
        t1 = time()
        res = func(n)
        t2 = time()
        print(t2-t1)
        return res

    return wrapper

@timer
def Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum 

print(Sum(1000000))