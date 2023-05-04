import nltk
from nltk import word_tokenize, pos_tag

sentence = input("enter the sentence: ") 

tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

tree = nltk.ne_chunk(tagged)
tree.draw()