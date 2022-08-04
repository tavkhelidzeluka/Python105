"""
0 - 100

25? greater
45? less
35? greater
37? correct!
"""

# 1. taking a random number between [0 - 100] +
# 2. take user input until user guesses the number
# 3. stop the game if user guesses correct number


import random

guess_the_number = random.randint(0, 100)

# print(guess_the_number)
"""
while True:
    user_input = input("Guess the Number: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input > guess_the_number:
            print("Less")
            continue
        if user_input < guess_the_number:
            print("Greater")
            continue
        if user_input == guess_the_number:
            print("You Win!")
            break
    else:
        print(f"{user_input} is not an number")
"""

while True:
    user_input = input("Guess the Number: ")
    if not user_input.isdigit():
        print(f"{user_input} is not an number")
        continue

    user_input = int(user_input)
    if user_input > guess_the_number:
        print("Less")
        continue
    if user_input < guess_the_number:
        print("Greater")
        continue
    if user_input == guess_the_number:
        print("You Win!")
        break
