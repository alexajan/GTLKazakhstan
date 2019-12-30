# Madlibs Game

harry_potter = ["On his 11th birthday, young ", " Potter discovers the ", " he never knew he had, the ",
                " of a/an ", ". In his first ", " at Hogwarts School of Witchcraft and ", " he meets his two ",
                " friends Ron Weasley, an expert at Wizard ", ", and Hermione Granger, a girl with ",
                " parents. Harry learns the game of Quiditch and Wizard ", " on his way to facing a Dark ",
                " teacher who is bent on ", " him."]

harry_potter_prompts = ["Boy's name", "noun", "occupation", "measurement", "noun", "adjective", "game", "adjective"
                        "noun (plural)", "verb ending in 'ing'"]

valentines = ["Be my ", "\n", " make the world go ", "\nPickachu says 'I ", " you.'\nRoses are ",
              ", and violets are blue. Sugar is ", " and so are you!\nYou make my ", " flutter."]

valentines_prompts = ["noun", "noun (plural)", "adjective", "verb", "color", "adjective", "body part"]


class MadLibs:
    def __init__(self, phrases, prompts):
        self.phrases = phrases
        self.prompts = prompts
        self.words = []

    def prompt_user(self):
        for prompt in self.prompts:
            self.words.append(input("Please give me a(n) " + prompt + ". "))

    def print_story(self):
        story = ""
        for i in range(len(self.words)):
            phrase = self.phrases[i]
            word = self.words[i]
            concat = phrase + word
            story += concat
        story += self.phrases[-1]
        return story

    def play(self):
        print("Let's get some words down.")
        self.prompt_user()

        print("Here's your story!")
        return self.print_story()


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
