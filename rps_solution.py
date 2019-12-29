# Rock, Paper, Scissors Solution

import random


def user_quit(response):
    """Checks if user would like to quit."""
    if response.lower() == "q":
        return True
    return False


def ask_user():
    """Asks user for a response. Returns string response that is one of the valid responses."""
    response = ""
    options = ['r', 'p', 's', 'q']

    while response not in options:
        response = input("Rock, Paper, or Scissors? Type r for rock, p for paper, or s for scissors. ").lower()

    return response


def ask_computer():
    """Chooses a random response for the computer and returns string response."""
    options = ['r', 'p', 's']
    i = random.randint(0, 2)
    if i == 0:
        print("Computer: Rock")
    elif i == 1:
        print("Computer: Paper")
    else:
        print("Computer: Scissors")
    return options[i]


def eval_winner(user, comp):
    """Evaluates winner of round and returns +1 for a user win, -1 for a user loss, +0 for a tie."""
    # All tie cases
    if user == comp:
        print("It's a tie.")
        return 0

    # User wins
    elif (user == 'p' and comp == 'r') or (user == 'r' and comp == 's'):
        print("You win!")
        return 1

    # Computer wins
    else:
        print("You lost!")
        return -1


def rps():
    """Runs helper functions to play a round of rock, paper, scissors."""
    score = 0

    # Ask user for response
    response = ask_user()
    if user_quit(response):
        return score, True

    # Get computer response
    comp_response = ask_computer()

    # Evaluate winner
    score += eval_winner(response, comp_response)

    return score, False


def main():
    q = False
    score = 0
    while not q:
        s, q = rps()
        score += s
        print("Your current score is " + str(score) + ".")
    print("Thanks for playing.")


if __name__ == "__main__":
    main()