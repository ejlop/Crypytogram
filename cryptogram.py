'''
Eduardo Lopez
01/29/24
APCSP Create Performance Task
Cryptogram!
'''

# Imports
from quoters import Quote
import time
import random
import os
import keyboard

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
    return key

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
    return quote_list

# Encrypts every letter found in the quote
def encrypt(quote):
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

# Prints out the controls of the game
def print_controls():
    print("----------")
    print("CONTROLS:")
    print(" ← : Move Left\n",
          "→ : Move Right\n",
          "↑ : Hint\n",
          "↓ : Select\n",
          "Q : Quit")
    print("----------")

# Selects a letter based on arrow inputs
index = 0
hint_num = 5
def select_letter(input):
    global index
    global encrypted_quote
    global quote
    global hint_num
    pos = [" "]*len(encrypted_quote)
    pos_indicator = "^"
    # Moves left
    if input.name == "left":
        if index == 0:
            index = len(encrypted_quote)-1
            pos[index] = pos_indicator
        else:
            index-=1
            pos[index] = pos_indicator
    # Moves right
    elif input.name == "right":
        if index == len(encrypted_quote)-1:
            index = 0
            pos[index] = pos_indicator
        else:
            index+=1
            pos[index] = pos_indicator
    # Input letter
    elif input.name == "down":
        if encrypted_quote[index] == quote[index]: # User can't change correct guesses
            pass
        elif encrypted_quote[index] == "_" or encrypted_quote[index].isalpha():
            guess(index)
        else:
            pass
    # Request hint
    elif input.name == "up":
        if hint_num > 0:
            hint()
        else:
            pass
    refresh(pos, encrypted_quote, quote)

# Replaces the letter with the user's guess  
def guess(index):
    global encrypted_quote
    letter = input("\nInput letter: ")
    while len(letter) > 1 or not(letter.isalpha()):
        letter = input("Invaid input, try again: ")
    encrypted_quote[index] = letter.upper()

# Inputs a correct letter (up to 5 times)
def hint():
    global encrypted_quote
    global quote
    global hint_num
    index = random.randint(0, len(encrypted_quote)-1)
    while (not encrypted_quote[index].isalpha() or not encrypted_quote[index] == "_") and (encrypted_quote[index] == quote[index]):
        index = random.randint(0, len(encrypted_quote)-1)
    encrypted_quote[index] = quote[index]
    hint_num-=1

# Refreshes the game
def refresh(pos, encrypted_quote, quote):
    os.system('cls')
    # Prints out encrypted quote 
    for char in encrypted_quote:
        print(char, end="")
    print()
    # Prints out the position indicator
    for char in pos:
        print(char, end="")
    print()
    # Prints out the key underneath encrypted quote
    for i in range(len(encrypted_quote)):
        if quote[i].isalpha():
            print(alphabet[key.index(quote[i])], end="")
        else:
            print(" ", end="")
    print()
    # Ends the game if puzzle has been solved
    if encrypted_quote == quote:
        end_game()
    # Prints out the number of hints left
    print("You have", hint_num, "hints left.")
    # Prints out controls
    print_controls()

# Prints out the initial state of the game
def generate_game(encrypted_quote, key, quote):
    os.system('cls')
    # Prints out encrypted quote 
    for char in encrypted_quote:
        print(char, end="")
    print()
    # Prints out initial position indicator
    print("^")
    # Prints out the key underneath encrypted quote
    for i in range(len(encrypted_quote)):
        if quote[i].isalpha():
            print(alphabet[key.index(quote[i])], end="")
        else:
            print(" ", end="")
    print()
    # Prints out initial number of hints
    print("You have 5 hints left.")
    # Prints out controls
    print_controls()

# Ends the game
def end_game():
    congrats = list("\n\nCongratulations! You solved the puzzle!")
    for i in range(len(congrats)):
        print(congrats[i], end="")
        time.sleep(.05)
    quit()

# Runs the game
os.system('cls')
key = generate_key()
quote = generate_quote()
encrypted_quote = encrypt(quote)

generate_game(encrypted_quote, key, quote)
keyboard.on_press(select_letter)
keyboard.wait('q') # Hitting Q stops the program