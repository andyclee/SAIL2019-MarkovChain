from collections import defaultdict

class Vertex:
    """
    Vertex in Graph
    word: The word the vertex represents
    edges: Map of edges which have this vertex as a source to frequency (Vertex:Int)
    term_freq: Number of times this vertex terminates a sentence
    start_freq: Number of times this vertex starts a sentence
    """
    def __init__(self, word):
        self.word = word
        self.edges = defaultdict(lambda : 0)
        self.term_freq = 0
        self.start_freq = 0

        """
        If you are more concerned about time than space, you may wish to
        create dedicated lists for start and term
        """

    def __eq__(self, other):
        """
        We will say two vertices are equal if they have the same word
        This will make it easier to check if we have seen a word already
        """
        return self.word == other.word

    def __hash__(self):
        """
        We must make the object hashable, we assume that each vertex has
        a unique word but we do not enforce this
        """
        return hash(self.word)

class Graph:
    """
    Modified directed Graph structure, creates the chain from list of WordTokens
    tokens: List of all tokens
    vertices: Dictionary of vertex to edge list
    starts: Number of starts
    terms: Number of terms
    """

    def __init__(self, tokens):
        self.tokens = tokens

        #Graph represented by set of vertices containing sets of edges (edge list)
        self.vertices = {}

        self.starts = 0
        self.terms = 0

        self.create_graph()

    def create_graph(self):

        #Parse the tokens into graph
        for token in tokens:
            self.starts += int(token.start)
            self.terms += int(token.term)

            #The word was already in the vertex set
            if token.word in self.vertices:

                #Update start and term freqs
                self.vertices[token.word].start_freq += int(token.start)
                self.vertices[token.word].term_freq += int(token.term)
            else:

                #Create a new vertex
                new_vertex = Vertex(token.word)
                if token.start:
                    new_vertex.start_freq = 1
                if token.term:
                    new_vertex.term_freq = 1
                self.vertices[token.word] = new_vertex

            #Add to edge list
            self.vertices[token.prev].edges[self.vertices[token.word]] += 1
