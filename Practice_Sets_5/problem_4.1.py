my_set = {1, 2, 3, 4, 3}
print(my_set)  # duplicates remove

my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)

my_set.remove(4) # throw error if it will not present in the set
print(my_set)