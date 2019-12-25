# Guess the Number Game Solution

import random

# Ask for name
name = input("Hello! What is your name? ")

# Say hi!
print("Hi " + name + ". Let's play a game of Guess the Number. I will think of a number between 1 and 20, and you will have 6 guesses to guess it.")

# Set a number
number = random.randint(1, 20)

# Use a for loop to have the user guess the number

for i in range(6):
    guess = int(input("Guess " + str(i+1) + ". What is your guess? "))

    # Check if the player won
    if guess == number:
        print("Congrats! You guessed that my number is " + str(number) + ".")
        break

    # Check if the player lost
    elif i == 5:
        print("You've used all of your guesses. My number was " + str(number) + ". Better luck next time.")

    # Give the player a hint
    elif guess > number:
        print("Your guess is too high. Try again.")

    else:
        print("Your guess is too low. Try again.")

# # Use a while loop to have the user guess the number
#
# i = 0
# while i < 6:
#     guess = int(input("Guess " + str(i + 1) + ". What is your guess? "))
#
#     # Check if the player won
#     if guess == number:
#         print("Congrats! You guessed that my number is " + str(number) + ".")
#         break
#
#     # Give the player a hint
#     elif guess > number:
#         print("Your guess is too high. Try again.")
#
#     else:
#         print("Your guess is too low. Try again.")
#
#     i += 1
#
# if i == 6:
#     print("You've used all of your guesses. My number was " + str(number) + ". Better luck next time.")

# extra credit: What happens when a user guesses nothing or something that's not a number?
# hint: look up try...except clauses.

# for i in range(6):
#     try:
#         guess = int(input("Guess " + str(i+1) + ". What is your guess? "))
#     except ValueError:
#         print("You did not enter a number. Goodbye.")
#         break
#
#     if guess == number:
#         print("Congrats! You guessed that my number is " + str(number) + ".")
#         break
#
#     elif i == 5:
#         print("You've used all of your guesses. My number was " + str(number) + ". Better luck next time.")
#
#     elif guess > number:
#         print("Your guess is too high. Try again.")
#
#     else:
#         print("Your guess is too low. Try again.")