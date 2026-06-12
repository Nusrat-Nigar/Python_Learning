from functools import reduce

numbers = [1, 23, 3, 5, 6, 7, 89, 4]
'''        [ 24, 3, 5, 6, 7, 89, 4]
            [ 27, 5, 6, 7, 89, 4]
             [32, 6, 7, 89, 4]
              [38, 7, 89, 4]
               [45, 89, 4]
                [134, 4]
                 [138]     '''

def sum(a,b):
    return a+b

new = reduce(sum, numbers)
print(new)