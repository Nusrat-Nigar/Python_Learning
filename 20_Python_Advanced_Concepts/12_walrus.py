def very_slow_func():
    print('Something.....')
    print('Something.....')
    print('Something.....')
    print('Something.....')
    return 90

# a = very_slow_func()
if ((a:=very_slow_func())>10):
    print(a)

else:
    print('it is not greater than 10')


# 2nd example:
while(data:=input('Enter the value: ')):
    print(data)
    if(data == 'q'):
        break

# 3rd way of writing
while(data:=input('Enter the value: ')) != 'Quit':
    print(f'You entered {data}')


words = ['Python', 'Rocks', 'Ai', 'Abs']

lengths = [n for w in words if(n := len(w)) < 4]
print(lengths)