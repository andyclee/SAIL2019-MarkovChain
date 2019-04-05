from parser import Parser
from graph import Graph

class Generator:
    '''
    Generator that puts the Parser and Graph classes to work
    markov_graph: Graph instance representing a Markov chain for the corpus
        in filename
    '''
    def __init__(self, filename):
        parser = Parser(filename)
        tokens = parser.getTokens()
        self.markov_graph = Graph(tokens)

    def gen_first_word(self):
        '''Pick a first word based on start_frequencies'''

    def gen_next_word(self, curr_word):
        '''Given a graph and a current word, randomly pick a next word'''

    def gen_sentence(self, length):
        '''Generate a sentence given a graph representing a Markov chain'''
        sentence = ""
        last_word = self.gen_first_word()
        for word_ind in range(length-1):
            sentence += last_word + " "
            last_word = self.gen_next_word(last_word)

        sentence += last_word + "."
        
        return sentence
