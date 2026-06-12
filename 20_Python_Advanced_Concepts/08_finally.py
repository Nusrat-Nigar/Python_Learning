def divide(a, b):
    try:
        c = a/b
        print(c)
        return c
        
    except Exception as e:
        print(e)
        return None

    # This is always executed no matters if try completely executes or not ( finally generally works in the functional case because outside the function normal print statement will also execute always)
    finally:
        print('This is always executed')

a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
divide(a, b)