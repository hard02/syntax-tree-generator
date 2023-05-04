import nltk
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")


def generate_syntax_tree(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return nltk.ne_chunk(tagged)

sentence = input("enter your sentence:")
syntax_tree = generate_syntax_tree(sentence)
print(syntax_tree)
syntax_tree.draw()
