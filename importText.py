# -*- coding:utf=8 -*-
from __future__ import division
import nltk
import codecs

def lexical_diversity(txt):
    return len(txt)/len(set(txt))

# read in textfile
f = open('document.txt')
raw = f.read()

#tokenize the raw text
tokens = nltk.word_tokenize(raw)

# turn it into a full text
text1 = nltk.Text(tokens)

# get information about text
text1.concordance("China")
text1.similar("China")
text1.collocations()
countword = text1.count("China")
print(countword)

lexdiv = lexical_diversity(text1)
print (lexdiv)

freqdist1 = nltk.FreqDist(text1)
print (freqdist1.most_common())




