# -*- coding: utf-8 -*-
"""Intro NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dB0YmAIzdYql2YckyWNIFqwm022ZWXLO
"""

sentence = "Her Cat's name luna"
lower_sentence = sentence.lower()
print(lower_sentence)

lower_list=['SUPPLY,TEST AND INSTALL HEAVY DUTY IN-LINE DUCTEDCENTRIFUGAL FANS TO SPP,OR APPROVED EQUAL WITHALL HANGERS, SUPPORTS, VIBRATION/ SEISMICPROTECTION EQUIPMENT, ELECTRIC CONNECTION,CONTROLS AND WIRING TO SPECIFICATIONS ANDDRAWINGS, AND ALL THE NECESSARY TO COMPLETE THEWORK,THE ITEM INCLUDE THE MCC AND ALL THE']

lower_sentence_list =[x.lower()  for x in lower_list]

print(lower_sentence_list)

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

en_stopwords = stopwords.words('english')
print(en_stopwords)

sentence=  " it  was  too  for  to  go  to  the  shop  and he  did  want her to walk "

sentence_on_stopwords=' '.join([ word  for  word  in  sentence.split()  if  word  not in  en_stopwords])

print(sentence_on_stopwords)

en_stopwords.remove('did')
en_stopwords.remove('not')

en_stopwords.append('go')

sentence_on_stopwords_cons=' '.join([ word  for  word  in  sentence.split()  if  word  not in  en_stopwords])

print(sentence_on_stopwords_cons)