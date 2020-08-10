#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  random.py
#  
#  Copyright 2020 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
"""
Arabic random text generator
"""
import os.path
import sys
import random
from . import rand_const as rconst
from . import nonsense_const

def select(category="text",  vocalized = False,):
    """
    Select a random text from a category
    
    @param category: the selected category (text, paragraph, phrase, Hadith, Aya, proverb, poem)
    @type category: unicode
    @param max: maximun units of text to select
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    lines = sample(category, 1, vocalized)
    if lines:
        return lines[0]
    else:
        return ""
def hadith(vocalized = False,):
    """
    Select a random hadith from a category
    
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    return select("hadith", vocalized)
def phrase(vocalized = False,):
    """
    Select a random phrase from a category
    
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    return select("hadith", vocalized)
        
def paragraph(vocalized = False,):
    """
    Select a random paragraph from a category
    
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    return select("paragraph", vocalized)
        
def proverb(vocalized = False,):
    """
    Select a random proverb from a category
    
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    return select("proverb", vocalized)
def aya(vocalized = False,):
    """
    Select a random aya from a category
    
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    return select("aya", vocalized)

def poem(vocalized = False,):
    """
    Select a random poem from a category
    
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    return select("poem", vocalized)


def sample(category="text",  max_length=1, vocalized = False,):
    """
    Select a random text from a category with a maximum units
    
    @param category: the selected category (text, paragraph, phrase, Hadith, Aya, proverb, poem)
    @type category: unicode
    @param max_length: maximun units of text to select
    @type max_length: int, default 1
    @param vocalized: want to select vocalized text
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    lines = []
    # select the file according to category
    filename = rconst.CATEGORY_FILENAMES.get(category.lower(), "texts.txt")
    # read file and get random lines
    # get the database path
    if hasattr(sys, 'frozen'): # only when running in py2exe this exists
        base = sys.prefix
    else: # otherwise this is a regular python script
        base = os.path.dirname(os.path.realpath(__file__))
    if vocalized:
        filepath = os.path.join(base, "data/vocalized", filename)
    else:
        filepath = os.path.join(base, "data", filename)
        
    try:
        with open(filepath) as fl:
            lines  = fl.readlines()
    except:
        print("File not found %s!"%filepath)
        sys.exit()
    if lines:
        lines = random.sample(lines, max_length)
        lines  = [l.strip() for l in lines]
    return lines

def rand_sentence(word_dict = {}):
    """
    Select a random sentence with non sense
    
    @param category: the selected category (text, paragraph, phrase, Hadith, Aya, proverb, poem)
    @type category: unicode
    @param max_length: maximun units of text to select
    @type max_length: int, default 1
    @param vocalized: want to select vocalized text
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    if not word_dict or type(word_dict) != dict:
        word_dict = nonsense_const.WORDS_DICT
    # given word_dict
    wordlist = []    
    # first word from keys
    word = random.choice(list(word_dict.keys()))
    wordlist.append(word) 
    while not word.endswith("."):
        choices = word_dict.get(word, [])
        if not choices:
            break
        word = random.choice(choices)
        wordlist.append(word)
        
    return u" ".join(wordlist)      

def rand_sentences(max_length=1, word_dict = {}):
    """
    Select a random text with non sense with a maximum units
    
    @param category: the selected category (text, paragraph, phrase, Hadith, Aya, proverb, poem)
    @type category: unicode
    @param max_length: maximun units of text to select
    @type max_length: int, default 1
    @param vocalized: want to select vocalized text
    @type vocalized: boolean, default False
    @return: a list of random text units
    @type: list of string
    """
    lines = []
    for i in range(max_length):
        lines.append(rand_sentence(word_dict))
    return lines

def main(args):
    return 0

if __name__ == '__main__':
    lines = sample('text', 4)
    print(lines)
    lines = select('text')
    print(lines)
    print(hadith())
    import sys
    sys.exit(main(sys.argv))
