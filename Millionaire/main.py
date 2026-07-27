question = [
    ["What is the capital of France?", "London", "Berlin", "Paris", "Madrid", 3],
    ["Which planet is known as the Red Planet?", "Jupiter", "Mars", "Saturn", "Venus", 2],
    ["Who wrote 'Romeo and Juliet'?", "Mark Twain", "Charles Dickens", "William Shakespeare", "Leo Tolstoy", 3],
    ["What is the largest ocean on Earth?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["Which language is primarily used for Android app development?", "Swift", "Python", "Java", "C++", 3],
    ["How many continents are there on Earth?", "6", "8", "7", "5", 3],
    ["Which gas do plants absorb from the atmosphere?", "Nitrogen", "Hydrogen", "Carbon Dioxide", "Oxygen", 3],
    ["What is the square root of 64?", "7", "9", "6", "8", 4],
    ["Which country is famous for the Eiffel Tower?", "Spain", "France", "Germany", "Italy", 2]
]
prizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
i = 0

for question in question:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    answer = int(input("Enter your answer (1-4): "))
    
    if answer == question[5]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is option {question[5]}.")
        print('Better luck next time!')
        break

    print(f"You have won ${prizes[i]} so far.")
    i += 1