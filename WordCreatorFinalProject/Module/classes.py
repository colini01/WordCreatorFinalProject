"""
File for the Words class.
Contains the methods:

create
make_many
clear
"""

#Import statements
import random
import pandas as pd

class Words:
    
    """
    Class that stores lists of previously made words,
    stored, contains functions to create() for creating
    words, and make_many() for making many words
    
    length = length of word to default to when creating
    words. Defaults = 0
    
    word_list = list of words created, defaults as []
    """
        
    def __init__(self, length=0, word_list=[]):
        """
        Create instance attributes, length, name of most recent word created, word_list.
        
        length default = 0
        word_list default = []
        """
        
        self.length = length
        self.name = ''
        self.word_list = word_list
        
    def create(self, bias=True):
        """
        Creates a word with the ability to have a
        bias towards typical word frequencies used
        in english according to this data:
        
        https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
        (frequency data based off that and changed
        to create ranges when computing a random number
        0.00-100.00)
        
        Gets a random number 0.00-100.00 and checks
        the list, going lowest frequency to largest,
        to see if that number is less than the 
        frequency of the current row, if it is, it
        gets the letter of the row and cocatenates it
        to the word string.
        
        bias: whether to keep the words completely
        random or use frequency data. Default = True
        """
        
        #Number Dataframe
        row1 = {'letter': 'E', 'frequency': 100.00}
        row2 = {'letter': 'T', 'frequency': 87.97}
        row3 = {'letter': 'A', 'frequency': 78.87}
        row4 = {'letter': 'O', 'frequency': 70.75}
        row5 = {'letter': 'I', 'frequency': 63.07}
        row6 = {'letter': 'N', 'frequency': 55.76}
        row7 = {'letter': 'S', 'frequency': 48.81}
        row8 = {'letter': 'R', 'frequency': 42.53}
        row9 = {'letter': 'H', 'frequency': 36.51}
        row10 = {'letter': 'D', 'frequency': 30.59}
        row11 = {'letter': 'L', 'frequency': 26.27}
        row12 = {'letter': 'U', 'frequency': 22.29}
        row13 = {'letter': 'C', 'frequency': 19.41}
        row14 = {'letter': 'M', 'frequency': 16.70}
        row15 = {'letter': 'F', 'frequency': 14.09}
        row16 = {'letter': 'Y', 'frequency': 11.79}
        row17 = {'letter': 'W', 'frequency': 9.68}
        row18 = {'letter': 'G', 'frequency': 7.59}
        row19 = {'letter': 'P', 'frequency': 5.56}
        row20 = {'letter': 'B', 'frequency': 3.74}
        row21 = {'letter': 'V', 'frequency': 2.25}
        row22 = {'letter': 'K', 'frequency': 1.14}
        row23 = {'letter': 'X', 'frequency': 0.45}
        row24 = {'letter': 'Q', 'frequency': 0.28}
        row25 = {'letter': 'J', 'frequency': 0.17}
        row26 = {'letter': 'Z', 'frequency': 0.07}
        
        freq = pd.DataFrame([ row1, row2,  row3,  row4,  row5,  row6,
                             row7,  row8,  row9,  row10, row11, row12,
                             row13, row14, row15, row16, row17, row18,
                             row19, row20, row21, row22, row23, row24,
                             row25, row26])
        out_str = ""
        
        #Create word using Dataframe and self.length
        for i in range(self.length):
            rand_num = round(random.uniform(0.00, 100.00), 2)

            for i in reversed(range(freq.shape[0])):
                if rand_num < freq.iat[i, 1]:
                    out_str = out_str + freq.iat[i, 0]
                    break
                else:
                    continue


        self.word_name = out_str
        self.word_list.append(out_str)
        return out_str
    
    
    def make_many(self, num_of_words=5, normalize_len=True, length=4):
        """
        Create a bunch of words at once. 
        Has option to have a length of 3-7
        letters per word. 
        
        Uses create() with a local langth
        variable. If normalize_len is False,
        creates words all at the same length.
        If normalize_len is True, makes words
        varying from 3-7, which are not too
        short and not too long.
        
        self = Words() instance
        
        num_of_words = how many words to create
        default = 5
        
        normalize_len = True to have words vary
        in length from 3-7 letters. False to
        have the same length
        default = True
        
        length = length of words if normalize_len
        is False.
        default = 4
        
        """
        
        word_list = []
        if normalize_len == False:
            
            for i in range(num_of_words):
                word_list.append(Words(length).create())
        else:
            
            for i in range(num_of_words):
                length = random.randrange(3, 7)
                word_list.append(Words(length).create())
                
        self.word_list = self.word_list + word_list
        return word_list

    def clear(self):
        """
        Makes the list of the instance empty.
        
        self = Words() instance
        """
        
        self.word_list = []