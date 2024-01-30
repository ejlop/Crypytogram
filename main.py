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
[ ] Encrypt each letter (do I need a dictionary?)
[ ] Create a key for each letter
[ ] Create external interface for the main game
[ ] Random number to leave X amount of letters known (depending on length of quote?)
'''

# Imports
from quoters import Quote
import time

# Generates a random quote and appends each character to a list
def generate_quote():
    quote = Quote.print().upper()
    print(quote)
    while "HAND-PICKED RELATED QUOTES" in quote:
        quote = Quote.print().upper()
    quote_list = []
    for i in range(len(quote)):
        if quote[i] == '"' and i > 0:
            return quote_list
        else:
            quote_list.append(quote[i])
    # for i in range(len(quote_list)):
    #     print(quote_list[i])
    return quote_list

# Encrypts every letter found in the quote
def encrypt_quote(quote):
    encrypted_quote = []
    for char in quote:
        encrypted_quote.append(char)
    # for i in range(len(encrypted_quote)):
    #     print(encrypted_quote[i])
    for i in range(len(encrypted_quote)):
        if encrypted_quote[i].isalpha():
            encrypted_quote[i] = "_"
    return encrypted_quote

# Updates the puzzle with correct guess
def guess(letter, quote, encrypted_quote):
    pass

# Generates known keys for each letter
def generate_library():
    pass

# Prints out the current state of the game
def generate_game(encrypted_quote):
    for char in encrypted_quote:
        print(char, end="")
    # print(encrypted_quote)

# Does what the name says 
def run_game():
    quote = generate_quote()
    encrypted_quote = encrypt_quote(quote)
    generate_game(encrypted_quote)
    
run_game()