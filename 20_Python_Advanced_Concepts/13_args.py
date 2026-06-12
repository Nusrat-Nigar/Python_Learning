def sum(*args):  
#   print(args)  # args will be a tuple of all the values passed to sum
    total = 0
    for item in args:
        total += item

    return total

print(sum(4,5,8,44))
