num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opr = input("Choose operation: ")
match opr:
    case '+':
        print("The addition of these two numbers is: ", num1+num2)
    case '-':
        print("The difference of these two numbers is: ", num1-num2)
    case '*':
        print("The production of these two numbers is: ", num1*num2)
    case '/':
        print("The devision of these two numbers is: ", num1/num2)
    