"""
a scategories type thing but it's anime related, for use by the anime club

Author: Rayha
Version: 1.1
Date updated: 05/06/23
Extra notes:
used chatgpt to make the lists
"""

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

def setting():
    print("ehhe")

    
def easy():
    print("you have chossen easy mode")
    # shuffle list
    random.shuffle(categories)
    for i in range(10):
        print(categories[i])
    
    

def hard():
    print("you have chossen hard mode")
    

# mains routine
if __name__ == '__main__':
    game = input("(E)asy or (H)ard mode: ")
    if game == 'e' or game == 'E':
        easy()
    elif game == 'h' or game == 'H':
        hard()
    else:
        print("enter something valid pls")
