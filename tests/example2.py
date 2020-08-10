#!/usr/bin/python
# -*- coding=UTF-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../')) # used for core
#~ import arrand.arrandom
import arrand.builder

#~ filename = "samples/al3qd_alfarid.txt"
filename = "/home/zerrouki/workspace/projects/arrand/tests/samples/al3qd_alfarid.txt"
##
mygen = arrand.builder.generator(filename)
mydict = mygen.word_dict
# print for file
print("WORD_DICT= {")
for key in mydict:
    print("u'%s': %s,"%(key, repr(mydict[key])))
print("}")

sentence = mygen.rand_sentences(2)
print(sentence)

