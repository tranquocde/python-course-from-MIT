# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

from cgitb import text
import string
import copy

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        #load_words() returns a list
        self.valid_words = load_words(file_name= 'words.txt')


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        ans = self.valid_words.copy()
        return ans


    def build_shift_dict(self, shift): #checked
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        ans = dict()
        lower_letters = string.ascii_lowercase
        n = len(lower_letters)
        #we shift the lower case first
        for i in range(n):
            shifted_pos = (i+shift)%n
            ans[lower_letters[i]] = lower_letters[shifted_pos] #shifting the letter
        for letter in lower_letters:
            upper_letter = letter.upper()
            ans[upper_letter] = ans[letter].upper()
        return ans



    def apply_shift(self, shift): #checked
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #DOES NOT MUTATE THE MESSAGE
        ans = ''
        for letter in self.message_text:
            if letter in self.build_shift_dict(shift):
                ans += self.build_shift_dict(shift)[letter] #adding the shifted letter to the answer
            else: #the case it is not a letter
                ans += letter
        return ans

class PlaintextMessage(Message):#checked
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        super().__init__(text) #inherit message_text and valid_words form Message class
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        #if we implement self.encryption_dict = self.build_shift_dict(shift)
        #then it will return the address in memory but not the result we want, so
        #we need to consider the parent class first then calling the method. Cause we are
        #not sure that self belongs to Message class
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):#checked
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):#checked
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encryption_dict_clone = self.encryption_dict.copy()
        return encryption_dict_clone

    def get_message_text_encrypted(self):#checked
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift): #checked
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)



class CiphertextMessage(Message): #checked
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max = 0
        word_list = self.get_valid_words()
        #shift is an integer running from 0 to 25
        for shift in range(26):
            num_of_matches = 0 #keep tracking the number of matched words
            decrypted_message = self.apply_shift(shift = 26-shift)
            list_of_words = decrypted_message.split()
            for word in list_of_words :
                if is_word(word_list ,word ) == True:
                    num_of_matches += 1
            if num_of_matches > max :
                max = num_of_matches
                ans = (26-shift,decrypted_message)
        return ans


if __name__ == '__main__':

   #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('this is my macbook.',shift = 10)
#    print(f"The original message: '{plaintext.get_message_text()}'\n" )
#    print(f"The message after encrypting with shift = {plaintext.get_shift()} : {plaintext.get_message_text_encrypted()}\n")
# #    plaintext.change_shift(shift = 1)
# #    print(f"The message after encrypting with shift = {plaintext.get_shift()} : {plaintext.get_message_text_encrypted()}\n")

   
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('drsc sc wi wkmlyyu.')
# #    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
   decryption = CiphertextMessage(get_story_string())
    #TODO: best shift value and unencrypted story 
   print(f"The best shift value is : {decryption.decrypt_message()[0]} ")
   print(f'The decrypted message is : \n "{decryption.decrypt_message()[1]}"')
    
    

