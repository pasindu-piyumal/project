import random

number = random.randint(1, 100)

print("Guess the number (You have only five attempts)")

for i in range(1,6):
    input_number = int(input(f"Attempt {i}: "))
    if (input_number == number):
        print("You won the game. Congratulations")
        break
    elif (input_number > number):
        print("Number is big")
    else:
        print("Number is small")
else:
    print("You lost the game")
