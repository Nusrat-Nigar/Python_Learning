t = (3, 12, 1, 6, 56, 12, 1)

print(t.count(12)) # print number of occurence of the given number

print(t.index(1))  # print the index of first occurence of the given number

# Why use tuples?
# - faster than lists (since they are immutable)
# - used as dictionary keys (since they are hashable)
# - safe from unintended modification
