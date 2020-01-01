# Check 3

# Q1: Create a class that describes a pizza (probably with toppings and size but up to you). Include at least two functions: one that adds toppings and one that prints the current toppings.

class Pizza:
    """Class describing a pizza."""
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def get_toppings(self):
        """Get what toppings are currently on the pizza."""
        print("Your toppings: ")
        for topping in self.toppings:
            print("-" + topping)

    def add_topping(self, *new_toppings):
        """Add new toppings to pizza."""
        self.toppings.extend(new_toppings)

# Q2: Create a deep dish pizza that inherits from your class above. Include an additional function that specifies the thickness of the crust.

class DeepDish(Pizza):
    """A tasty type of pizza from Chicago with a thick crust."""
    def __init__(self, size, toppings, crust):
        super().__init__(size, toppings)
        self.crust = crust # in inches

    def change_crust(self, new_size):
        """Changes crust depth."""
        self.crust = new_size

# Q3: How do Python classes fit in to the object oriented programming paradigm? Are classes and objects the same thing?

# Classes are a type of data structure that is user-defined. An instance of a class (i.e. instantiating it
# in a variable) is an object, not the definition of the class itself.