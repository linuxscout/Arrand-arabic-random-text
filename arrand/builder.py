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

from . import rand_const
from . import arrandom

class generator:
    def __init__(self, filename):
        ## a word dict for bigrams
        self.word_dict = {}
        # build word model
        self.word_dict = self.build_word_dict(filename)
        
    def remove_forbidden(self, wordlist):
        """
        remove forbiden words to avoid miss undersood sentences
        """
        tmp_list = []
        for word in wordlist:
            if not word.endswith(u"لله") and word not in rand_const.FORBIDDEN:
                tmp_list.append(word)
        return tmp_list
        
    def build_word_dict(self, filename):
        
        words_dict = defaultdict(list)
        words = []
        with open(filename, encoding="utf8") as fl:
            words = fl.read().split()
            words = [ar.strip_tashkeel(w) for w in words]
        # remove forbiden words
        words = self.remove_forbidden(words)
        bigrams = zip(words, words[1:])
        for word1, word2 in bigrams:
            words_dict[word1].append(word2)
        for key in words_dict:
            words_dict[key] = list(set(words_dict[key]))
        return words_dict
    
    def rand_sentences(self, max_length=1, word_dict = {}):
        """
        Generate sentences with the generator
        """
        return arrandom.rand_sentences(max_length, self.word_dict)
        
if __name__ == '__main__':
    import sys
    filename = "../tests/samples/al3qd_alfarid.txt"
    ##
    mygen = generator(filename)
    mydict = generator.word_dict
    # print for file
    mydict = words_dict
    print("WORD_DICT= {")
    for key in mydict:
        print("u'%s': %s,"%(key, repr(mydict[key])))
    print("}")

    for i in range(10):
        sentence = mygen.rand_sentences()
        print(sentence)
