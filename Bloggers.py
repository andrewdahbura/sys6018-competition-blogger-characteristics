#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:46:21 2018

@author: amd6ua
"""

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

#Get initial look at data
train.head()

#lowercase
train['text'] = train['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))
train['text'].head()

#remove punctuation
train['text'] = train['text'].str.replace('[^\w\s]','')
train['word_count2'] = train['text'].apply(lambda x: len(str(x).split(" ")))
train['text'].head()

#remove stop words
from nltk.corpus import stopwords
stop = stopwords.words('english')
train['text'] = train['text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
train['word_count3'] = train['text'].apply(lambda x: len(str(x).split(" ")))
train['text'].head()

freq = pd.Series(' '.join(train['text']).split()).value_counts()[-10:]

#remove uncommon words
freq = list(freq.index)
train['text'] = train['text'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
train['text'].head()

###remove common words###
freq = pd.Series(' '.join(train['text']).split()).value_counts()[:10]
freq = list(freq.index)
train['text'] = train['text'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
#Visualize
train['text'].head()

###Remove rare words###
freq = pd.Series(' '.join(train['tweet']).split()).value_counts()[-10:]
freq = list(freq.index)
train['text'] = train['text'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
#Visualize
train['text'].head()

###Spelling correction###
from textblob import TextBlob
train['text'][:5].apply(lambda x: str(TextBlob(x).correct()))

###Tokenization (dividing the text into a sequence of words or sentences)###
TextBlob(train['text'][1]).words

#Stemming (removal of suffices, like “ing”, “ly”, “s”, etc. by a simple rule-based approach)
#from nltk.stem import PorterStemmer
#st = PorterStemmer()
#train['text'][:5].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

#Lemmatization (more effective option than stemming because 
# converts the word into its root word, rather than just stripping the suffices)
#*Preferred to stemming*#

from textblob import Word
train['text'] = train['text'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
train['text'].head()















