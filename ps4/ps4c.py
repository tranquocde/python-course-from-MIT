# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xxk

from cgitb import text
import string

# from zmq import EVENT_HANDSHAKE_FAILED_NO_DETAIL
from ps4a import get_permutations

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

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text): #checked
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        self.message_text = text
        self.valid_words = load_words(file_name='words.txt')

        
    def get_message_text(self):#checked
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self): #checked
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        ans = self.valid_words.copy()
        return ans               

    def build_transpose_dict(self, vowels_permutation): #checked
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        ans = dict()
        num_of_vowel = len(VOWELS_LOWER)
        for index in range(num_of_vowel):
            ans[VOWELS_LOWER[index]] = vowels_permutation[index]
            ans[VOWELS_UPPER[index]] = vowels_permutation[index].upper()
        for consonant_lower  in CONSONANTS_LOWER:
            ans[consonant_lower] = consonant_lower
        for consonant_upper in CONSONANTS_UPPER:
            ans[consonant_upper] = consonant_upper
        return ans


    def apply_transpose(self, transpose_dict): #checked
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        ans = ''
        message = self.get_message_text()
        for letter in message:
            if letter in transpose_dict:
                ans += transpose_dict[letter]
            else:
                ans += letter
        return ans

        
        
class EncryptedSubMessage(SubMessage): #checked
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        word_list = self.get_valid_words()
        max = 0
        for vowels_permutation in get_permutations(sequence=VOWELS_LOWER):
            transpose_dict = self.build_transpose_dict(vowels_permutation)
            encrypted_message = self.apply_transpose(transpose_dict)
            list_of_words_in_encryption = encrypted_message.split()
            num_of_matches = 0
            for word in list_of_words_in_encryption:
                if is_word(word_list, word) ==True :
                    num_of_matches += 1
            if num_of_matches > max:
                max = num_of_matches
                ans = encrypted_message
        return ans





if __name__ == '__main__':

    # Example test case
    message = SubMessage(text ='Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.' )
    permutation = "ueaio"
    enc_dict = message.build_transpose_dict(permutation)
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print(f"Encrypted message: {enc_message.get_message_text()}")
    # print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    
    