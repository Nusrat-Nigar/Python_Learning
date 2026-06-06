def sum(a,b):
    print("Hey, I am summing")
    c = a+b
    global z  # please modify global z
    z = 0  # this will refer to global z and not create a local variable 
    return c

z = 3
print(sum(3,7))
print(z)

# Imp Note : Can you modify a global variable inside a function? ---> yes, we can but we'll have to use global
# accessive use of global is discouraged because it will create mess up.