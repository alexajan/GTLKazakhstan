# Madlibs Game
# Your mission is to create a Madlibs game where the player fills in the blanks for a story they don't know. At the end, the game prints the story back to them. Your game must:
# > create a Madlibs class that has at least two function definitions
# > pass in two arguments to the class: the phrases of the story and the user prompts for the story.
# > feel free to create your own Madlibs story!

# default story options
# hp for Harry Potter
harry_potter = ["On his 11th birthday, young ", " Potter discovers the ", " he never knew he had, the ",
                " of a/an ", ". In his first ", " at Hogwarts School of Witchcraft and ", " he meets his two ",
                " friends Ron Weasley, an expert at Wizard ", ", and Hermione Granger, a girl with ",
                " parents. Harry learns the game of Quiditch and Wizard ", " on his way to facing a Dark ",
                " teacher who is bent on ", " him."]

harry_potter_prompts = ["Boy's name", "noun", "occupation", "measurement", "noun", "adjective", "game", "adjective"
                        "noun (plural)", "verb ending in 'ing'"]

# v for valentine's
valentines = ["Be my ", "\n", " make the world go ", "\nPickachu says 'I ", " you.'\nRoses are ",
              ", and violets are blue. Sugar is ", " and so are you!\nYou make my ", " flutter."]

valentines_prompts = ["noun", "noun (plural)", "adjective", "verb", "color", "adjective", "body part"]

# Define the Madlibs class

# Define an init function

# Define helper functions (i.e. prompt_user or print_story)

# Define a main play function

# Extra (hard) credit: How would you make the stories into classes that inherit from Madlibs?

### SKELETON CODE ###

# class definition
class MadLibs:
    def __init__(self, ..., ...): #TODO fill all the ... in.
        self.phrases = ...
        self.prompts = ...
        self.words = []

    def prompt_user(self):
        for prompt in #TODO reference this class's prompts:
            response = input(...) #TODO ask the user for a response to the prompt
            #TODO add the response to the end of this class's words list

    def print_story(self):
        story = ""
        for i in range(len(self.words)):
            phrase = #TODO reference this class's phrases and index into it
            word = #TODO reference this class's words and index into it
            # TODO add these to story variable
        story += self.phrases[-1] # self-test: what is this line of code doing? why is it needed?
        return story

    def play(self):
        print("Let's get some words down.")
        # TODO call prompt_user function

        print("Here's your story!")
        final_story = # TODO call print_story
        return final_story

### END SKELETON CODE ###

def main():
    q = False
    while not q:
        response = input("Welcome to Madlibs. Type 'p' to play or 'q' to quit. ")
        if response == 'q':
            print("Thanks for playing!")
            q = True
        elif response == 'p':
            story = input("Type 'hp' to play the Harry Potter story, and 'v' to play the valentine's card. ")
            if story == 'hp':
                game = MadLibs(harry_potter, harry_potter_prompts)
            elif story == 'v':
                game = MadLibs(valentines, valentines_prompts)
            print(game.play())


if __name__ == "__main__":
    main()
