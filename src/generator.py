from src.parser import Parser
from src.graph import Graph
import random

class Generator:
    '''
    Generator that puts the Parser and Graph classes to work
    graph: Graph instance representing a Markov chain for the corpus in filename
    MAX_WORDS: limit on most words in a sentence we can generate
    '''
    def __init__(self, filename):
        parser = Parser(filename)
        tokens = parser.tokens
        self.graph = Graph(tokens)
        self.MAX_WORDS = 1000
        self.WORD_FAILURE = '~~~'

    def gen_first_word(self):
        '''Pick a first word based on start_frequencies'''
        idx = random.randint(0, self.graph.starts)
        for key, value in self.graph.vertices.items(): 
            if idx <= value.start_freq:
                return key
            else:
                idx -= value.start_freq

        return "Inconcievable!"

    def gen_next_word(self, curr_word):
        '''Given a graph and a current word, randomly pick a next word'''
        curr_vertex = self.graph.vertices[curr_word]
        if curr_vertex.total_edge_weight == 0:
            return self.WORD_FAILURE
        idx = random.randint(0, curr_vertex.total_edge_weight)
        counter = 0
        for key, value in curr_vertex.edges.items(): 
            counter += value
            if counter >= idx:
                return key.word

        return self.WORD_FAILURE

    def stop(self, curr_word):
        '''Given a current word, randomly decide whether or not we should
        stop'''
        curr_vertex = self.graph.vertices[curr_word]
        stop_chance = curr_vertex.term_freq / curr_vertex.total_freq
        choice = random.random()
        return (choice <= stop_chance)

    def gen_sentence(self):
        '''Generate a sentence given a graph representing a Markov chain'''
        sentence = ""
        last_word = self.gen_first_word()
        counter = 1
        while(not self.stop(last_word) and counter < self.MAX_WORDS):
            sentence +=  " " + last_word
            last_word = self.gen_next_word(last_word)
            if last_word == self.WORD_FAILURE:
                last_word = ""
                break
            counter += 1

        sentence += " " + last_word + "."
        
        return sentence[1:]
