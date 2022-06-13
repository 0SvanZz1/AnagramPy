import random
import sys, os
import requests
import json

import gamer as ga

def create_anagram(words, separator=None):
    """Create an anagram based on a array of words

    Parameters
    ----------
    words : list of str
        List of words

    separator : int, optional (default is 10)
        Number of letters to be displayed at each line
    """

    if separator is None:
        separator = 10

    anagram = []
    for word in words:
        for letter in word.upper():
            #if letter not in anagram:
            anagram.append(letter)

    # Shuffles the anagram to be in a random order
    random.shuffle(anagram)

    lineLimit = 0
    for letter in anagram:
        if lineLimit < separator:
            print(letter, end=' ')
            lineLimit += 1
        else:
            print()
            print(letter, end = ' ')
            lineLimit = 1
    print()

def search_word(words, gamer):
    """Search for a word in the word database
    
    Parameters
    ----------
    words : list of str
        List of words
    
    gamer : instance of Gamer
        Instance of Gamer class
    """

    print("""
    This an anagram game. Your objective is to search for words based on the displayed letters.

    RULES:
        - You can only miss 5 times, otherwise the game will end
        - The anagram is shuffled everytime you miss or find a word
        - The word database won't consider words with special characters, so avoid using it
    """)

    if len(words) > 0:
        if gamer.chances > 0:
            print("Anagram:")
            create_anagram(words)

            print("\nDiscovered words:")
            if len(gamer.discovered_words) == 0:
                print(0)
            else:
                [print(word) for word in gamer.discovered_words]

            print("\nChances:")
            print(gamer.chances)

            print('\nObs: To exit press \'Enter\'.')

            typed_word = input("\nType a possible word: ")
            print()

            if typed_word == "":
                x = input("Do you want to see the word database? (Y/n) ")
                if x.lower() == "y" or x == "":
                    display_word_db(words)
                    sys.exit(0)
                else:
                    sys.exit(0)

            if typed_word.isalpha():
                if typed_word.lower() in words:
                    print("You've discovered a word! Well done.")
                    words.remove(typed_word.lower())
                    gamer.discovered_words.append(typed_word.lower())

                    if len(words) > 0:
                        x = input("Do you want to continue? (Y/n) ")
                        if x.lower() != "y" and x != "":
                            sys.exit(0)

                    clear_terminal()
                else:
                    print("This word is not present in the anagram. I'm sorry :/")
                    gamer.decrease_chances()
                    
                    x = input("Do you want to continue? (Y/n) ")
                    if x.lower() != "y" and x != "":
                        sys.exit(0)
                    
                    clear_terminal()
                        
            else:
                print("The typed word is not a String.")
                gamer.decrease_chances()
                
                x = input("Do you want to continue? (Y/n) ")
                if x.lower() != "y" and x != "":
                    sys.exit(0)
                
                clear_terminal()
        else:
            print("Your chances are over haha goodbye :P")
            sys.exit(0)
    else:
        print("You've discovered all words. Well done!")
        print("Discovered words:")
        [print(word) for word in gamer.discovered_words]
        sys.exit(0)

def display_word_db(words):
    """Display a word database content
    
    Parameters
    ----------
    words : list of str
        List of words
    """

    for word in words:
        print(word.upper(), end=' ')

def clear_terminal():
    """Clear the terminal"""
    
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word_database(topic, max):
    """Get a word database based on a specified topic

    Parameters
    ----------
    topic: str
        Topic to serve as a base for the word database creation
    max: int
        Maximum number of words to be returned

    Returns
    -------
    list of str
        List of words to act as a word database
    """
    
    word_db = []
    
    url = "https://api.datamuse.com/words?topics={}&max={}".format(topic, max)
    response = requests.get(url)

    if response.status_code == 200:
        response_content = json.loads(response.text)
        for word_resp in response_content:
            if word_resp['word'].isalpha():
                word_db.append(word_resp['word'])
    else:
        print("There was an error while fetching words for the database")
        sys.exit(1)

    return word_db

def main():
    if len(sys.argv[1:]) != 2:
        print("""
        You're not executing it in the right way. Take this as an example:
        $ python3 anagram.py War 15

        Where 'War' is the topic and '15' the maximum number of words for the word database.

        Try one more time!
        """)
        sys.exit(1)
    
    topic, max = sys.argv[1:]
    words = get_word_database(topic, max)
    gamer = ga.Gamer()

    while True:
        search_word(words, gamer)

if __name__ == '__main__':
    main()