import nltk

# Import the necessary functions for tokenization and part-of-speech tagging
from nltk import word_tokenize, pos_tag


sentence = input("enter the sentence: ")    

tokens = word_tokenize(sentence)  # Tokenize the sentence into individual words
tagged = pos_tag(tokens) # Tag each word with its part of speech

tree = nltk.ne_chunk(tagged)  # Apply named entity recognition to the tagged sentence
tree.draw()
