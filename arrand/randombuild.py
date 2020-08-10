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
import random

from io import open
from collections import defaultdict
import pprint
import pyarabic.araby as ar

import rand_const
def remove_forbidden(wordlist):
    """
    remove forbiden words to avoid miss undersood sentences
    """
    tmp_list = []
    for word in wordlist:
        if not word.endswith(u"لله") and word not in rand_const.FORBIDDEN:
            tmp_list.append(word)
    return tmp_list
    
def build_random(filename):
    
    words_dict = defaultdict(list)
    words = []
    with open(filename, encoding="utf8") as fl:
        words = fl.read().split()
        words = [ar.strip_tashkeel(w) for w in words]
    # remove forbiden words
    words = remove_forbidden(words)
    bigrams = zip(words, words[1:])
    for word1, word2 in bigrams:
        words_dict[word1].append(word2)
    for key in words_dict:
        words_dict[key] = list(set(words_dict[key]))
    return words_dict
def generator(word_dict):
    
    wordlist = []    
    # first word from keys
    word = random.choice(list(word_dict.keys()))
    wordlist.append(word) 
    while not word.endswith("."):
        word = random.choice(word_dict[word])
        wordlist.append(word)
        
    return u" ".join(wordlist)
if __name__ == '__main__':
    import sys
    filename = "../tests/samples/al3qd_alfarid.txt"
    words_dict = build_random(filename)
    #~ pprint.pprint(words_dict)
    # print for file
    mydict = words_dict
    print("WORD_DICT= {")
    for key in mydict:
        print("u'%s': %s,"%(key, repr(mydict[key])))
    print("}")

    #~ for i in range(10):
        #~ sentence = generator(words_dict)
        #~ print(sentence)
