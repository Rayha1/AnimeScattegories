"""
a scategories type thing but it's anime related, for use by the anime club
first patch made 05/06/23 by Rayha

Author/s: Rayha
Other Contributors: Amelia, Silvia
Version: 1.4
Date updated: 05/06/23
Extra notes:
- used chatgpt to make parts of this
- I know printing from functions is bad but how else am I supposed to print an
  entire list
"""

# CONSTANTS

# variables

# for the shuffles
import random

# categories
categories = [
    "Genres",
    "Characters",
    "Studios",
    "Movies",
    "Series",
    "Openings/Endings",
    "Streaming Platforms (aka illegal websites lol)",
    "Merchandise",
    "Symbolism",
    "Fantasy Worlds",
    "Slice of Life",
    "Strong Female Characters",
    "Antiheroes",
    "Villains",
    "Anime",
    "Manga",
    "Manga artists/ authors",
    "Animals",
    "Male Protagonist",
    "Female Protagonist",
    "Protagonist",
    "Powers/ Skills",
    "Schools",
    "Characters",
    "Antagonist",
    "Anime Style RPGS",
    "Anime style video games",
    "A song from an Anime Rythm game",
    "Anime Content Creator (like a youtuber or something)"
]

# hard categories no one probably solve, hence the warning
hard_cats = [
    "Soundtracks",
    "Adaptations",
    "Conventions",
    "Voice Actors",
    "Directors",
    "Mecha",
    "A Fanartist (not you or your friends)"
    ]

# letters
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def demo():
    """
    a demo to show how it works
    """

    # Intro message
    print("***** Welocome to Anime & Manga Scattegories! *****")
    print("the rules are simple:")
    print("* Pick a mode, E for easy and H for hard (Or press X to exit)")
    print("* Easy gives you one letter for all the catgories")
    print("* Hard gives you a letter per category")
    print("* In both modes you can choose the ammount of categories")
    print("\n\n***** Now for the actual game *****")
    print("- work in groups or alone")
    print("- any double ups will result in 0 points")
    print("  for the groups involved for that category")
    print("- if a group presents an answer with 2 words both starting")
    print("  with the rounds letter, give double points")
    print("- the team with the most points as the end of the round wins")
    print("- idk how to deal with ties you decide what to do :)")
    
    

def scattegories():
    """
    basically the main routine, asks for the mode
    and then directs you to correct function 
    """

    # loop to pick and/or exit
    while True:
        # instructions
        print("\n\n*****INSTRUCTIONS*****")
        print("* Press 'E' for Easy")
        print("* Press 'M' for Medium")
        print("* Press 'H' for Hard(only if you dare)")
        print("# and press 'X' to exit :(")
        game = input("So, what will it be? ")

        # easy
        if game == 'e' or game == 'E':
            easy()
        # medium
        elif game == 'm' or game == 'M':
            med()
        # hard
        elif game == 'h' or game == 'H':
            hard()
        # exit
        elif game == 'x' or game == "X":
            print("thank you for playing ")
            exit()
        # error
        else:
            print("enter something valid pls")
        print("you have 5 mins, go!")

def many(num):
    """
    how many catgories or letter do u want?
    """
    
    # shuffle lists
    random.shuffle(categories)
    random.shuffle(alphabet)

    # error checker loop to get valid number
    while True:
        try:
            # ask num
            print("\nenter a number for categories (and letter for hard mode)")
            num = int(input("So how many?:  "))

            # checks if there enough nums or categories
            if num > len(categories) or num > len(alphabet):
                print("how many categoires do you want???\n")
            # negative nums
            elif num <= 0:
                print("haha I see what you did there.")
                print("please enter a positive number and not 0 either\n")
            # valid num
            elif num > 0 and num < len(categories) and num < len(alphabet):
                break
          # when they dont enter number  
        except ValueError:
            print("I thought you are better than this")
            print("Please enter a number\n\n")

    return num
            

    
def easy():
    """
    easy mode
    one letter, multiple catgories
    """
    
    # setting the variable to send to function
    number_of = 1
    # getting letter
    letter = alphabet[number_of]
    # tell u the mode
    print("you have chossen easy mode")
    # get number of categories
    num = many(number_of)

    # prints catgeories and letter
    print("The letter for this round is...")
    print("**********  " + letter + "  **********")
    print("and you categories are...\n")
    for i in range(num):
        print("* " + categories[i] + "\n")
    
    
    
def med():
    """
    meidum mode
    multiple letters and categories
    """
    # setting the variable to send to function
    number_of = 1

    # prints the mode
    print("you have chossen hard mode")
    # setting num of letter and variable
    num = many(number_of)
    # prints catgeories and letters
    print("the formt of this round is: ")
    print("letter . category")
    for i in range(num):
        letter = alphabet[i]
        category = categories[i]
        print(letter + " . " + category + "\n")
        

def hard():
    """
    hard mode
    multiple letters and hard categories
    """
    # setting the variable to send to function
    number_of = 1

    # prints the mode
    print("you have chossen hard mode")
    # setting num of letter and variable
    num = len(hard_cats)
    # prints catgeories and letters 
    print("the formt of this round is: ")
    print("letter . category")
    for i in range(num):
        letter = alphabet[i]
        category = hard_cats[i]
        print("\n" + letter + " . " + category + "\n")
    
    

# mains routine
if __name__ == '__main__':

    demo()
    # forever loop
    while True:
        scattegories()
        
