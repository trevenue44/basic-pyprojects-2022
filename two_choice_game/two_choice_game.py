# Simple two-choice game
# Let's see how lucky you are. How good is your 50/50 chance?
# continuously choose between two letters: a and b
# would your choice be same as the computer's?

import random

options = ["a", "b"]
score = 0
score_multiplier = 1

print("Game started! Enter 'XX' to quit.")
while True:
    user_choice = input("A or B? ->>> ").lower()
    if user_choice.lower() == "xx":
        print("Thanks for playing.")
        break
    elif user_choice in options:
        if user_choice == random.choice(options):
            score += score_multiplier
            print(f"Yes, {user_choice.upper()} indeed!\tScore: {score}")
            score_multiplier += 1
        else:
            print("Oh no... It's the other.")
            print(f"Final Score: {score}")
            break
    else:
        print("Invalid Input. Try again.")
    print()
