num = int(input("Enter anumber between 1 to 10: "))
match num:
    case 1:
        print("You won a trophy")
    case 3:
        print("You won a 50$")
    case 5:
        print("You won a TV")
    case _:
        print("Better luck next time!")             
