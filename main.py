'''
Eduardo Lopez
01/29/24
APCSP Create Performance Task
Cryptogram!
'''

'''
** IDEAS SO FAR: **
--> Create a dictionary to encrypt each letter
--> Function to traverse the diverse the list of the alphabet, ykyk
--> Keep or remove having to solve for the author's name (if there is one)?
--> For text-based program: create a "board" that updates currently known letters

** TO-DO: **
[X] Encrypt each letter (do I need a dictionary?)
[X] Create a key for each letter
[ ] Create external interface for the main game?
[X] Random number to leave X amount of letters known (depending on length of quote?)
'''

# Imports
from quoters import Quote
import time
import random
import os

# Constants
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Generates the key for the game
def generate_key():
    key = []
    taken_letters = []
    random_num = random.randint(0,25)
    for i in range(len(alphabet)):
        while str(alphabet[random_num]) in taken_letters:
            random_num = random.randint(0,25)  
        key.append(alphabet[random_num])
        taken_letters.append(alphabet[random_num])
    print(alphabet)
    print(key)    
    return key

# Generates a random quote and appends each character to a list
def generate_quote():
    quote = Quote.print().upper()
    print(quote)
    while "HAND-PICKED RELATED QUOTES" in quote or len(quote) < 60:
        quote = Quote.print().upper()
    quote_list = []
    for i in range(len(quote)):
        if quote[i] == '"' and i > 0:
            return quote_list
        else:
            quote_list.append(quote[i])
    return quote_list

# Encrypts every letter found in the quote
def encrypt_quote(quote):
    encrypted_quote = []
    # Append each character from quote to new list
    for char in quote:
        encrypted_quote.append(char)
    # Replace each letter with an underscore
    for i in range(len(encrypted_quote)):
        if encrypted_quote[i].isalpha():
            encrypted_quote[i] = "_"
    # Replace a few underscores with the original letter for hints
    for i in range((int)(len(encrypted_quote)/10)):
        random_num = random.randint(0, len(encrypted_quote)-1)
        while not quote[random_num].isalpha():
            random_num = random.randint(0, len(encrypted_quote)-1)
        encrypted_quote[random_num] = quote[random_num]
    return encrypted_quote

# Requests a guess from the user and updates the game
def guess(letter, quote, encrypted_quote):
    pass

# Generates known keys for each letter
def generate_library():
    pass

# Refreshes and prints out the current state of the game
def generate_game(encrypted_quote, key, quote):
    for char in encrypted_quote:
        print(char, end="")
    print()
    for i in range(len(encrypted_quote)):
        if quote[i].isalpha():
            print(alphabet[key.index(quote[i])], end="")
        else:
            print(" ", end="")

# Does what the name says 
def run_game():
    os.system('cls')
    key = generate_key()
    quote = generate_quote()
    encrypted_quote = encrypt_quote(quote)
    generate_game(encrypted_quote, key, quote)
    
run_game()