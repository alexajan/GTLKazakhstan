# Rock, Paper, Scissors
# Your mission is to create the rock, paper, scissors game, where the user plays in terminal against a computer. It must:
# > keep track of the total score (+1 for wins, -1 for losses, +0 for ties) or a tally of wins, losses, and ties.
# > function to get the user response
# > function to get the computer response
# > function to evaluate the win/loss/tie
# > function to call the other helper functions

import random

# Create a function to get user response

# Create a function to get computer response

# Create a function to evaluate who won the round

# Put it all together in a function that runs the three other functions

# Extra credit: Create a function to allow the user to quit by typing 'q' at any time. Where would you need to call that function?


### SKELETON CODE ###


def ask_user():
    """TODO fill in function description"""
    response = ""
    options = [] #TODO What are the possible responses?

    # TODO Create a while loop that ensures response is one of the valid options
    while ... not in ...:
        response = input(...)

    return response


def ask_computer():
    """TODO fill in function description"""
    options = [...] #TODO What are the possible responses?
    i = #TODO hint: use random to choose a random index
    if i == 0:
        print("Computer: ...") #TODO: fill in with what the computer chose
    elif i == 1:
        print("Computer: ...") #TODO: fill in with what the computer chose
    else:
        print("Computer: ...") #TODO: fill in with what the computer chose
    return options[i]


def eval_winner(user, comp):
    """TODO fill in function description"""
    # TODO: all tie cases

    # TODO: all cases where the user wins

    # TODO: all cases where the computer wins


def rps():
    """TODO fill in function description"""
    # TODO call ask_user

    # TODO call ask_computer

    # Evaluate winner
    score = #TODO call eval_winner using the responses from above

    return score


def main():
    score = 0
    while True:
        score += #TODO call rps function
        print("Your current score is " + str(score) + ".")
    print("Thanks for playing.")


if __name__ == "__main__":
    main()