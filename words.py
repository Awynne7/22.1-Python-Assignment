"""
Do this work in a new file, ***words.py***.
def print_upper_words(words):

1. For a list of words, print out each word on a separate line,
but in all uppercase. How can you change a word to uppercase?
Ask Python for help on what you can do with strings!

2.Turn that into a function, print_upper_words. Test it out.
(Don’t forget to add a docstring to your function!)

3. Change that function so that it only prints words that start
with the letter ‘e’ (either upper or lowercase).

4. Make your function more general: you should be able to pass in
a set of letters, and it only prints words that start with one of
those letters.
"""

""" print earch word on a seperate line, all uppercase
"""
def print_upper_words(words):
    for word in words:
        print(word.upper())
        
""" print each word on a seperatr line, all uppercase,
if word starts with e or E
"""
def print_upper_words2(words):
    for word in words:
        if word.startswith("e") or word.startswith ("E"):
            print(word.upper())
            
"""print each word on seperate line, all uppercase, if start with one of given
"""
def print_upper_words3(words, must_start_with):
    for word in words:
        if lerrer in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
