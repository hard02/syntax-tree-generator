# syntax-tree-generator
The following repositories contain iterations of syntax tree generator which I tried to develop. The basic library which is required is Natural Language Toolkit (NLTK) library in Python which can be installed by pip by running the following command:

```pip install nltk```

It is recommended to install these dependent libraries as well:

```
pip install numpy
pip install matplotlib
pip install scipy
```

The following repo contains three iterations:


## iteration_1_parser:
- This iteration is using the Natural Language Toolkit (NLTK) library in Python to perform Named Entity Recognition (NER) on a user-entered sentence.

- First, the code imports the necessary functions from the NLTK library: word_tokenize for tokenizing the sentence into words and pos_tag for tagging each word with its part of speech. The user is then prompted to enter a sentence, and the input is stored in the variable "sentence".

- The code then tokenizes the sentence into individual words and tags each word with its part of speech. Next, the NLTK function ne_chunk is used to perform NER on the tagged sentence. This function identifies and labels named entities such as names, organizations, and locations.

- Finally, the resulting named entity chunks are displayed as a tree diagram using the draw() method. The tree diagram provides a visual representation of the named entities and their relationships within the sentence.


## iteration_2_parser:
This code defines a function called generate_syntax_tree which takes a sentence as an input and returns a syntax tree of the sentence using the Natural Language Toolkit (NLTK) library. The code begins by importing the NLTK library and downloading the necessary models for part-of-speech tagging and named entity recognition. This iteration contains the following functions: 

- The generate_syntax_tree function takes a sentence as an argument and tokenizes it into individual words using the word_tokenize function from NLTK. It then tags each word with its part of speech using the pos_tag function.

- The ne_chunk function from NLTK is then used to generate a syntax tree of the sentence, with named entities identified and labeled. The resulting syntax tree is returned by the function.

The main body of the code prompts the user to enter a sentence, and then calls the generate_syntax_tree function with the input sentence. The resulting syntax tree is printed to the console using the print function, and also displayed as a tree diagram using the draw method of the syntax tree object.


## finalised_parser:
- The final iteration is using the Natural Language Toolkit (NLTK) library in Python to extract different parts of speech from a given sentence and display them in a tree diagram. The code first imports the required libraries from NLTK and downloads the necessary models for tokenization and part-of-speech tagging. The example text is then defined in the variable sample_text.

- The code uses the pos_tag and word_tokenize functions from NLTK to tokenize the sentence into individual words and tag each word with its part of speech.

- The RegexpParser function is used to define regular expressions that specify patterns for different parts of speech. In this case, the regular expressions are used to extract noun phrases, prepositions, verbs, prepositional phrases, and verb phrases from the tagged sentence.

- The parse method of the chunker object is used to apply the regular expressions to the tagged sentence and extract the different parts of speech. The resulting tree structure is stored in the output variable.

The code then prints the extracted parts of speech and displays them as a tree diagram using the draw method of the output object.
