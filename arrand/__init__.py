"""
Arrand: Arabic Random Text Generator

This is the top-level API that exposes core functionality for easy import.
"""

# Expose public functions from arrandom
from .arrandom import (
    aya,
    hadith,
    phrase,
    proverb,
    poem,
    paragraph,
    word,
    select,
    sample,
    rand_sentence,
    rand_sentences,
)

# Expose builder API
from .builder import generator

__all__ = [
    "aya",
    "hadith",
    "phrase",
    "proverb",
    "poem",
    "paragraph",
    "word",
    "select",
    "sample",
    "rand_sentence",
    "rand_sentences",
    "generator",
]
