"""
File that contains the functions of the project

Includes:

keep_and_define
go_for_word
"""


#Import statements
import random
import pandas as pd

from Module.classes import Words

def keep_and_define(w_list):
    """
    Look at a word list and make a
    new dictionary with words a user
    wants to keep and define.
    
    w_list = List of words to iterate
    through
    """
    out_dict = {}
    
    #Loop through the list and either keep and define or remove from a new dictonary
    try:
        for value in w_list:
            response = input("Keep " + value +  " (y/n): ")
            if response == 'y':
                out_dict[value] = input("Give definition: ")
            elif response == 'n':
                continue
            else:
                print("Please type 'y' or 'n', word has been skipped.")
                
        return out_dict
    
    #Skip word and tell user if they didn't input y or n
    except response != y or response != n:
        
        print("Please only type 'y' or 'n' (case sensitive); word skipped.")
    
def go_for_word(input_word):
    """
    Have the computer randomly generate words
    until it gets a specified word. Only creates
    words with the length of the specified word
    the computer is searching for.
    """
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    
    w = Words(length = len(input_word))
    input_word = input_word.upper()
    
    for character in input_word:
        if character not in alphabet:
            print("Not a valid letter.")
            err_msg = "Not a valid letter."
            return err_msg
        else:
            
            continue
    
    while input_word not in w.word_list:
        w.create()
        
    print(w.word_list)    
    print("It took: " + str(len(w.word_list)) + " words to get " + input_word + ".")
    
    return len(w.word_list)
    