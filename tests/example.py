#!/usr/bin/python
# -*- coding=UTF-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../')) # used for core
import arrand.arrandom

## Random text
arrand.arrandom.select()
## Select Hadith
arrand.arrandom.hadith()
## Select Aya
arrand.arrandom.aya()
## Select Proverb
arrand.arrandom.proverb()
## Select phrase
arrand.arrandom.phrase()
## select word
arrand.arrandom.word()
## Select poem
arrand.arrandom.poem()

## Sample many
arrand.arrandom.sample(category = "text", max_length=2, vocalized=False)
arrand.arrandom.sample(category = "hadith", max_length=2, vocalized=False)
arrand.arrandom.sample(category = "poem", max_length=2, vocalized=False)
## vocalized
arrand.arrandom.sample(category = "text", max_length=2, vocalized=True)
arrand.arrandom.sample(category = "hadith", max_length=2, vocalized=True)
arrand.arrandom.sample(category = "poem", max_length=2, vocalized=True)
arrand.arrandom.hadith(vocalized=True)
arrand.arrandom.aya(vocalized=True)
arrand.arrandom.proverb(vocalized=True)
arrand.arrandom.phrase(vocalized=True)
arrand.arrandom.poem(vocalized=True)

## Select Generic
arrand.arrandom.rand_sentences(3)
## Select non sense text
arrand.arrandom.rand_sentence()


