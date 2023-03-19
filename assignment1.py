# Name: Gowthaman Kangatharan
# Student ID: 101247677
# Assignment 1: Hangman template
# assignment1.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(' ')
    print("  ", len(wordlist), "words loaded.")
    return wordlist


# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
#secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0, len(words_dict))]
    return word


# end of helper code
# -----------------------------------

# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
secret_word = "claptrap"
letters_guessed = []

# word_guessed function:
def word_guessed():
    """
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    """
    global secret_word
    global letters_guessed
    ####### YOUR CODE HERE ######
    num = 0
    if secret_word in letters_guessed:
        num += 1
    if num == len(secret_word):
        return True
    else:
        return False

# print_guessed function
def print_guessed():
    """
    Prints out the characters you have guessed in the secret word so far
    """
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    guessWord = []
    if secret_word in letters_guessed:
        guessWord += secret_word
    else:
        guessWord += "_"
    return guessWord


# play_hangman function
def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to final steps.
    secret_word = get_word()
    print('Starting game...')
    ####### YOUR CODE HERE ######
    print("Welcome to the Hangman Game!")
    while (mistakes_made < MAX_GUESSES):
        print_hangman_image(mistakes_made)
        print(MAX_GUESSES - mistakes_made),
        print_guessed()

        letter = input("Please guess the letter: ")
        if (len(letter) == 1):
            if (letter in letters_guessed):
                print("You already guessed that letter.Please Try again!")
            else:
                letters_guessed.append(letter)
                if (letter in secret_word):
                    print("You have guess the correct letter!")
                    if word_guessed():
                        print("You got it correct!")
                        mistakes_made = MAX_GUESSES
                else:
                    print("Your guess was incorrect!")
                    mistakes_made += 1
    print("Secret Word:", secret_word)
    print("Game Over!!")

    userinput = input("Run Again?(y/n or yes/no): ")
    if userinput == "yes" or userinput == "y":
        play_hangman()
    if userinput == "no" or userinput == "n":
        print("Thank you for play!")
    return None
# Start the game
play_hangman()

