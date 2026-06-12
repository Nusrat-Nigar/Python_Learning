def is_greater_than_9(x):
    if x>9:
        return True
    
    else:
        return False
    
a = [1, 4, 6, 34, 26, 90, 3, 7]
# filter always returns a filter object so we need to typecast it into list
new = list(filter(is_greater_than_9, a))
print(new)