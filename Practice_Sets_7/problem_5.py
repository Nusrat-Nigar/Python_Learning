class NegativeNumberError(Exception):  # manually define the custom Exception class in case of absence of Exception type
    pass

try:
    num = int(input('Enter a number: '))

    if num<0:
        raise NegativeNumberError('Negative number not allowed! ')
    
    res = 45/num
    print(f'the result is: {res}')

except ValueError:
    print('Error: please enter the correct value typecast')

except ZeroDivisionError:
    print("Error: Don't divide by zero")

except NegativeNumberError as e:
    print(f'Error: {e}')