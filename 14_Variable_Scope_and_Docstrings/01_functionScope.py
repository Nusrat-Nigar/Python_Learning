def add(a,b):
    # a,b and c are local variables we can't access them outside of the function.
    c = a+b
    print(z)
    return c


z = 8 # z is a global variable it can be access anywhere 
print(add(4,6)) 
# print(c)# it will throw error because c is not in scope of main function.