"""
a scategories type thing but it's anime related, for use by the anime club
first patch made 05/06/23 by Rayha

Author/s: Rayha
Version: 1.6
Date updated: 07/06/23
Extra notes:
used chatgpt to make parts of this
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
    "a character from an Anime game"
]

hard_cats = [
    "Soundtracks",
    "Adaptations",
    "Conventions",
    "Voice Actors",
    "Directors",
    "Mecha"
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
        print("\n\n*****INSTRUCTIONS*****")
        print("* Press 'E' for Easy")
        print("* Press 'M' for Medium")
        print("* Press 'H' for Hard(only if you dare)")
        print("# and press 'X' to exit :(")
        game = input("So, what will it be? ")
        if game == 'e' or game == 'E':
            easy()
        elif game == 'm' or game == 'M':
            med()
        elif game == 'h' or game == 'H':
            hard()
        elif game == 'x' or game == "X":
            print("thank you for playing ")
            exit()
        else:
            print("enter something valid pls")

def many(num):
    """
    how many catgories or letter do u want?
    """
    # shuffle lists
    random.shuffle(categories)
    random.shuffle(alphabet)
    
    while True:
        try:
            print("\nenter a number for categories (and letter for hard mode)")
            num = int(input("So how many?:  "))
            if num > len(categories) or num > len(alphabet):
                print("how many categoires do you want???\n")
            elif num <= 0:
                print("haha I see what you did there.")
                print("please enter a positive number and not 0 either\n")
            elif num > 0 and num < len(categories) and num < len(alphabet):
                break
            
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

    # prints the stuff
    print("you have chossen easy mode")
    num = many(number_of)
    print("The letter for this round is...")
    print("**********  " + letter + "  **********")
    print("and you categories are...\n")
    for i in range(num):
        print("* " + categories[i] + "\n")
    print("you have 5 mins, go!")
    
    
    
def med():
    """
    meidum mode
    multiple letters and categories
    """
    # setting the variable to send to function
    number_of = 1

    # prints the stuff
    print("you have chossen hard mode")
    # setting num of letter and variable
    num = many(number_of)
    
    print("the formt of this round is: ")
    print("letter . category")
    for i in range(num):
        letter = alphabet[i]
        category = categories[i]
        print("\n" + letter + " . " + category)

def hard():
    """
    hard mode
    multiple letters and hard categories
    """
    # setting the variable to send to function
    number_of = 1

    # prints the stuff
    print("you have chossen hard mode")
    # setting num of letter and variable
    num = len(hard_cats)
    
    print("the formt of this round is: ")
    print("letter . category")
    for i in range(num):
        letter = alphabet[i]
        category = hard_cats[i]
        print("\n" + letter + " . " + category)
    
    

# mains routine
if __name__ == '__main__':

    demo()
    # forever loop
    while True:
        scattegories()
