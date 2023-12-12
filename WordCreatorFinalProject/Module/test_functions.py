"""
Test class and non-class
functions and attributes.
"""

#import statements
import pandas as pd
from Module.classes import Words
from Module.functions import keep_and_define, go_for_word

w = Words(length = 1)
w2 = Words()

def test_attributes():
    
    w = Words(length = 1)
    w2 = Words()
    assert w.length == 1
    assert w2.length == 0
    assert w.word_list == []

def test_create():
    
    assert len(w.create()) == 1
    assert len(w.create(bias = False)) == 1
    assert len(w2.create()) == 0

def test_make_many():
    
    assert len(w.make_many()) == 5
    assert len(w.make_many(num_of_words = 4, normalize_len=False )[3]) == 4
    assert len(w.make_many(num_of_words=1)) == 1

def test_go_for_word():
    
    w.create()
    w.clear()

    assert w.word_list == []
    assert go_for_word('E')
    assert go_for_word('e')
    assert go_for_word('5') == "Not a valid letter."