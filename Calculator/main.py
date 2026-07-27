try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Which kind of operation you want to perform?\n1. + for Addition\n2. - for Subtraction\n3. * for  Multiplication\n4. / for Division")
    o = input("Enter your choice: ")
    match o:
        case "+":
            print(f"The sum of {a} and {b} is {a + b}")
        case "-":
            print(f"The difference of {a} and {b} is {a - b}")
        case "*":
            print(f"The product of {a} and {b} is {a * b}")
        case "/":
            print(f"The division of {a} and {b} is {a / b}")
        case default:
            print("Invalid operation")
except Exception as e:
    print("Error: Enter the valid numbers", e)

