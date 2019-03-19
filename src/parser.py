import re
import string
import time

import nltk

class WordToken:
    """
    Word Token, stores information relevant to construction of Markov Chain
    word: The word itself
    prev: The previous word, may be None
    start: Whether it is the start of a sentence
    term: Whether it terminates a sentence
    """
    def __init__(self, word, prev, start, term):
        self.word = word
        self.prev = prev
        self.start = start
        self.term = term

class Parser:
    """
    Constructs a Chain from a given input dataset
    filename: The filename of the data file
    tokens: List of WordTokens from the data
    """
    def __init__(self, filename):
        self.filename = filename
        print("Parsing " + filename + " ...")
        start_time = time.time()
        self.tokens = self.get_tokens()
        end_time = time.time()
        print(filename + " parsed in " + str(end_time - start_time) + "seconds")

    def get_tokens(self):
        """
        Reads the given filename and tokenizes the document into a list of
        WordTokens
        """

        tokens = []

        #Opens and closes file, allows for reading
        with open(self.filename, 'r') as df:
            curline = df.readline()

            #Continue to read the file until we read an End Of File
            while curline:

                #Get sentences in each line
                sentences = nltk.sent_tokenize(curline)

                for sent in sentences:

                    #This will not give the best tokenization but is servicable
                    sent = sent.split(' ')
                    cleaned = [ word.translate(str.maketrans('', '', string.punctuation)).lower()
                            for word in sent ]

                    #For one word sentences
                    if len(sent) == 0:
                        continue
                    elif len(sent) == 1:
                        tokens.append(WordToken(cleaned[0], None, True, True))
                    else:

                        #Add first word
                        tokens.append(WordToken(cleaned[0], None, True, False))

                        #Add center words, do not add last word
                        center_indices = list(range(1, len(sent) - 1))
                        center_tokens = [ WordToken(cleaned[i], cleaned[i-1], False, False) 
                                for i in center_indices ]
                        tokens = tokens + center_tokens

                        #Add last word
                        tokens.append(WordToken(cleaned[-1], cleaned[-2], False, True))

                #Move on to next line
                curline = df.readline()
