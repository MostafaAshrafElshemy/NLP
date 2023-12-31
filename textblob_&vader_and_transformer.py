# -*- coding: utf-8 -*-
"""TextBlob &VADER and TransFormer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bg4zNFF7UuvqNY7iPdlKiYiBOPwr0sqB
"""

sentence_1 = "I hed a great time at the movie it was really funny"

sentence_2 = "I hed a great time at the movie but the parking was terrible"

sentence_3 = "I hed a great time at the movie but the parking was't "

sentence_4 = "I hed a great time at the movie "

"""# TextBlob"""

from textblob import TextBlob

print(sentence_1)

print(sentence_1)
sentiment_score_1 = TextBlob(sentence_1)

print(sentiment_score_1.sentiment.polarity)

print(sentence_2)
sentiment_score_2 = TextBlob(sentence_2)

print(sentiment_score_2.sentiment.polarity)

print(sentence_3)
sentiment_score_3 = TextBlob(sentence_3)

print(sentiment_score_3.sentiment.polarity)

print(sentence_4)
sentiment_score_4 = TextBlob(sentence_4)

print(sentiment_score_4.sentiment.polarity)

"""# VADER"""

pip install vaderSentiment

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

import nltk
nltk.downloader.download('vader_lexicon')

print(sentence_1)

print(sid.polarity_scores(sentence_1))

print(sentence_2)

print(sid.polarity_scores(sentence_2))

print(sentence_3)

print(sid.polarity_scores(sentence_3))

print(sentence_4)

print(sid.polarity_scores(sentence_4))

"""# Pre _ Trained TransFormer"""

import transformers
from transformers import pipeline

sentiment_pipeline  = pipeline("sentiment-analysis")

print(sentence_1)

sentiment_pipeline(sentence_1)

print(sentence_2)

sentiment_pipeline(sentence_2)

print(sentence_3)

sentiment_pipeline(sentence_3)

print(sentence_4)

sentiment_pipeline(sentence_4)

"""# specific _ model"""

specifi_model = pipeline("sentiment-analysis" , model="finiteautomata/bertweet-base-sentiment-analysis")

print(sentence_1)

specifi_model(sentence_1)

print(sentence_2)

specifi_model(sentence_2)

print(sentence_3)

specifi_model(sentence_3)

print(sentence_4)

specifi_model(sentence_4)