# Guess the Number Game
# Your mission is to build a game that:
# > asks a user for their name
# > explains that they will guess a number between 1 and 20
# > generate a number between 1 and 20 (hint: use random.randint(min number, max number) )
# > ask the user for their guess until they guess it or they have guessed 6 times, whichever comes first
# Goal: Review for/while loops, if/else statements, user input, and terminal use. Introduce try/except.

# Try it first, and if you need help, skeleton code is on the bottom.

# import so you can use random.randint(min number, max number)
import random

# Ask for name

# Say hi!

# Set a number

# Use a for loop to have the user guess the number
    # Ask for a guess

    # Check if the player won

    # Check if the player lost

    # Give the player a hint

# Use a while loop to have the user guess the number

# extra credit: What happens when a user guesses nothing or something that's not a number?
# hint: look up try...except clauses.


### SKELETON CODE ###

# Ask for name
name = input(#TODO ask for name)

# Say hi!
hello = "Hi " + name #TODO concatenate name here
print(hello + ". Let's play a game of Guess the Number. I will think of a number between 1 and 20, and you will have 6 guesses to guess it.")

# Set a number
number = random.randint(#TODO)

# Use a for loop to have the user guess the number

for i in range(#TODO):
    guess = #TODO ask for a number and convert to integer

    # TODO Check if the player won
    if ...:
        print("Congrats! You guessed that my number is " + str(number) + ".")
        break

    # TODO Check if the player lost hint: how many guesses have they tried?

    # TODO Give the player a hint
    elif ...:
        ...

    else:
        ...