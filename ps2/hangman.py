# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from distutils.log import set_verbosity
from math import fabs
import random
import string

from numpy import str_

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
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words() #a list of words


def is_word_guessed(secret_word, letters_guessed): #checked
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed: return False
    return True 
  



def get_guessed_word(secret_word, letters_guessed): #checked
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    n = len(secret_word)
    ans = '_'*n
    for letter in letters_guessed:
      for i in range(n):
        if secret_word[i] == letter:
            ans = ans[0:i]+letter+ans[i+1:n]
    
    return ans
        
    pass

import string

def get_available_letters(letters_guessed): #checked
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str_available = string.ascii_lowercase
    ans =''
    for letter in str_available:
        if letter not in letters_guessed:
            ans += letter
    return ans

    
    

def hangman(secret_word): #checked

    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman !")
    
    print(f"I'm thinking of a word that is {len(secret_word)} letters long")
    sep_str = "----------------------"
    print(sep_str)
    #initialize the number of guesses : 6
    num_of_guesses = 6
    #initialize the list of guessed letters so far
    letters_guessed = []
    #initialize the number of warnings, when you have 0 warnings and you insert 
    #an invalid input such as string,number,etc... you will lose 1 point
    num_of_warnings = 3

    #be sure that taking the advantages of 3 helper funcs : is_word_guessed,get_guessed_word
    #get_available_letters
    
    #The game keep continuing whenever num_of_guesses > 0:
    while num_of_guesses > 0:
      print(f"You have {num_of_guesses} guesses left")
      print(f"Available letters : {get_available_letters(letters_guessed)}")
      #taking the guessed lette
      letter = input("Please guess a letter : ")
      #REMEMBER ADDING THE GAME RULES.
      #The case input is invalid
      if len(letter) > 1 or letter.isalpha() == False: 
        if num_of_warnings > 0:
          num_of_warnings -= 1
          print(f"Oops, that is not a valid letter. You have {num_of_warnings} warnings left")
        else: #The case when we have 0 warnings left
          print("Oops, that is not a valid letter. You have no warnings left, so you lose one guess")
          num_of_guesses -= 1
        #print sep_str to end a guess
        print(sep_str)
      
      #The case when input is a guessed letter 
      elif letter in letters_guessed:
        if num_of_warnings > 0 : 
          num_of_warnings -= 1
          print(f"Oops, you've already guessed this letter. You have {num_of_warnings} warnings left")
        else: #The case when we have 0 warnings left
          print("Oops,you've guessed this letter. You have no warnings left, so you lose one guess")
          num_of_guesses -= 1
        #print sep_str to end a guess 
        print(sep_str)
      
        
      else: #the case that input is valid
        #update the letter_guessed list (for the case the input is valid)
        letters_guessed.append(letter)
        #start checking whether the guessed letter is in secret_word or not
        if letter in secret_word:
          print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}")
        else:
          print(f"Oops, that letter is not in my word: {get_guessed_word(secret_word,letters_guessed)} ")

        #Adding separate string after each guess
        print(sep_str)
        #checking whether the secret word is guessed or not
        if is_word_guessed(secret_word,letters_guessed) == True:
          print("Congratulations, you won !")
          print(f"Your total score is {num_of_guesses*len(letters_guessed)}")
          break
        #Don't forget to decrement num_of_guesses otherwise the loop will never end
        num_of_guesses -=  1
    
    #recheck that if we ran out of guesses and the secret word is not found yet
    if num_of_guesses == 0 and is_word_guessed(secret_word,letters_guessed) == False:
      print("Sorry, you ran out of guesses. The word is else")
      print(f"The secret word is '{secret_word}'")


      

    
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word): #checked
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word) != len(other_word):
      return False
    else:
      n = len(my_word)
      #initialize the loop
      for i in range(n):
        if my_word[i].isalpha() == True: #checking a letter is matched or not
          if my_word[i] != other_word[i] : return False
      return True



def show_possible_matches(my_word): #checked
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for word in wordlist:
      if match_with_gaps(my_word,other_word=word) == True:
        print(word,end = ' ')




def hangman_with_hints(secret_word): #checked
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman !")
    
    print(f"I'm thinking of a word that is {len(secret_word)} letters long")
    sep_str = "----------------------"
    print(sep_str)
    #initialize the number of guesses : 6
    num_of_guesses = 6
    #initialize the list of guessed letters so far
    letters_guessed = []
    #initialize the number of warnings, when you have 0 warnings and you insert 
    #an invalid input such as string,number,etc... you will lose 1 point
    num_of_warnings = 3

    #be sure that taking the advantages of 3 helper funcs : is_word_guessed,get_guessed_word
    #get_available_letters
    
    #The game keep continuing whenever num_of_guesses > 0:
    while num_of_guesses > 0:
      print(f"You have {num_of_guesses} guesses left")
      print(f"Available letters : {get_available_letters(letters_guessed)}")
      #taking the guessed lette
      letter = input("Please guess a letter : ")
      #REMEMBER ADDING THE GAME RULES. except the rule that a wrong vowel will lose 2 points
      #adding the asterisk case of input to show all hint words
      if letter == '*':
        print("Possible matched words are : ")
        show_possible_matches(my_word=f"{get_guessed_word(secret_word,letters_guessed)}")
        print("") #to end a print line of hint words
        print(sep_str)
        pass

      #The case input is invalid
      elif len(letter) > 1 or letter.isalpha() == False: 
        if num_of_warnings > 0:
          num_of_warnings -= 1
          print(f"Oops, that is not a valid letter. You have {num_of_warnings} warnings left")
        else: #The case when we have 0 warnings left
          print("Oops, that is not a valid letter. You have no warnings left, so you lose one guess")
          num_of_guesses -= 1
        #print sep_str to end a guess
        print(sep_str)
      
      #The case when input is a guessed letter 
      elif letter in letters_guessed:
        if num_of_warnings > 0 : 
          num_of_warnings -= 1
          print(f"Oops, you've already guessed this letter. You have {num_of_warnings} warnings left")
        else: #The case when we have 0 warnings left
          print("Oops,you've guessed this letter. You have no warnings left, so you lose one guess")
          num_of_guesses -= 1
        #print sep_str to end a guess 
        print(sep_str)
      
        
      else: #the case that input is valid
        #update the letter_guessed list (for the case the input is valid)
        letters_guessed.append(letter)
        #start checking whether the guessed letter is in secret_word or not
        if letter in secret_word:
          print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}")
        else:
          print(f"Oops, that letter is not in my word: {get_guessed_word(secret_word,letters_guessed)} ")

        #Adding separate string after each guess
        print(sep_str)
        #checking whether the secret word is guessed or not
        if is_word_guessed(secret_word,letters_guessed) == True:
          print("Congratulations, you won !")
          print(f"Your total score is {num_of_guesses*len(letters_guessed)}")
          break
        #Don't forget to decrement num_of_guesses otherwise the loop will never end
        num_of_guesses -=  1
    
    #recheck that if we ran out of guesses and the secret word is not found yet
    if num_of_guesses == 0 and is_word_guessed(secret_word,letters_guessed) == False:
      print("Sorry, you ran out of guesses. The word is else")
      print(f"The secret word is '{secret_word}'")


    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)



###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
