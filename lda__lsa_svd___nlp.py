# -*- coding: utf-8 -*-
"""LDA _LSA_SVD___NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10qZsNwiizwUlFVr_5yhPZadLUdTgyBbE
"""

import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import gensim
import gensim.corpora as corpora

data = pd.read_csv("/content/drive/MyDrive/news_articles.csv")
data.head()

data.info()

articies = data['content']

articies

from gensim.corpora import Dictionary

articies = articies.str.split()

dictionary = Dictionary(articies)


print(dictionary)



#
doc_term =[dictionary.doc2bow(text) for text in articies]

print(doc_term)

num_topics = 2

lda_model = gensim.models.LdaModel(corpus=doc_term ,
                                   ld2word = dictionary,
                                   num_topics=num_topics)

#lda_ = gensim.models.LdaModel(corpus=doc_term,ld2word = dictionary,num_topics=num_topics)

lda_model = gensim.models.LdaModel(corpus=doc_term ,
                                   num_topics=num_topics)

lda_model.print_topics(num_topics=num_topics , num_words=5)

from gensim.models import LsiModel

lsa_model = LsiModel(corpus=doc_term , num_topics=num_topics)

lsa_model.print_topics(num_topics=num_topics , num_words=5)