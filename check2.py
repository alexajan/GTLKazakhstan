# Question 1
# Create a function that takes in an integer and returns "odd" if an even number and "even" if an odd number.


def check_even(num):
    if num % 2 == 0:
        return "odd"
    else:
        return "even"

# Question 2
# Copy your function from above and edit it to take in 0 as a default value.


def check_even(num=0):
    if num % 2 == 0:
        return "odd"
    else:
        return "even"

# Question 3
# Edit the function below to take that takes an arbitrary number of arguments.


def make_sandwiches(size, *condiments):
    """Print the list of condiments that have been requested."""
    print("Making a " + str(size) + "-inch sandwich with the following condiments:")
    for condiment in condiments:
        print("- "  + condiment)


# Question 4
# Any questions?