# Word Guessing Game with Creativity Enhancements
# Enhancements: Random secret word selection

import random

def generate_hint (secret, guess):              # function hint
    hint = ""                                   # variable hint initializing
    for i in range(len(secret)):                # index range length secret
        if guess[i] == secret[i]:               # cheking
            hint += guess[i].upper() + " "      # putting upper and space when equals
        elif guess[i] in secret:
            hint += guess[i].lower() + " "      # putting lower when has the word but not equal
        else:
            hint += "_ "                        # when is different put just _ and space

    return hint

# Enhancement - list of possible secret words
word_list = ["mosiah", "nephi", "temple", "heleman", "moroni"]

# Enhancement - select a random word from the list
secret = random.choice(word_list)

guesses = 0                                     # initialize the counter
correct_guess = False                           # first condition


print("Welcome to the word guessing game!")

# Hint:
print("Your hint is: " + "_ " * len(secret))    # print: Your hint is: _ _ _ _ _ _ 


while not correct_guess:                        # question when guess is wrong:
    guess = input("What is your guess? ").lower()
    guesses += 1                                # counting guesses in each try 

    if len(guess) != len(secret):               # length different
        print("Sorry, the guess must have the same number of letters as the secret word.")
    elif guess == secret:
        correct_guess = True                    # question when guess is correctly
        print(f"Congratulations! You guessed it!\nIt took you {guesses} guesses.")
    else:
        hint = generate_hint(secret, guess)     # generating hint
        print(f"Your hint is: {hint}")





