'''
Eduardo Lopez
01/29/24
APCSP Create Performance Task
'''
# Imports
from random_word import RandomWords
from quote import quote
 
# Generates a random word 
r = RandomWords()
def generate_word():
    random_word = r.get_random_word()
    print("Keyword Generated: ", random_word)
    return random_word

# Generates a random quote based on the random word generated
# in generate_word()
def generate_quote(random_word):
    random_quote = quote(random_word, limit=1)
    # This for loop is necessary when only printing the quote as the quote function returns 
    # a list of dictionaries with information about a quote
    for i in range(len(random_quote)):
        print("\nQuote Generated: ", random_quote[i]["quote"]) #Will print only the value next to the quote key.
        quote = random_quote[i]["quote"]
    return quote

# Main
random_word = generate_word()
random_quote = generate_quote(random_word)