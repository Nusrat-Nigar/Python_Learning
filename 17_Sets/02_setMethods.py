s  = {'cherry',5,'banana',9}
s.add('Mango')
print(s)

s.remove('cherry')
print(s)

s.discard('cherry') # No error if element not found in the set.
print(s)

s.remove(8) # throws an error because element is not present in the set.

s.pop() # removes random element
print(s)
