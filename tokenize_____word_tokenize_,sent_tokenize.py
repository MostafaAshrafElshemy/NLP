# -*- coding: utf-8 -*-
"""tokenize ___ word_tokenize ,sent_tokenize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12wraYCDhENt_pTk4rvybF97ltlTUxYD_
"""

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize ,sent_tokenize

sentences = "her cat's name is luna ,her dog's name is max"

sent_tokenize(sentences)

sentences1="her cat's name is luna"

word_tokenize(sentences1)

sentences2 = "her cat's name is luna ,her dog's name is max"

word_tokenize(sentences2)