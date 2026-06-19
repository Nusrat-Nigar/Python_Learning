coordiates = (10, 20)
print(coordiates)

# coordiates[0] = 50 (it will make error because tuple is immutable(unchangable) )

my_list = list(coordiates)
my_list[0] = 50

my_tuple = tuple(my_list)
print(my_tuple)
