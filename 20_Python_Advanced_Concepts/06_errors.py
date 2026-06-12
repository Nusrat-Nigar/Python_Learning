# while True:
#     try:
#         a = int(input('Enter First Number: '))
#         b = int(input('Enter Second Number: '))
#         print(f'The division is {a/b}')

#     except ValueError:
#         print("Please don't perform bad typecasts")

#     except ZeroDivisionError:
#         print("Don't devide by zero")

#     except Exception as e:
#         print('Unknown error occured!', e)


a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))

if b==0:
    raise ValueError("Please don't devide by zero")
print(f'The division is {a/b}')
