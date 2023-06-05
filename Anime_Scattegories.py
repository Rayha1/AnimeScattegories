"""
a scategories type thing but it's anime related, for use by the anime club
first patch made 05/06/23 by Rayha

Author/s: Rayha
Version: 1.2
Date updated: 05/06/23
Extra notes:
used chatgpt to make the lists
"""

# CONSTANTS

# variables

# for the shuffles
import random

# categories
categories = [
    "Anime Genres",
    "Anime Characters",
    "Anime Studios",
    "Anime Movies",
    "Anime Series",
    "Anime Soundtracks",
    "Anime Adaptations",
    "Anime Openings/Endings",
    "Anime Cosplay",
    "Anime Conventions",
    "Anime Streaming Platforms",
    "Anime Crossovers",
    "Anime Fandom",
    "Anime Merchandise",
    "Anime Voice Actors",
    "Anime Art Styles",
    "Anime Directors",
    "Anime Symbolism",
    "Anime Mecha",
    "Anime Romance",
    "Anime Fantasy Worlds",
    "Anime Slice of Life",
    "Anime Strong Female Characters",
    "Anime Antiheroes",
    "Anime Villains",
    "Anime Comedy",
    "Anime Fan Art"
]

# letters
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

def many(num):
    """
    how many catgories or letter do u want?
    """
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
    

def scattegories():
    """
    basically the main routine, asks for the mode
    and then directs you to correct function
    """
    # shuffle lists
    random.shuffle(categories)
    random.shuffle(alphabet)

    # loop to pick and/or exit
    while True:
        print("\n\n\npress x to exit")
        game = input("(E)asy or (H)ard mode: ")
        if game == 'e' or game == 'E':
            easy()
        elif game == 'h' or game == 'H':
            hard()
        elif game == 'x' or game == "X":
            print("thank you for playing ")
            exit()
        else:
            print("enter something valid pls")
            

    
def easy():
    # setting the variable to send to function
    number_of = 1
    # getting letter
    letter = alphabet[number_of]
    
    print("you have chossen easy mode")
    num = many(number_of)
    print("The letter for this round is...")
    print("**********  " + letter + "  **********")
    print("and you categories are...\n")
    for i in range(num):
        print(categories[i] + "\n")
    print("you have 5 mins, go!")
    
    
    

def hard():
    # setting the variable to send to function
    number_of = 1
    
    print("you have chossen hard mode")
    

# mains routine
if __name__ == '__main__':

    # forever loop
    while True:
        scattegories()
    
